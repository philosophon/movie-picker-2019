import random
action=["avengers endgame","spiderman:far from home", "jumanji", "shazam", "Godzilla: King of the Monsters"]
horror=["Us", "demon eye", "childs play" , "annabelle 2", "prodigy", "it", "pet cemetary"]
comedy=["42nd street:the musical", "murder mystery", "plus one", "granddaddy day car"]
scifi=["star wars:rise of skywalker","captain marvel", "dark pheonix", "alita:battle angel", "see you yesterday"]
fantasy=["malifiecent 2", "cruella", "chronicle of narnia:the silver chair", "five nights at freddys", "dragonology"]
animation=["toy story 4", "frozen 2", "spies in disguise", "ugly dolls", "angry birds 2","spiderman into the spiderverse"]
while True:
	genre=input("what genre do you want to see? Press q to quit\n")
	if genre=='action':
		for x in action:
			print(x)
			ask = input("would you like to see this movie? y/n")
			if ask == "y":
				break
	elif genre=='horror':
		for x in horror:
			print(x)
			ask = input("would you like to see this movie? y/n")
			if ask == "y":
				break
	elif genre=='comedy':
		for x in comedy:
			print(x)
			ask = input("would you like to see this movie? y/n")
			if ask == "y":
				break
	elif genre=='scifi':
		for x in action:
			print(x)
			ask = input("would you like to see this movie? y/n")
			if ask == "y":
				break
	elif genre=='fantasy':
		for x in fantasy:
			print(x)
			ask = input("would you like to see this movie? y/n")
			if ask == "y":
				break
	elif genre=='fantasy':
		for x in fantasy:
			print(x)
			ask = input("would you like to see this movie? y/n")
			if ask == "y":
				break
	elif genre == "q":
		break
	else:
		print("that's not an option")