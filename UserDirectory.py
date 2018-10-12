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
		try:
			with open(fileName,'a+') as filePtr:
				filePtr.write('START')
				filePtr.write(user.toString())
				filePtr.write('END')
    	except IOError:
			print 'Unable to add user to file'

    def deleteUser(self,user):
        pass #TODO
    
	""" Returns a list of all Users """
    def getUsers(self,user):
    	try:
			with open(self.fileName,'r') as filePtr:
				lines = filePtr.readlines()
				for line in lines.split():
					#write code to read in b/t start
    
    
class DBStorage(object):
    
    def __init__(self,_host,_port):
        fileName = _fileName
    
    def addUser(self, user):
        pass #TODO
    
    def deleteUser(self,user):
        pass #TODO
    
    def listUsers(self,user):
        pass #TODO
    
    
