from scipy.stats import norm, t
from math import sqrt
import numpy as np


class TwoSmallNormalSamples():
    """Class for modelling the difference between two small
    sample normal distributions"""

    def __init__(self) -> None:
        """Constructor for objects of type t_test"""
        pass

    def do_samples_have_common_variance(self):
        """Tests to see if the two samples have a common variance.
        Returns True if they do, otherwise return False"""
        return self.has_s1_var() / self.has_s2_var() < 3

    def generate_samples(self, mean: float, var: float,
                         n1: int, n2: int) -> None:
        """Generates two samples of size n1, n2 fro N(mean, var).
        Sets them to s1, s2 respectively."""
        self.__s1 = norm.rvs(mean, sqrt(var), n1)
        self.__s2 = norm.rvs(mean, sqrt(var), n2)
        self.__set_s_comb()

    def has_s1(self):
        """Returns sample 1 as an np.array"""
        return self.__s1

    def has_s2(self):
        """Returns sample 1 as an np.array"""
        return self.__s2

    def has_s_comb(self):
        """Returns combined sample s_comb as an np.array"""
        return self.__s_comb

    def has_s1_size(self):
        return len(self.has_s1())

    def has_s2_size(self):
        return len(self.has_s2())

    def has_s1_mean(self):
        """Returns the sample mean of s1"""
        return self.has_s1().mean()

    def has_s2_mean(self):
        """Returns the sample mean of s1"""
        return self.has_s2().mean()

    def has_s1_var(self):
        """Returns the sample variance of s1"""
        return self.has_s1().var(ddof=1)

    def has_s2_var(self):
        """Returns the sample variance of s2"""
        return self.has_s2().var(ddof=1)

    def has_sample_mean_dfference(self):
        """Returns the difference between the two sample means"""
        return self.has_s1_mean() - self.has_s2_mean()

    def has_degrees_of_freedom(self):
        """Returns the degrees of freedom for a two sample t-interval"""
        return self.has_s1_size() + self.has_s2_size() - 2

    def has_sample_pooled_var(self):
        """Returns the pooled sample variance"""
        return ((self.__has_s1_weighted_var() + self.__has_s2_weighted_var()) /
                self.has_degrees_of_freedom())

    def has_sample_pooled_std(self):
        """Returns the pooled sample variance"""
        return sqrt(self.has_sample_pooled_var())

    def set_samples(self, a_sample1, a_sample2):
        """Set s1, s2 to a_sample1, a_sample2.
        Also concatenates the objects and sets to __s_comb"""
        self.set_s1(a_sample1)
        self.set_s2(a_sample2)
        self.__set_s_comb()

    def set_s1(self, a_sample):
        """Sets s1 to a_sample, some list-type object"""
        self.__s1 = a_sample

    def set_s2(self, a_sample):
        """Sets s2 to a_sample, some list-type object"""
        self.__s2 = a_sample

    def __set_s_comb(self):
        """Sets s_comb to concatenation of s1 and s2"""
        self.__s_comb = np.concatenate((self.has_s1(), self.has_s2()))

    def __has_s1_weighted_var(self):
        """Returns the weighted sample variance for s1"""
        return (self.has_s1_size() - 1) * self.has_s1_var()

    def __has_s2_weighted_var(self):
        """Returns the weighted sample variance for s2"""
        return (self.has_s2_size() - 1) * self.has_s2_var()

    def __has_reciprocal_sum_of_sizes(self):
        """Returns the reciprocal difference between the sizes.
        1/n1 + 1/n2"""
        return self.has_s1_size()**-1 + self.has_s2_size()**-1

    def has_interval(self, alpha):
        """Returns the alpha confidence interval for the difference between
        two small normal samples"""

        q = (1 + alpha)/2

        t_stat = t.ppf(q, self.has_degrees_of_freedom())

        d_plus = (self.has_sample_mean_dfference() +
                  (t_stat * self.has_sample_pooled_std() *
                  sqrt(self.__has_reciprocal_sum_of_sizes())))

        d_minus = (self.has_sample_mean_dfference() -
                   (t_stat * self.has_sample_pooled_std() *
                   sqrt(self.__has_reciprocal_sum_of_sizes())))

        return [d_minus, d_plus]
