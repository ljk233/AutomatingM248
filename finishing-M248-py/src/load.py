
import pandas as pd


PATH: str = "../data/"


def _load(a_csv: str) -> pd.DataFrame:
    """
    Returns arg a_csv as a pandas DataFrame. There is no need to
    state the file type.
    """

    return pd.read_csv(Data.PATH + a_csv + ".csv")


def plasma() -> pd.DataFrame:
    """
    Returns the data in plasma.csv as a pandas DataFrame.
    """

    return _load("plasma")


def glass_fibres() -> pd.DataFrame:
    """
    Returns the data in glass_fibres.csv as a pandas DataFrame.
    """

    return _load("glass-fibres")


def accidents() -> pd.DataFrame:
    """
    Returns the data in accidents.csv as a pandas DataFrame.
    """

    return _load("accidents")


def sewer() -> pd.DataFrame:
    """
    Returns the data in sewer.csv as a pandas DataFrame.
    """

    return _load("sewer")


def schoolgirls() -> pd.DataFrame:
    """
    Returns the data in schoolgirls.csv as a pandas DataFrame.
    """

    return _load("schoolgirls")


def skulls() -> pd.DataFrame:
    """
    Returns the data in skulls.csv as a pandas DataFrame.
    """

    return _load("skulls")


def practical_test() -> pd.DataFrame:
    """
    Returns the data in practical-test.csv as a pandas DataFrame.
    """

    return _load("practical-test")


def darwin() -> pd.DataFrame:
    """
    Returns the data in darwin.csv as a pandas DataFrame.
    """

    return _load("darwin")


def movements() -> pd.DataFrame:
    """
    Returns the data in movements.csv as a pandas DataFrame.
    """

    return _load("movements")


def lesions() -> pd.DataFrame:
    """
    Returns the data in lesions.csv as a pandas DataFrame.
    """

    return _load("lesions")


def dopamine() -> pd.DataFrame:
    """
    Returns the data in dopamine.csv as a pandas DataFrame.
    """

    return _load("dopamine")


def coal() -> pd.DataFrame:
    """
    Returns the data in coal.csv as a pandas DataFrame.
    """

    return _load("coal")


def osa() -> pd.DataFrame:
    """
    Returns the data in osa.csv as a pandas DataFrame.
    """

    return _load("osa")


def uniform_goals() -> pd.DataFrame:
    """
    Returns the data in uniform_goals.csv as a pandas DataFrame.
    """

    return _load("uniform_goals")


def cholesterol() -> pd.DataFrame:
    """
    Returns the data in cholesterol.csv as a pandas DataFrame.
    """

    return _load("cholesterol")


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

    def load_goals() -> pd.DataFrame:
        """
        Returns the data in goals.csv as a pandas DataFrame.
        """

        return Data.load("goals")

    def load_snoring() -> pd.DataFrame:
        """
        Returns the data in snoring.csv as a pandas DataFrame.
        """

        return Data.load("snoring")
