
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

    def load_glass_fibres() -> pd.DataFrame:
        """
        Returns the data in glass_fibres.csv as a pandas DataFrame.
        """

        return Data.load("glass-fibres")

    def load_accidents() -> pd.DataFrame:
        """
        Returns the data in accidents.csv as a pandas DataFrame.
        """

        return Data.load("accidents")

    def load_snoring() -> pd.DataFrame:
        """
        Returns the data in snoring.csv as a pandas DataFrame.
        """

        return Data.load("snoring")

    def load_skulls() -> pd.DataFrame:
        """
        Returns the data in skulls.csv as a pandas DataFrame.
        """

        return Data.load("skulls")

    def load_sewer() -> pd.DataFrame:
        """
        Returns the data in sewer.csv as a pandas DataFrame.
        """

        return Data.load("sewer")

    def load_schoolgirls() -> pd.DataFrame:
        """
        Returns the data in schoolgirls.csv as a pandas DataFrame.
        """

        return Data.load("schoolgirls")

    def load_practical_test() -> pd.DataFrame:
        """
        Returns the data in practical-test.csv as a pandas DataFrame.
        """

        return Data.load("practical-test")

    def load_darwin() -> pd.DataFrame:
        """
        Returns the data in darwin.csv as a pandas DataFrame.
        """

        return Data.load("darwin")

    def load_movements() -> pd.DataFrame:
        """
        Returns the data in movements.csv as a pandas DataFrame.
        """

        return Data.load("movements")

    def load_lesions() -> pd.DataFrame:
        """
        Returns the data in lesions.csv as a pandas DataFrame.
        """

        return Data.load("lesions")

    def load_dopamine() -> pd.DataFrame:
        """
        Returns the data in dopamine.csv as a pandas DataFrame.
        """

        return Data.load("dopamine")

    def load_osa() -> pd.DataFrame:
        """
        Returns the data in osa.csv as a pandas DataFrame.
        """

        return Data.load("osa")
