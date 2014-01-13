#This class is supposed to encapsulate an instance of a file.
#
#It should contain methods to manipulate File Information
#and also retrieve file information.
#
#It is mean't to be a helper class to the Database Class
#when storing information.

import os

class File:
    def __init__(self, item):           #constructor takes a file's full directory address
        self._name = self.getName(item)
        self._path = self.getPath(item)
        self._size = self.getSize(item)
        self._datec = self.getDatec(item)
        self._datem = self.getDatem(item)
        self._extension = self.getExtension(item)

    def getDetails(self):   #returns tuple containing all relevant information about the file
        return (None, self._name, self._path, self._size, self._datec, self._datem, self._extension)

    #The get functions help get the corresponding properties,
    # e.g getName() returns the name of the File.
    def getName(self, item):
        return os.path.basename(item)

    def getPath(self, item):
        return os.path.split(item)[0]

    def getSize(self, item):
        return os.path.getsize(item)

    def getDatec(self, item):
        date = os.path.getctime(item)
        return str(date)

    def getDatem(self, item):
        date = os.path.getmtime(item)
        return str(date)        

    def getExtension(self, item):
        return os.path.splitext(item)[1]
