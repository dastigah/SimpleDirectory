import argparse

import User			#TODO
import FileStorage	#TODO
import DBStorage	#TODO



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
    
	exclusiveGroup = parser.add_mutually_exclusive_group()
	exclusiveGroup.add_argument('-c','--create',help='Create a new user in the directory')
	exclusiveGroup.add_argument('-l','--list',action='store_true',help='List all users in directory')
	exclusiveGroup.add_argument('-d','--delete',help='Delete user in directory')
    
    parser.add_argument('-f','--file',help='Use a local file instead of database')
	# Possibly need to include an option to choose DB connection string
    
	parser.parse_args()

	""" Decide on the storage type to use File vs Databse """
	if parser.file:
		userDirectory = FileStorage(parser.file)
	else:
		userDirectory = DBStorage(hostName,portNumber,isCredsReq)

	""" Options """
	if exclusiveGroup.create:
		addUser(userDirectory,currentUser)		#TODO
	elif exclusiveGroup.list:
		listUsers(userDirectory)				#TODO
	else:
		deleteUser(userDirectory,currentUser)	#TODO
