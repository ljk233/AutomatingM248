import sqlite3
from sqlite3 import Error
import pandas as pd


class Database():
    """
    Creates a connection to an sqlite3 data, and executes a SELECT * FROM tbl
    query.
    """

    def __init__(self, db: str, tbl: str) -> None:
        '''
        add docstring
        '''

        # initiate paramters
        self.db: str = "./data/" + db + ".db3"
        self.tbl: str = tbl

        self.createConnection()
        self.setCursor()
        self.setData()
        self.setTitles()

        self.dataframe = pd.DataFrame(self.data, columns=self.titles)

    def createConnection(self) -> None:
        """
        Create a database connection to the SQLite database
        specified by the db_file

        :param db_file: database file
        :return: Connection object or None
        """

        self.conn = None

        try:
            self.conn = sqlite3.connect(self.db)
        except Error as e:
            print(e)

    def table(self, table: str) -> object:
        '''
        Creates a cursor object for db.tbl
        '''

        self.setData()
        self.setTitles()

    def setCursor(self) -> None:
        self.cur = self.conn.cursor()  # creates the cursor object
        str_query: str = "SELECT * FROM " + self.tbl  # query to exe
        self.cur.execute(str_query)  # executes the query

    def setTitles(self) -> None:
        '''
        sets the column title
        '''

        self.titles: list = list()

        for column in self.cur.description:
            self.titles.append(column[0])

    def setData(self) -> None:
        '''
        sets the data
        '''

        self.data = self.cur.fetchall()

    def getDF(self) -> object:
        '''
        Returns the dataframe attribute
        '''

        return self.dataframe
