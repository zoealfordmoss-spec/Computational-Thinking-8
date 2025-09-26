day_person = 0
night_person = 0


answer = input("If you could be any animal would you rather A be a owl, or B be a deer")  
if answer == "A" or answer == "a":
	day_person += 1
elif answer == "B" or answer == "b":
	night_person += 1
else:
    print("you can only do A or B try again!")


answer = input("what is your favorite movie  A Twilight,  B The Bee Movie, C The Breakfast Club or D Goosebumps?")    
if answer == "A" or answer == "a":
	day_person += 1
elif answer == "B" or answer == "b":
	night_person += 1
elif answer == "C" or answer == "c":
	day_person += 1
elif answer == "D" or answer == "d":
	night_person += 1
else:
	print("try one of the letter ABCD please")


answer = input("if you could choose what job you want when you grow up would you rather A be a doctor, or B a reporter?")
if answer == "A" or answer == "a":
	night_person += 1 
elif answer == "B" or answer == "b":
	day_person   += 1
else:
	print ("you messed up again! start over bud")

answer = input("Are you A an extrovert, or B an introvert?")
if answer == "A" or answer == "a":
	day_person += 1
elif answer == "B" or answer == "b":
	night_person += 1


answer = input("whats your favorite season A winter, or B summer?")
if answer == "A" or answer == "a" and night_person > 1:
	print("are you sure you like winter?")
	night_person += 1
elif answer == "B" or answer == "b":
	day_person += 1


if day_person > night_person:
	print("you are a day person! you like to wake up early and love to hang out with friends")	
elif night_person > day_person:
	print("you are a night person! you enjoy movies and night time walks with you dog")