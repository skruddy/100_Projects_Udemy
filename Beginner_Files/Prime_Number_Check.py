#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(int((number/2)+1)):
        for j in range(int((number/2)+1)):
            if i*j == number:
                is_prime = False
                break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
