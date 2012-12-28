class File:
    def __init__(self, item):
        self._name = getName(item)
        self._path = getPath(item)
        self._size = getSize(item)
        self._datec = getDatec(item)
        self._datem = getDatem(item)
        self._extension = getExtension(item)

    def getDetails(self):
        return (self._name, self._path, self._size, self._datec, self._datem, self._extension)

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
