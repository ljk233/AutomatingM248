import sqlite3
from sqlite3 import Error
import pandas as pd


class Database():
    """
    Creates a connection to an sqlite3 database.
    """

    def __init__(self, db: str) -> None:
        '''
        add docstring
        '''

        # initiate paramters
        self.db: str = "./data/" + db + ".db3"

        self.createConnection()

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

    def __init__(self, tbl: str, db: object) -> None:

        self.db = db
        self.tbl = tbl
        self.setCursorFetchAll()
        self.setData()
        self.setTitles()
        self.setDF()

    def setCursorFetchAll(self) -> None:
        self.cur = self.db.conn.cursor()  # creates the cursor object
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

    def setDF(self) -> None:
        '''
        Creates the DataFrame object
        '''

        self.dataframe = pd.DataFrame(self.data, columns=self.titles)

    def toDF(self) -> object:
        '''
        Returns the dataframe attribute
        '''

        return self.dataframe

