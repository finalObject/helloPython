class FileError(IOError):
    def __init__(self,info):
        Exception.__init__(self)
        self.errorInfo = info
    def __str__(self):
        return "FileError:%s" % self.errorInfo
try:
    raise FileError("FF")
except FileError as e:
    print(e) 