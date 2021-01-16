
from scipy import stats


def get_y_mean(x_mean: float, a: float, b: float = 0) -> float:
    """
    Returns the mean E(X) of Y=aX+b, where X is some other rv.
    """
    return a * x_mean + b


def get_y_var(x_var: float, a: float) -> float:
    """
    Returns the variance V(Y) of Y=aX+b, where X is some other rv.
    """
    return a ** 2 * x_var


def get_z_from_x(x: float, mean: float, std: float) -> float:
    """
    Returns the value of the standard normal variable z, given a value for x
    with known mean and std for x.

    Return value is to 2dp (to support studies in M248)
    """
    return round((x-mean) / std, 2)


def get_x_from_a(a: float, mean: float, std: float) -> float:
    """
    Returns the value of a normal variable x with known mean and std for x,
    and the a-quantile value for standard normal variable z.

    Return value is to 2dp (to support studies in M248)
    """
    return round(std * a + mean, 3)


def get_mu_plus(mu: float, std: float, size: int, ci: float) -> float:
    """
    Calculates the upper value of a CI% confidence interval.
    """

    z = stats.norm()  # the standard normal distribution

    return mu + z.ppf(q=0.5 + ci/2) * std/size**(0.5)


def get_mu_minus(mu: float, std: float, size: int, ci: float) -> float:
    """
    Calculates the lower value of a CI% confidence interval.
    """

    z = stats.norm()  # the standard normal distribution

    return mu - z.ppf(q=0.5 + ci/2) * std/size**(0.5)


class Standard_Normal():
    """
    A class to support calculations involving the
    standard normal distribution, as outlined by M248.

    Dependencies: scipy.
    """

    """-----------------------------------------------------------------------
    Static methods
    -----------------------------------------------------------------------"""

    @staticmethod
    def has_phi(z: float, dp: int = 4, greater_than: bool = False) -> float:
        """
        Returns the probability Phi(z) of the standard normal
        distribution, rounded to arg dp.

        If greater_than is set to True, then return the
        probability 1-Phi(z).
        """
        if not greater_than:
            a_prob = stats.norm().cdf(x=z)
        else:
            a_prob = 1 - stats.norm().cdf(x=z)

        return round(a_prob, dp)

    @staticmethod
    def has_prob_range_phi(z1: float, z2: float, dp=4) -> float:
        """
        Returns the probability Phi(z1 < Z < z2) of the standard normal
        distribution, rounded to arg dp.
        """
        return round((Standard_Normal.has_phi(z=z2) -
                      Standard_Normal.has_phi(z=z1)),
                     dp)

    @staticmethod
    def has_quantile(a: float, dp: int = 4) -> float:
        """
        Returns the value of the alpha-quantile q_(alpha) of the
        standard normal distribution, rounded to arg dp.
        """
        return round(stats.norm().ppf(q=a), dp)


