#################################
#This is intended to be the file#
#management for my tent project #
#Pretty Cool round              #
#################################

#The Framework class is designed to be the core of the File System Program.
#It contains methods that will be used directly by the application i.e it class
#that interacts directly with all other classes.

import os
import time

from file import *
from database import *

FOLDERS = []
log = 'temp.log'


class Framework: 
    def __init__(self): 
        self.db = Database(); #creates a database instance for the Framework

        if not self.upToDate(): #checks to see if this is the first time of running 
            self.scanDirectory('/')  #the program. 
            self.update();   

    def __del__(self): #destructor helps to close open resources.
        if self.__isOpen: # closes log file if open.
            self.__temp.close();

    def update(self):   #Updates the log file
        self.__temp = open(log, 'w')
        self.__temp.write('Up To Date: True');
        self.__temp.close();

    def upToDate(self): #checks if the database is up to date.
        self.__temp = open(log, 'r')
        self.__isOpen = True;

        line = self.__temp.readline();
        if line[12:] == 'True':
            return True
        else:
            return False
   
    def transform(self, cudir, lst): #helper method to scanDirectory()
        for i in range(len(lst)):
            lst[i] = cudir+'\\'+lst[i]

    def appendStack(self, stack, lst):  #helper method to scanDirectory()
        for i in lst:
            stack.append(i)

    def processFile(self, file):    #helper method to scanDirectory()
        
        fileHandle = File(file);
        print("Processing...", fileHandle.getName(file))
        fileDetails = fileHandle.getDetails()

        self.db.insert(fileDetails)

    def scanDirectory(self, directory, process = None): #scans the given directory and stores it in the database.
        if process == None: #replace process with a function to process each file
            process = self.processFile;

        filestack = os.listdir(directory);
        curdir = directory;
        self.transform(curdir, filestack)
        
        while len(filestack) != 0:
            curItem = filestack.pop()
        
            if os.path.isfile(curItem):
                try:
                    process(curItem)
                except UnicodeEncodeError:
                    print(curItem)
                    continue
            elif os.path.isdir(curItem):
                try:
                    tmpStack = os.listdir(curItem)
                except WindowsError:
                    continue
            
                self.transform(curItem, tmpStack)
                self.appendStack(filestack, tmpStack)
            
                FOLDERS.append(curItem)

    def showAll(self):      #supposed to show all files in the database.
        query = "select %s, count(%s) as noOfDuplicates from %s group by %s having (count(%s)>1)" %(NAME_KEY, NAME_KEY, TABLE_NAME, NAME_KEY, NAME_KEY);
        self.db.select(select = query);
        # print("Showing all");
        cur = self.db.getCursor();

        for col in cur:
            print(['-' for i in range(15)])
            print("File: ", col[0]);
            print("Occurence: ", col[1]);
     
            
            

