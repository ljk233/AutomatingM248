
from __future__ import annotations
from math import sqrt
from scipy.stats import norm, t


class ConfidenceInterval():
    """
    """

    # ========================================================================
    # static methods
    # ========================================================================

    @staticmethod
    def get_ci_as_dict(x: float, q: float, ese: float) -> dict:
        """
        returns
        =======
        dict : a dictionary with the lower and upper boundaries of a
        confidence interval

        params
        ======
        x : float
            the sample parameter, either the sample mean, proportion,
            or difference between two proportions
        q : float
            either z-stat or t-stat
        ese : float
            estimated standard error of the mean
        """

        a_dict: dict = dict()
        a_dict["lower"] = round(x - q*ese, 6)
        a_dict["upper"] = round(x + q*ese, 6)
        return a_dict

    @staticmethod
    def get_z(a: float) -> float:
        """
        returns
        =======
        float : (1-a/2)-quantile of the standard normal, rounded to 4dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        """
        return round(norm().ppf(1-a/2), 4)

    @staticmethod
    def get_t(a: float, df: int) -> float:
        """
        returns
        =======
        float : (1-a)- or (1-a/2)-quantile of the t(df) distribution,
        rounded to 4dp

        params
        ======
        a : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        df : int
            degrees of freedom of t
        mean : float
            sample mean
        stderr : float
            standard error of the mean
        """
        return round(t(df).ppf(1-a/2), 4)

    @staticmethod
    def zinterval_mean(
            alpha: float,
            mean: float,
            size: int,
            var: float = 0,
            sd: float = 0) -> dict:
        """
        returns
        =======
        dict : (1-alpha)% z-interval for the mean, with limits rounded
        to 6dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        mean : float
            sample mean
        size : int
            sample size
        var : float, default is 0
            sample variance
        sd : float, default is 0
            sample standard deviation
        """
        # parse args
        if var == 0 and sd == 0:  # abort
            print("Cancelled: Please specify either var or std.")
        elif (var != 0 and sd == 0):  # convert var -> std
            sd = sqrt(var)

        # get parameters
        z: float = ConfidenceInterval.get_z(alpha)
        ese: float = sd/sqrt(size)

        return ConfidenceInterval.get_ci_as_dict(x=mean, q=z, ese=ese)

    @staticmethod
    def zinterval_prop(alpha: float, count: int, nobs: int) -> dict:
        """
        returns
        =======
        dict : (1-alpha)% z-interval for a proportion, with limits
        rounded to 6dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        count : int
            number of successes
        nobs : int
            number of observations
        """
        # get parameters
        p: float = count/nobs
        z: float = ConfidenceInterval.get_z(alpha)
        ese: float = sqrt(p*(1-p)/nobs)

        return ConfidenceInterval.get_ci_as_dict(x=p, q=z, ese=ese)

    @staticmethod
    def zinterval_diff_props(
            alpha: float,
            count1: int,
            nobs1: int,
            count2: int,
            nobs2: int) -> dict:
        """
        returns
        =======
        dict : (1-alpha)% z-interval for the difference between two
        proportions, with limits rounded to 6dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        count1 : int
            number of successes in sample 1
        nobs1 : int
            sample size of sample 1
        count2 : int
            number of successes in sample 2
        nobs2 : int
            sample size of sample 2
        """
        # get parameters
        p1: float = count1/nobs1
        p2: float = count2/nobs2
        d: float = p1-p2
        z: float = ConfidenceInterval.get_z(alpha)
        ese: float = sqrt(p1*(1-p1)/nobs1 + p2*(1-p2)/nobs2)

        return ConfidenceInterval.get_ci_as_dict(x=d, q=z, ese=ese)

    @staticmethod
    def zinterval_poisson(
            alpha: float,
            mean: float,
            size: int) -> dict:
        """
        returns
        =======
        dict : (1-alpha)% z-interval for the poisson parameter, with
        limits rounded to 6dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        mean : float
            sample mean
        size : int
            sample size
        """
        # get parameters
        z: float = ConfidenceInterval.get_z(alpha)
        ese: float = sqrt(mean/size)

        return ConfidenceInterval.get_ci_as_dict(x=mean, q=z, ese=ese)

    @staticmethod
    def tinterval_mean(
            alpha: float,
            mean: float,
            size: int,
            var: float = 0,
            sd: float = 0) -> dict:
        """
        returns
        =======
        dict : (1-alpha)% t-interval for the mean, with limits rounded
        to 6dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        mean : float
            sample mean
        size : int
            sample size
        var : float, default is 0
            sample variance
        sd : float, default is 0
            sample standard deviation
        """
        # parse args
        if var == 0 and sd == 0:  # abort
            print("Cancelled: Please specify either var or std.")
        elif (var != 0 and sd == 0):  # convert var -> std
            sd = sqrt(var)

        # get parameters
        df: int = size - 1
        ese: float = sd/sqrt(size)
        t: float = ConfidenceInterval.get_t(alpha, df)

        return ConfidenceInterval.get_ci_as_dict(x=mean, q=t, ese=ese)

    @staticmethod
    def tinterval_diff_means(
            alpha: float,
            d: float,
            size1: int,
            size2: int,
            sd1: float,
            sd2: float) -> dict:
        """
        returns
        =======
        dict : (1-alpha)% t-interval for the difference between two
        normal means, with limits rounded to 6dp

        params
        ======
        alpha : float
            float in (0,1), significance level of the ci to return, as
            in (1-alpha)%
        d : float
            difference between the sample means, expected mean1-mean2
        size1 : int
            size of sample 1
        size2 : int
            size of sample 2
        sd1 : float
            standard deviation of sample 1
        sd2 : float
            standard deviation of sample 2
        """
        # get parameters
        df: int = size1 + size2 - 2
        pooled_var: float = ((size1-1)*(sd1**2) + (size2-1)*(sd2**2)) / df
        ese: float = sqrt(pooled_var) * sqrt(1/size1 + 1/size2)
        t: float = ConfidenceInterval.get_t(alpha, df)

        return ConfidenceInterval.get_ci_as_dict(x=d, q=t, ese=ese)
