import random

print("==================================================================")

random_int = random.randint(0, 100)

def curse_random_int():
    print(f"Fuck you, {random_int}")

curse_random_int()

print("==================================================================")

names_list = ["Ashley", "Robert", "Alejandro", "Jose", "Brigitte"]
you_are_a_bitch = True

if len(names_list) >= random_int or you_are_a_bitch: # Of course you're
    names_list.append("Barry")

print(names_list)
print(names_list[1+1])

print("==================================================================")

liste = [1, 2]
one, _ = liste
print(one)

print("==================================================================")

# Commented because it was annoying on runtime
# while I was trying other things.
""" bruh = ('ayo', 'ooomaigaa', 'yessir', 'goofy', 'ahh')
try:
	print(bruh.index(input('What you aiming at?\n')))
except ValueError:
	print('Bruh who you trynna call smh') """


capyslay = {'chuiguire', 'rissotto', 'gort', 'carpincho'}
if len(capyslay) > 20:
    print(capyslay) 
elif len(capyslay) < 10:
    print('Capy slay') 

new_capy = {'py', 'go', 'rs'}
print(new_capy.union(capyslay))

print("==================================================================")

giorgio_dict = {
    "name": "Giorgio",
    "surname": "Giovanni",
    "hobbie": "dance",
    "age": "900a.c"
}
print(f"Giorgio loves to {giorgio_dict['hobbie']}.")
print("You're goddamn right. Giorgio is the best dancer.")

for i in giorgio_dict.values():
    if i != "Giorgio":
        print(f"- {i}")
    else:
        print("- Giorgio is an amazing duck.")

print("==================================================================")

capy_is_god = True
if capy_is_god:
    print("Capy supremacy")

print("==================================================================")

def print_lots_of_capys(*capys):
    for capy in capys:
        print(f"I love {capy}")

print_lots_of_capys("Gort", "Risotto", "Robert", "Chigui")

print("==================================================================")

class Capybara:
    def __init__(self, name: str):
        self.name = name

    def slay(self):
        print(f"{self.name} slays") # it's a better practice to use a return, and so, I can use the print statement as below

my_capy = Capybara("Gort")
print(my_capy.name)
print(my_capy.slay()) # prints None afterwards (solved: it was printing a print)
my_capy.slay()        # (solution) the function is being called directly  // if return is used, this doesn't print anything

Capybara("GG").slay() # also a way to call it without assigning it // same case as above

print("==================================================================")

capy_is_not_good = False 

try:
    print(capy_is_not_good + "") # added this error on porpose due to a vscode visual disconfort
except TypeError:
    print("Capy is always good")
except Exception as e:
    print(e)
else:
    print("Well... maybe not always good :(")
finally:
    print("I love Capybaras")
    
print("==================================================================")