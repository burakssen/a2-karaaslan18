print("WELCOME")
start = "y"

comments = []

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
			allcomments = comments + [comment]
			comments = allcomments

	a = input("Are you sure(y/n):")
	if a == "n":
		a = start
	else:
		message = "See you later."
		print(message)
		break
