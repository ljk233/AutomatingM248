
from __future__ import annotations
from scipy.stats import linregress, probplot, t
import seaborn as sns
import matplotlib.pyplot as plt


class LinearRegression():
    """
    A convenience class for scipy.stats.lingress.
    """

    # static vars

    def __init__(self, x, y) -> None:
        """
        Constructor for objects of type LinearRegression.

        @param  x, array-like object of the independent data

        @param  y, array-like object of the dependent data
        """

        self._x = x
        self._y = y

    # @properties
    @property
    def slope(self) -> float:
        """
        Returns the model's slope coefficient.
        """
        return self._model.slope

    @property
    def intercept(self) -> float:
        """
        Returns the model's intercept constant.
        """
        return self._model.intercept

    @property
    def str_slope(self) -> str:
        """
        Returns the model's slope coefficient as a formatted string.
        """
        return f"{self.slope:.6f}"

    @property
    def str_intercept(self) -> str:
        """
        Returns the model's intercept constant.
        """
        return f"{self.intercept:.6f}"

    @property
    def predicted_values(self):
        """
        Returns the fitted values of the model.
        """
        return self.intercept + self.slope*self._x

    @property
    def residuals(self):
        """
        Returns the residuals of the model.
        """
        return self._y - self.predicted_values

    @property
    def p_val(self):
        """
        Returns the p_value for beta
        """
        return self._model.pvalue

    @property
    def str_p_val(self):
        """
        Returns the p_value for beta
        """
        return f"{self.p_val:.6f}"

    @property
    def stderr(self):
        """
        Returns the standard error of beta.
        """
        return self._model.stderr

    # instance methods

    def fit(self):
        """
        Models the relationship between the dependent and independent
        variables.
        """

        self._model = linregress(self._x, self._y)

    def report(self):
        """
        Generates a report of the model.
        """
        # coefficients
        print(
            "Regression equation"
            + "\n===================\n"
            + f"{{slope={self.str_slope}, intercept={self.str_intercept}}}"
            + "\n")

        # model
        self.plt_model()

        # ci beta, hypothesis test beta=0
        print(
            "\n" + "Hypothesis test of beta=0"
            + "\n" + "========================="
            + "\n" + f"p-value={self.str_p_val}"
            + f", 95%_CI={self.print_beta_confint()}")

        # plot residuals, prob plot, model
        print(
            "\n" + "Other graphs"
            + "\n" + "============")

        self.plt_residuals()
        self.plt_prob_plot()

    def interpret_p_val(self):
        """
        Returns an interpretation of the p-value for the hypotheis test
        of beta=0, based on the table in the handbook.
        """

        tail = " evidence against H_0)"

        if self.p_val <= 0.01:
            head = "(Strong"
        elif self.p_val <= 0.05:
            head = "(Moderate"
        elif self.p_val <= 0.1:
            head = "(Weak"
        else:
            head = "(Little to no"

        return head + tail

    def print_beta_confint(self):
        """
        Returns a 95% CI for beta as a formatted string.
        """

        ts = abs(t.ppf(self.p_val/2, self._x.size))

        lower = self.slope - ts*self.stderr
        upper = self.slope + ts*self.stderr

        return f"({lower:.6f}, {upper:.6f})"

    def plt_model(self):
        """
        """
        ax = sns.scatterplot(x=self._x, y=self._y, label='original data')
        sns.lineplot(
            x=self._x, y=self.predicted_values, color="r", label='fitted line')
        ax.set(title="Original data and fitted line")
        plt.show()

    def plt_residuals(self):
        """
        """
        ax1 = sns.scatterplot(
            x=self.predicted_values, y=self.residuals)
        ax1.set(
            xlabel="Fitted value", ylabel="Residual", title="Residual plot")
        plt.axhline(y=0, color="r", linestyle="-.")
        plt.show()

    def plt_prob_plot(self):
        """
        """
        ax = plt.subplot()
        probplot(x=self.residuals, plot=ax)
        ax.set(title="Probability plot of residuals")
        plt.show()
