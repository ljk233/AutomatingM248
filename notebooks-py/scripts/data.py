
import pandas as pd


class Data():
    """
    A class of static methods that returns a specific CSV data file in
    "/data/" as a pandas DataFrame.
    """

    PATH: str = "../data/"

    def load(a_csv: str) -> pd.DataFrame:
        """
        Returns arg a_csv as a pandas DataFrame. There is no need to
        state the file type.
        """

        return pd.read_csv(Data.PATH + a_csv + ".csv")

    def load_tattoos() -> pd.DataFrame:
        """
        Returns the data in tattoos.csv as a pandas DataFrame.
        """

        return Data.load("tattoos")

    def load_workforce() -> pd.DataFrame:
        """
        Returns the data in workforce.csv as a pandas DataFrame.
        """

        return Data.load("workforce")

    def load_membership() -> pd.DataFrame:
        """
        Returns the data in membership.csv as a pandas DataFrame.
        """

        return Data.load("membership")

    def load_response_inhibition() -> pd.DataFrame:
        """
        Returns the data in response-inhibition.csv as a pandas
        DataFrame.
        """

        return Data.load("response-inhibition")

    def load_distance() -> pd.DataFrame:
        """
        Returns the data in distance.csv as a pandas DataFrame.
        """

        return Data.load("distance")

    def load_coal() -> pd.DataFrame:
        """
        Returns the data in coal.csv as a pandas DataFrame.
        """

        return Data.load("coal")

    def load_plasma() -> pd.DataFrame:
        """
        Returns the data in plasma.csv as a pandas DataFrame.
        """

        return Data.load("plasma")

    def load_goals() -> pd.DataFrame:
        """
        Returns the data in goals.csv as a pandas DataFrame.
        """

        return Data.load("goals")