class Normal():
    """
    A class to support calculations involving the normal distribution,
    as outlined by M248.

    Dependencies: scipy.
    """

    __mu__: float  # the mean of the distribution
    __sigma__: float  # the standard deviation
    __dist__: object  # the normal distribution N(mu, sigma^2)
    __std_norm__: object  # the standard normal distribution N(0,1)
    __size__: int  # the sample size

    """-----------------------------------------------------------------------
    Constructor
    -----------------------------------------------------------------------"""

    def __init__(self,
                 a_mean: float,
                 a_std: float) -> None:
        """
        Constructor for objects of class Normal.
        """

        self.__mu__ = a_mean
        self.__sigma__ = a_std
        self.__dist__ = stats.norm(loc=a_mean, scale=a_std)

    """-----------------------------------------------------------------------
    Setter and Getter methods
    -----------------------------------------------------------------------"""

    def get_mu(self) -> float:
        """
        Returns the mean.
        """
        return self.__mu__

    def get_sigma(self) -> float:
        """
        Returns the standard deviation.
        """
        return self.__sigma__

    def get_dist(self) -> float:
        """
        Returns the normal distribution N(mu, sigma^2).
        """
        return self.__dist__

    def get_size(self) -> int:
        """
        Returns sample size.
        """
        return self.__size__

    def ret_var(self) -> float:
        """
        Returns the variance, an attribute of the distribution
        with no corresponding instance variable.
        """
        return self.get_sigma() ** 2

    """-----------------------------------------------------------------------
    Public methods
    -----------------------------------------------------------------------"""

    def has_z(self, x: float, dp: int = 2) -> float:
        """
        Returns the corresponding z-value of the standard
        normal distribution, rounded to dp.
        """
        return round((x - self.get_mu()) / self.get_sigma(), dp)

    def has_F(self,
              x: float,
              dp: int = 4,
              greater_than: bool = False) -> float:
        """
        Returns the probability F(x) of the normal distribution,
        N(mu, sigma^2), rounded to arg dp.

        If greater_than is set to True, then return the
        probability 1-F(x).
        """
        if not greater_than:
            a_prob = self.get_dist().cdf(x=x)
        else:
            a_prob = 1 - self.get_dist().cdf(x=x)

        return round(a_prob, dp)

    def has_prob_range_F(self, x1: float, x2: float, dp=4) -> float:
        """
        Returns the probability F(x1 < X < x2) of normal
        distribution, rounded to arg dp.
        """
        return round((self.has_F(x=x2) - self.has_F(x=x1)), dp)

    def has_quantile(self, a: float, dp: int = 4) -> float:
        """
        Returns the value of the alpha-quantile q_(alpha) of the
        normal distribution N(mu, sigma^2), rounded to arg dp.
        """
        return round(self.get_dist().ppf(q=a), dp)

    def is_distributed(self) -> None:
        """
        Prints the distribution of the variable, N(mu, sigma^2)
        """
        print(("Current model: N(" +
               str(self.get_mu()) +
               ", " +
               str(round(self.get_sigma(), 2)) +
               "^2)"))

    def model_sampling_distribution_of_total(self, n: int) -> object:
        """
        Updates the distribution to one for the sampling
        distribution of the total, T_n, where
        T_n = X_1 + X_2 + .... + X_n.

        Note
        - the distribution must be first be declared before
        the sample total can be modelled.
        - the original distribution is lost.
        """

        self.__size__ = n
        self.__mu__ = n * self.__mu__
        self.__sigma__ = (n ** 0.5) * self.__sigma__
        self.__dist__ = stats.norm(loc=self.__mu__, scale=self.__sigma__)

        return self

    def model_sample_distribution_of_mean(self, n: int) -> object:
        """
        Updates the distribution to one for the sampling
        distribution of the mean, X_bar.

        Note
        - the distribution must be first be declared before
        the sample mean can be modelled.
        - the original distribution is lost.
        """

        self.__size__ = n
        self.__sigma__ = self.get_sigma() / (n ** 0.5)
        self.__dist__ = stats.norm(loc=self.__mu__, scale=self.__sigma__)

        return self

    def has_ci(self, a: float) -> list:
        """
        Returns the 100(1-a)% CI.
        Arg a should be (0,1).
        """
        a_list: list = list()

        a_list.append(self.has_quantile(a/2 + 0.5))

        return a_list


class ConfidenceInterval():
    """
    A class to model confidence intervals, as outlined by M248.

    Dependenics: scipy.
    """

    # instance variables

    def __init__(self, mean: float, size: int, std: float) -> None:
        """
        Constructor for objects of class ConfidenceInterval.
        """

        self.mu = mean
        self.n = size
        self.sigma = std
        self.__std_norm__ = stats.norm()  # standard normal N(0,1)

    """-----------------------------------------------------------------------
    Getter methods
    -----------------------------------------------------------------------"""

    def get_mu(self) -> float:
        """
        Returns variable mu, the sample mean
        """
        return self.mu

    def get_n(self) -> int:
        """
        Returns variable n, the sample size
        """
        return self.n

    def get_sigma(self) -> float:
        """
        Returns variable n, the sample size
        """
        return self.sigma

    def ret_standard_error(self) -> float:
        """
        Returns the (estimated) standard error, an attribute that has no
        corresponding instance variable
        """
        return self.get_sigma / self.get_n ** 0.5

    """-----------------------------------------------------------------------
    Public methods
    -----------------------------------------------------------------------"""

    @staticmethod
    def ret_alpha(ci: float) -> float:
        """
        Returns the needed alpha-value for for the confidence interval.

        Arg ci should be a percentage.
        """
        return round(1 - (ci*1/100), 2)

    def ret_z(self, ci: int) -> float:
        """
        Returns z, the z-value for the confidence interval.

        Argument ci is the percentage confidence interval.
        """

        an_alpha: float = self.ret_alpha(ci=ci)

        return round(self.__std_norm__.ppf(q=(1-(0.5*an_alpha))), 3)
