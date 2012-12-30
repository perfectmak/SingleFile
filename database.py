from sqlite3 import *

class Singleton:
    __sharedState = {}
    def __init__(self):
        self.__dict__ = self.__sharedState


class Database(Singleton):
    DATABASE_NAME = 'FILE_DB'
    TABLE_NAME = 'file_table'
    CREATE_COMMAND = "create table %s (\
                    %s int primary key auto_increment,\
                    %s text\
                    %s text\
                    %s int\
                    %s varchar(25)\
                    %s varchar(25)\
                    %s varchar(4)"
    ID_KEY = "id"
    NAME_KEY = "name"
    PATH_KEY = "path"
    SIZE_KEY = "size"
    DATEC_KEY = "date_created"
    DATEM_KEY = "date_modified"
    EXTENSION_KEY = "extension"

    HEADERS = (TABLE_NAME, ID_KEY, NAME_KEY, PATH_KEY, SIZE_KEY, DATEC_KEY, DATEM_KEY, EXTENSION_KEY)

    def __init__(self, databaseName=DATABASE_NAME):
        Singleton.__init__(self)
        self._databaseIsOpen = None
        self.__dbName = databaseName

    def openDatabase(self, databaseName):
        if not self._databaseIsOpen: #self.databaseIsOpen is okay, cos i intend to work with the same database through out the program
            self._conn = connect(databaseName)
            self._cursor = conn._cursor()
            self._databaseIsOpen = True

    def closeDatabase(self):
        if self._databaseIsOpen:
            self._cursor.close()
            self._databaseIsOpen = False

    def getCursor(self):
        if self._databaseIsOpen:
            return self._cursor
    
    def getConnection(self):
        if _self._databaseIsOpen:
            return self._conn

    def insert(self, command, Tuple): #for insert command into the database
        
