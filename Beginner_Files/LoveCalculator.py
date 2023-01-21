# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def occInTrue(name):
    name = name.lower()
    aCount = name.count("t")
    aCount += name.count("r")
    aCount += name.count("u")
    aCount += name.count("e")
    return aCount


def occInLove(name):
    name = name.lower()
    aCount = name.count("l")
    aCount += name.count("o")
    aCount += name.count("v")
    aCount += name.count("e")
    return aCount


countInTrue = occInTrue(name1) + occInTrue(name2)
countInLove = occInLove(name1) + occInLove(name2)
finalPercentage = int(str(countInTrue)+str(countInLove))

if finalPercentage <= 10 or finalPercentage >= 90:
    print(f"Your score is {finalPercentage}, you go together like coke and mentos.")
elif finalPercentage >= 40 and finalPercentage <= 50:
    print(f"Your score is {finalPercentage}, you are alright together.")
else:
    print(f"Your score is {finalPercentage}")