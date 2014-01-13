#This module is no where near functional yet. I'm in a dillema of
#wether to implement the file system watcher with IronPython or PyQt.
#So if you have a better solution, you are free to try it out.

#This is supposed to help watch the file system for changes
#and notify the database to include such changes.

#This code is written in PyQt and it is only a template, not tested yet.

from PyQt4 import QtCore
app = QtGui.QApplication(sys.argv)

@QtCore.pyqtSlot(str)
def directory_changed(path):
    print('Directory changed!!!')

@QtCore.pyqtSlot(str)
def file_changed(path):
    print('File Changed!!!')

#Be sure to change 'path/to/file_..' to the correct file path.
fs_watcher = QtCore.QFileSystemWatcher(['path/to/files_1','path/to/file_2', 'path/to/file_3'])

fs_watcher.connect(fs_watcher, QtCore.SIGNAL('directoryChanged(QString)'), directory_changed)

fs_watcher.connect(fs_watcher, QtCore.SIGNAL('fileChanged(QString)'), file_changed)

app.exec_()
