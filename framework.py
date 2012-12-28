#################################
#This is intended to be the file#
#management for my tent project #
#Pretty Cool round              #
#################################

import os
import time
from sqlite3 import *
import file

FOLDERS = []

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

class Framework: #baseclass for my files system
    def __init__(self, databaseName=DATABASE_NAME):
        self._databaseIsOpen = None
        openDatabase(databaseName)
        cursor = getCursor()
        cursor.execute(CREATE_COMMAND % HEADERS)

        scanDirectory()
        
        closeDatabase()

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
    
    def transform(cudir, lst):
        for i in range(len(lst)):
            lst[i] = cudir+'\\'+lst[i]

    def appendStack(stack, lst):
        for i in lst:
            stack.append(i)

    def processFile(file, databaseName):
        openDatabase(databaseName)
        INSERT_COMMAND = "insert into %s(%s, %s, %s, %s, %s, %s) values(?, ?, ?, ?, ?, ?)" %(); #continue from here tommorow

        fileDetails = File(file).getDetails()

        closeDatabase()

    def scanDirectory(directory = 'C:\\', databaseName=DATABASE_NAME):
        os.chdir(directory)
        filestack = os.listdir();
        
        curdir = os.getcwd()
        transform(curdir, filestack)
    
        while len(filestack) != 0:
            curItem = filestack.pop()
        
            if os.path.isfile(curItem):
                try:
                    processFile(curItem, databaseName)
                except UnicodeEncodeError:
                    print(curItem)
                    continue
            elif os.path.isdir(curItem):
                try:
                    tmpStack = os.listdir(curItem)
                except WindowsError:
                    continue
            
                transform(curItem, tmpStack)
                appendStack(filestack, tmpStack)
            
                FOLDERS.append(curItem)
           

