print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")
l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")

true_total = t + r + u + e
love_total = l + o + v + e

true_love_total = int(str(true_total) + str(love_total))

if true_love_total < 10 or true_love_total > 90:
    print(f"Your score is {true_love_total}, you go together like coke and mentos.")
elif 40 <= true_love_total <= 50:
    print(f"Your score is {true_love_total}, you are alright together.")
else:
    print(f"Your score is {true_love_total}.")