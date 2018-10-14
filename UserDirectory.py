"""
FileStorage will store users within a text file with the format given below:

FORMAT:
    {NAME}
    {PHONE}
    {ADRESS}
"""
class FileStorage(object):
    def __init__(self, _fileName):
            self.fileName = _fileName

    def addUser(self, user):
        try:
            with open(self.fileName,'a+') as filePtr:
                filePtr.write(user.toString())
                filePtr.write('\n\n')
        except IOError:
            print 'Unable to add user to file'

    def deleteUser(self,user):
        pass #TODO

    """ Returns a list of all Users """
    def getUsers(self,user):
        try:
            with open(self.fileName,'r') as filePtr:
                lines = filePtr.readlines()
                #for line in lines.split():
                    #write code to read in b/t start
        except IOError:
            print 'Unable to get users'

class DBStorage(object): 
    pass

    def __init__(self,_host,_port):
        self.host = _host
        self.port = _port

    def addUser(self, user):
        pass #TODO

    def deleteUser(self,user):
        pass #TODO

    def listUsers(self,user):
        pass #TODO
