print("WELCOME")
start = "y"
comments = []

#copied part starts
from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
#copied part ends

mypassword = '981ff4a93dbb05d76d4cd34d3fb0f493db0145d653ee56cbb71a93853adcef4e'

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
				if password == "e":
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
