
import pandas as pd


class Load():
    """
    A class of static methods to help load the data sets.
    """

    PATH_IN: str = "../data/"

    def dataframe(a_csv: str) -> pd.DataFrame:
        """
        Returns a csv file as a pd DataFrame.
        There is no need to append ".csv".
        """

        return pd.read_csv(Load.PATH_IN + a_csv + ".csv")

    def practical_tests() -> pd.DataFrame:
        """
        Returns epl_1819.csv as a pd DataFrame
        """

        return Load.dataframe("practical-tests")

    def total_goals_scored() -> pd.DataFrame:
        """
        Returns ft_goals_17_18.csv as a pd DataFrame
        """

        return Load.dataframe("ft_goals_17_18")

    def epl_goals() -> pd.DataFrame:
        """
        Returns epl_goals.csv as a pd DataFrame
        """

        return Load.dataframe("epl_goals")

    def attendance() -> pd.DataFrame:
        """
        Returns attendance.csv as a pd DataFrame
        """

        return Load.dataframe("attendance")

    def basketball() -> pd.DataFrame:
        """
        Returns basketball.csv as a pd DataFrame
        """

        return Load.dataframe("basketball")

    def laurel_and_hardy() -> pd.DataFrame:
        """
        Returns laurel-and-hardy.csv as a pd DataFrame
        """

        return Load.dataframe("laurel-and-hardy")

    def summer_rentals() -> pd.DataFrame:
        """
        Returns summer_rentals.csv as a pd DataFrame
        """

        return Load.dataframe("summer_rentals")

    def tattoos() -> pd.DataFrame:
        """
        Returns tattoos.csv as a pd DataFrame
        """

        return Load.dataframe("tattoos")

    def sleep_gain() -> pd.DataFrame:
        """
        Returns sleep-gain.csv as a pd DataFrame
        """

        return Load.dataframe("sleep-gain")

    def coins() -> pd.DataFrame:
        """
        Returns coins.csv as a pd DataFrame
        """

        return Load.dataframe("coins")
