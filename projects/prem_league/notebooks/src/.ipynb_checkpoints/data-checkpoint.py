
import pandas as pd


class Data():
    """
    A class of static methods to help load the data sets.
    """

    PATH_IN: str = "../data/in/"
    PATH_OUT: str = "../data/out/"
    
    def load_in(a_csv: str) -> pd.DataFrame:
        """
        Returns a csv file as a pd DataFrame.
        There is no need to append ".csv".
        """

        return pd.read_csv(Data.PATH_IN + a_csv + ".csv")
  
    def load_out(a_csv: str) -> pd.DataFrame:
        """
        Returns a csv file as a pd DataFrame.
        There is no need to append ".csv".
        """

        return pd.read_csv(Data.PATH_OUT + a_csv + ".csv")

    def load_epl_1819() -> pd.DataFrame:
        """
        Returns epl_1819.csv as a pd DataFrame
        """

        return Data.load_in("epl_1819")

    def load_epl_1819_game_id() -> pd.DataFrame:
        """
        Returns epl_1819.csv as a pd DataFrame
        """

        return Data.load_out("epl_1819_game_id")

    def load_goal_times() -> pd.DataFrame:
        """
        Returns goal_times.csv as a pd DataFrame
        """

        return Data.load_out("goal_times")
    