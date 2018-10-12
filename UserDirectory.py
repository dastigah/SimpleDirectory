"""
FileStorage will store users within a text file with the format given below:

FORMAT:
    START
    {NAME}
    {PHONE}
    {ADRESS}
    END
"""
class FileStorage(object):
    
    def __init__(self,_fileName):
        fileName = _fileName
    
    def addUser(self, user):
        pass #TODO
    
    def deleteUser(self,user):
        pass #TODO
    
    def listUsers(self,user):
        pass #TODO
    
    
    
class DBStorage(object):
    
    def __init__(self,_host,_port):
        fileName = _fileName
    
    def addUser(self, user):
        pass #TODO
    
    def deleteUser(self,user):
        pass #TODO
    
    def listUsers(self,user):
        pass #TODO
    
    