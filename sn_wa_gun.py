import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True 
        elif you == 'g':
            return False         
    elif comp == 'g':
        if you == 'w':
            return True 
        elif you == 's':
            return False           

print("comp turn:snake(s), water(w), gun(g)")
randNO = random.randint(1,3)
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'
# print(comp)

you = input("your turn:snake(s), water(w), gun(g)")
a = gamewin(comp, you)

print(f"computer choose: {comp}")
print(f"you choose: {you}")

# if a == None:
#     print("The game is a tie!")
# elif a:
#     print("You Win!")
# else:
#     print("You Lose!")
print(a)