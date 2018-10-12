
class User(Object):
    
    
    def __init__(self,_name,_phone,_address):
        self.name = _name
        self.phone = _phone
        self.address = _address
        
	def toString(self):
		return 	self.name + '\n' \
				self.phone + '\n' \
				self.address 
