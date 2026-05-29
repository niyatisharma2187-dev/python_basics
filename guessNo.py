import random
n=random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a=int(input("Enter the number: "))
    if(a>n):
        print("lower number please!!")
    else:
        print("Higher number please!!")
    guesses +=1
print(f"Congratulations you are assumed the right number which is:{n} on attemps {guesses}")
