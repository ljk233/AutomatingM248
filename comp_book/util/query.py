import sqlite3
from sqlite3 import Error
import pandas as pd


class Database():
    """
    Creates a connection to an sqlite3 database.
    """

    def __init__(self, db: str = './data/sets.db3') -> None:
        '''
        Constructor for the Database class.
        arg db is the relative path to the sqlite3 database.
        '''

        # initiate paramters
        self.db: str = db

        self.createConnection()

    def createConnection(self) -> None:
        """
        Create a database connection to the sqlite database.
        """

        self.conn = None

        try:
            self.conn = sqlite3.connect(self.db)
        except Error as e:
            print(e)

    def listTables(self) -> None:
        '''
        Lists all the tables in the target database
        '''

        cursor = self.conn.cursor()

        cursor.execute('SELECT name from sqlite_master where type= "table"')

        print("Table list")
        print("----------")

        for table in cursor.fetchall():
            tblName = table[0]
            print(tblName)


class Table():
    '''
    Retrieve a table of data from a database.
    '''

    def __init__(self, table: str, db: object) -> None:
        '''
        Constructor for the Table class.
        '''

        self.db = db
        self.tbl = table
        self.setCursorFetchAll()
        self.setData()
        self.setTitles()
        self.setDF()

    def setCursorFetchAll(self) -> None:
        '''
        Creates a default cursor object that retrieves all the data.
        '''

        self.cur = self.db.conn.cursor()  # creates the cursor object
        str_query: str = "SELECT * FROM " + self.tbl  # query to exe
        self.cur.execute(str_query)  # executes the query

    def setTitles(self) -> None:
        '''
        Sets the column title for the DataFrame.
        '''

        self.titles: list = list()

        for column in self.cur.description:
            self.titles.append(column[0])

    def setData(self) -> None:
        '''
        Sets the data for the DataFrame
        '''

        self.data = self.cur.fetchall()

    def setDF(self) -> None:
        '''
        Creates the DataFrame
        '''

        self.dataframe = pd.DataFrame(self.data, columns=self.titles)

    def toDF(self) -> object:
        '''
        Returns the DataFrame
        '''

        return self.dataframe