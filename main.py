import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	exclusiveGroup = parser.add_mutually_exclusive_group()
	exclusiveGroup.add_argument('-c','--create',help='Create a new user in the directory')
	exclusiveGroup.add_argument('-l','--list',action='store_true',help='List all users in directory')
	exclusiveGroup.add_argument('-d','--delete',help='Delete user in directory')
	parser.parse_args()
