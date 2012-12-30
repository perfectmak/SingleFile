#################################
#This is intended to be the file#
#management for my tent project #
#Pretty Cool round              #
#################################

import os
import time

import file
import database

FOLDERS = []



class Framework: #baseclass for my files system
    def __init__(self, databaseName=DATABASE_NAME):
        self.db = Database();
        self.db.openDatabase()
        self.cursor = db.getCursor()
        self.cursor.execute(CREATE_COMMAND % HEADERS)

        scanDirectory()
        
        self.db.closeDatabase()
   
    def transform(cudir, lst):
        for i in range(len(lst)):
            lst[i] = cudir+'\\'+lst[i]

    def appendStack(stack, lst):
        for i in lst:
            stack.append(i)

    def processFile(file, databaseName):
        self.db.openDatabase()
        INSERT_COMMAND = "insert into %s(%s, %s, %s, %s, %s, %s) values(?, ?, ?, ?, ?, ?)" %(); #continue from here tommorow

        fileDetails = File(file).getDetails()

        self.db.closeDatabase()

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
           

