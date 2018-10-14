
class User(object):
    
    def __init__ (self,rawText):
        userParams = rawText.split(';')
        self.name = userParams[0]
        self.phone = userParams[1]
        
        if len(userParams) == 3:
            self.address = Address(userParams[2])
        else:
            self.address = None
            
    def toStringArray(self):
		return 	[self.name, self.phone] + self.address.toStringArray() \
                if self.address else [self.name, self.phone]
    
    def toString(self):
        return self.name + '\n' + self.phone + '\n' + self.address.toString()


""" User actions """        
def addUser(userDirectory,currentUser):
    userDirectory.addUser(currentUser)

def deleteUser(userDirectory, currentUser):
    userDirectory.deleteUser(currentUser)

def listUsers(userDirectory):
    userDirectory.listUsers()
    
    
class Address(object):
        
    def __init__(self,rawText):
        addressParams  = rawText.split(',')
        self.street = addressParams[0]
        self.city = addressParams[1]
        self.state = addressParams[2]
        
    def toStringArray(self):
        return [self.street,self.city,self.state]
    
    def toString(self):
        return self.street + '\n' \
                + self.city + "," + self.state
