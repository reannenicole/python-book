recruitment_link = ("wwwjobscom")

polite_message = "Your current wage should be "
band_1 = "£19000 - £20500"
band_2 = "£20500 - £23000"
band_3 = "£23000 - £27000"
band_4 = "£27000 - £32000"
band_5 = "£32000 and up" 

current_wage = input("what is your current wage band from 0-5?: ")


if current_wage == "0":
    print(("Looks like you're not employed by us, lets find you a job ") + recruitment_link)
elif current_wage == "1":
    print (polite_message + band_1)
elif current_wage == "2":
    print (polite_message + band_2)
elif current_wage == "3":
    print (polite_message + band_3)
elif current_wage == "4":
    print (polite_message + band_4)
elif current_wage == "5":
    print (polite_message + band_5)
else:
    print ("Sorry I didn't recognise that, please enter a number between 1 and 5")