print("\n\n\tWelcome in Maharana pratap Group of Institutions\n")
res = "yes"
p = int(input("Enter the present => "))
if(p<50):
    print("Come with parents")
    res = "decline"
elif(p<60):
    print("Fine 400 indian rupees")
elif(p<70):
    print("Fine 200 indian rupees")
elif(p < 80):
    print("\tFine 100 indian rupees")
elif(p < 90):
    print("\tFine 50 indian rupees")
else:
    print("No fine")
    res = "No fine"
if("yes" in res):
    state = input("Have you any medical leave reply yes and no => ")
    if("yes" in state or "Yes" in state):
        p  += p/20
        print("you would have be relaxation base on new presence => ", int(p))
        if(p<60):
            print("Fine 400 indian rupees")
        elif(p<70):
            print("Fine 200 indian rupees")
        elif(p < 80):
            print("\tFine 100 indian rupees")
        elif(p < 90):
            print("\tFine 50 indian rupees")
        else:
            print("No fine")
    elif "no" in state or "No" in state:
        print("no relaxation")
    else:
        print("Reply only yes or no, fill again with right input")
elif("decline" in res):
    print("-------------Notice---------------------")
else:
    print("Congratulation, You are selected for prize base on presence")
