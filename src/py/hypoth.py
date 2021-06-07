
from __future__ import annotations
from math import sqrt
from scipy.stats import norm, t


class HypothesisTest():
    """
    """

    # ========================================================================
    # static methods
    # ========================================================================

    @staticmethod
    def get_test_stat(x1: float, val: float, sd: float, size: int) -> float:
        """
        returns
        =======
        float : value of the test statistic

        params
        ======
        mu : float
            sample mean
        mu0 : float
            hypothesised value for the mean
        sd : float
            sample standard deviation
        size : int
            sample size
        """

        return (x1-val) / (sd/sqrt(size))

    def get_p(test_stat: float, alternative: str) -> float:
        """
        returns
        =======
        float : p-value, based on the normal distribution.

        params
        ======
        test_stat : float
            value of the test statistic
        alternative :
            The alternative hypothesis, H1.
            Accepts either 'two-sided', 'larger', or 'smaller'
        """
        pval: float = 0
        if (alternative == "two-sided"):
            pval = 2 * norm().sf(abs(test_stat))
        elif (alternative == "larger"):
            pval = norm().sf(test_stat)
        elif (alternative == "smaller"):
            pval = norm().cdf(test_stat)
        else:
            print(
                "Please enter a valud alternative hypothesis: "
                + "two-tailed, larger, or smaller.")
            pval = "NaN"
        return pval

    def make_param_dict(
            teststat: str,
            teststatval: float,
            pval: float) -> dict:
        """
        returns
        =======
        dict : a dictionary with keys teststat and pval

        params
        ======
        teststat : str
            the test statistic being calculated, to be used as the key
            in the dictionary
        teststatval : float
            value of the test statistic
        pval : float
            p-value of the test
        """

        a_dict: dict = dict()
        a_dict[teststat] = round(teststatval, 6)
        a_dict["pval"] = round(pval, 6)
        return a_dict

    @staticmethod
    def ztest_1sample(
            mu: float,
            sd: float,
            size: int,
            mu0: float = 0,
            alternative: str = "two-sided") -> dict:
        """
        returns
        =======
        dict : test statistic and the p-value of a one sample z-test,
        both rounded to 6dp

        params
        ======
        mu : float
            sample mean
        sd : float
            sample standard deviation
        size : int
            sample size
        mu0 : float, default is 0
            hypothesised value for the mean
        alternative : str, default is 'two-sided'
            The alternative hypothesis, H1.
            Accepts either 'two-sided', 'larger', or 'smaller'
        """

        # get test statistic
        zstat: float = HypothesisTest.get_test_stat(
            x1=mu, val=mu0, sd=sd, size=size)
        # get p-value
        pval: float = HypothesisTest.get_p(
            test_stat=zstat, alternative=alternative)

        return HypothesisTest.make_param_dict("zstat", zstat, pval)

    @staticmethod
    def ttest_1sample(
            mu: float,
            sd: float,
            size: int,
            mu0: float = 0,
            alternative: str = "two-sided") -> dict:
        """
        returns
        =======
        dict : test statistic and the p-value of a one sample t-test,
        both rounded to 6dp

        params
        ======
        mu : float
            sample mean
        sd : float
            sample standard deviation
        size : int
            sample size
        mu0 : float, default is 0
            hypothesised value for the mean
        alternative : str, default is 'two-sided'
            The alternative hypothesis, H1.
            Accepts either 'two-sided', 'larger', or 'smaller'
        """

        # get test statistic
        tstat: float = HypothesisTest.get_test_stat(
            x1=mu, val=mu0, sd=sd, size=size)
        # get p-value
        df: int = size - 1
        pval: float = 0
        if (alternative == "two-sided"):
            pval = 2 * t(df).sf(abs(tstat))
        elif (alternative == "larger"):
            pval = t(df).sf(tstat)
        elif (alternative == "smaller"):
            pval = t(df).cdf(tstat)
        else:
            print(
                "Please enter a valud alternative hypothesis: "
                + "two-tailed, larger, or smaller.")
            tstat = "NaN"
            pval = "NaN"

        return HypothesisTest.make_param_dict("tstat", tstat, pval)

    @staticmethod
    def ztest_prop(
            count: float,
            nobs: int,
            p0: float = 0,
            alternative: str = "two-sided") -> dict:
        """
        returns
        =======
        dict : test statistic and the p-value of a one sample z-test of
        the proportion, both rounded to 6dp

        params
        ======
        count : float
            number of 'successes' in the sample
        size : int
            sample size
        p0 : float, default is 0
            hypothesised value for the proportion
        alternative : str, default is 'two-sided'
            The alternative hypothesis, H1.
            Accepts either 'two-sided', 'larger', or 'smaller'
        """
        # get p
        p = count/nobs
        # get sd of p0
        sd = (p0*(1-p0)) ** 0.5
        # get test statistic
        zstat: float = HypothesisTest.get_test_stat(
            x1=p, val=p0, sd=sd, size=nobs)
        # get p-value
        pval: float = HypothesisTest.get_p(
            test_stat=zstat, alternative=alternative)

        return HypothesisTest.make_param_dict("zp_stat", zstat, pval)

    def wilcoxon(
            w: int,
            nobs: int,
            alternative: str = "two-sided") -> dict:
        """
        returns
        =======
        dict : E(W), v(W), test statistic and the p-value of a
        wilcoxon test, all values rounded to 6dp.

        params
        ======
        w : int
            test statistic
        nobs : int
            sample size, without zeroes
        alternative : str, default is 'two-sided'
            The alternative hypothesis, H1.
            Accepts either 'two-sided', 'larger', or 'smaller'
        """
        # get expected
        e_w: int = nobs*(nobs + 1)/4
        # get var
        v_w: int = nobs*(nobs + 1)*(2*nobs + 1)/24
        # get Z
        zstat: float = (w - e_w)/sqrt(v_w)
        # get p
        pval: float = HypothesisTest.get_p(
            test_stat=zstat, alternative=alternative)
        # construct dictionary
        a_dict: dict = dict()
        a_dict["E(W)"] = round(e_w, 6)
        a_dict["V(W)"] = round(v_w, 6)
        a_dict["zstat"] = round(zstat, 6)
        a_dict["p-value"] = round(pval, 6)

        return a_dict

    def mann_whitney(
            u: float,
            nobs1: int,
            nobs2: int,
            alternative: str = "two-sided") -> dict:
        """
        returns
        =======
        dict : E(U), v(U), test statistic and the p-value of a
        mann-whitney test, all values rounded to 6dp.

        params
        ======
        u : int
            test statistic
        nobs1 : int
            size of sample one
        nobs2 : int
            size of sample two
        alternative : str, default is 'two-sided'
            The alternative hypothesis, H1.
            Accepts either 'two-sided', 'larger', or 'smaller'
        """

        # get expected
        e_u: int = nobs1*(nobs1 + nobs2 + 1)/2
        # get var
        v_u: int = nobs1*nobs2*(nobs1 + nobs2 + 1)/12
        # get Z
        zstat: float = (u - e_u)/sqrt(v_u)
        # get p
        pval: float = HypothesisTest.get_p(
            test_stat=zstat, alternative=alternative)
        # construct dictionary
        a_dict: dict = dict()
        a_dict["E(U)"] = round(e_u, 6)
        a_dict["V(U)"] = round(e_u, 6)
        a_dict["zstat"] = round(zstat, 6)
        a_dict["p-value"] = round(pval, 6)

        return a_dict
