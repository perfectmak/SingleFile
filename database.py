#Author: Makanju Perfect
#This module abstracts the workings of
#the Database.

from sqlite3 import *

#Singleton class should be inherited by class Intended to be singleton
class Singleton:    
    __sharedState = {}
    def __init__(self):
        self.__dict__ = self.__sharedState

#Information about fields and names related to the database.
DATABASE_NAME = 'FILE_DB'
TABLE_NAME = 'file_table'
CREATE_COMMAND = "create table if not exists %s (\
                    %s integer primary key,\
                    %s text,\
                    %s text,\
                    %s integer,\
                    %s varchar(25),\
                    %s varchar(25),\
                    %s varchar(4))"
ID_KEY = "id"
NAME_KEY = "name"
PATH_KEY = "path"
SIZE_KEY = "size"
DATEC_KEY = "date_created"
DATEM_KEY = "date_modified"
EXTENSION_KEY = "extension"

#Tuple containing table name and field names.
HEADERS = (TABLE_NAME, ID_KEY, NAME_KEY, PATH_KEY, SIZE_KEY, DATEC_KEY, DATEM_KEY, EXTENSION_KEY)


class Database(Singleton):

    __databaseIsOpen = None # Used to know if the database is open.
    
    def __init__(self, databaseName=DATABASE_NAME):
        Singleton.__init__(self) # needed to initiate singleton class.
        
        self.__dbName = databaseName
        self.__openDatabase(databaseName)

    def __del__(self): #destructor makes sure the database is closed.
        self.__closeDatabase()

    def __openDatabase(self, databaseName): #opens the database and creats tables if doesn't exist.
        if not self.__databaseIsOpen: #self.__databaseIsOpen is okay, cos i intend to work with the same database through out the program
            self.__conn = connect(databaseName)
            self.__cursor = self.__conn.cursor()
            self.__databaseIsOpen = True
            try:
                self.__cursor.execute(CREATE_COMMAND % HEADERS)
            except OperationalError:
                print(OperationalError)
                return 0;

    def __closeDatabase(self): #closes open database.
        if self.__databaseIsOpen:
            self.__cursor.close()
            self.__databaseIsOpen = False

    def getCursor(self): #returns cursor to the database for interation
        if self.__databaseIsOpen:
            return self.__cursor
    
    def getConnection(self): #returns the database connection instance
        if self.__databaseIsOpen:
            return self.__conn

    def insert(self, value): #for insert command into the database
        INSERT_COMMAND = "insert into %s(%s, %s, %s, %s, %s, %s, %s) values\
        (?, ?, ?, ?, ?, ?, ?)" %(TABLE_NAME, ID_KEY, NAME_KEY, PATH_KEY, SIZE_KEY, DATEC_KEY, DATEM_KEY, EXTENSION_KEY);
        
        self.__cursor.execute(INSERT_COMMAND, value);
        self.__conn.commit();

    def insertCols(self, select, cols): #helper function to select()
        chars = '%s';
        for i in range(len(cols) - 1):
            chars += ', %s'

        return (select[:8] + chars + select[8:])

    def insertWhere(self, select, where):  #helper function to select()
        count = 0;
        while where:
            item = where.popitem();
            if count == 0:
                temp = " where %s = %s" %(item[0], item[1])
                count += 1;
            else:
                temp += " and %s = %s" %(item[0], item[1])

        return select + temp

    def select(self, cols = None, where = None, select = ''): #works as a select statement for the database.
        if select != '':            #the select parameter should only be used to execute raw select querys.
            self.__cursor.execute(select)    
            return
        
        select = 'select () from %s' %TABLE_NAME;
        
        if cols == None and where == None:
            self.__cursor.execute("select * from %s" %TABLE_NAME);
            
        elif where == None:
            select = self.insertCols(select, cols) %cols
            self.__cursor.execute(select)

        elif cols == None:
            temp = "select * from %s" %TABLE_NAME
            select = self.insertWhere(temp, where);
            self.__cursor.execute(select);

        else:
            select = self.insertCols(select, cols) %cols
            select = self.insertWhere(select, where)

            self.__cursor.execute(select);
