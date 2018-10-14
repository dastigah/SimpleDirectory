import argparse

from User import addUser,deleteUser,listUsers,User,Address			#TODO
from UserDirectory  import FileStorage, DBStorage #TODO



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    exclusiveGroup = parser.add_mutually_exclusive_group()
    exclusiveGroup.add_argument('-a','--add',help='Create a new user in the directory')
    exclusiveGroup.add_argument('-l','--list',action='store_true',help='List all users in directory')
    exclusiveGroup.add_argument('-d','--delete',help='Delete user in directory')

    parser.add_argument('-f','--file',help='Use a local file instead of database')
    # Possibly need to include an option to choose DB connection string

    args = parser.parse_args()

    """ Decide on the storage type to use File vs Databse """
    if args.file:
        userDirectory = FileStorage(args.file)
    else:
        hostName = 'localhost'
        portNumber = '8080'
        userDirectory = DBStorage(hostName,portNumber)

    """ Options """
    if args.add:
        currentUser = User(args.add)
        addUser(userDirectory,currentUser)		#TODO
    elif args.list:
        listUsers(userDirectory)				#TODO
    elif args.delete:
        currentUser = User(args.delete)
        deleteUser(userDirectory,currentUser)	#TODO
