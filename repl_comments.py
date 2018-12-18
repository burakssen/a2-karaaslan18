print("WELCOME")
start = "y"
comments = []

#copied part starts
from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
#copied part ends

mypassword = 'de8f8396402c' + '642d8b144c86' + '8798b693a6367d1ae83' + 'd3d329ce4c73544c77e79'

while start == "y":
	
	while True:
		
		comment = input("Type your comment(type s to see all comments, e to exit): ")
		if comment == "e":
			break
		if comment == "s":
			if comments == []:
				message = "You do not have any comments."
				print(message)
			else:
				print(allcomments)
		else:
			while True:
				password = input("Please enter your password(type g to give up):")
				if password == "g":
					break
				userinput = create_hash(password)
				
				if userinput == mypassword:
					allcomments = comments + [comment]
					comments = allcomments
					break
				else:
					message = "Your password is not true"
					print(message)
            

	a = input("Are you sure(y/n):")
	if a == "n":
		a = start
	else:
		message = "See you later."
		print(message)
		break
