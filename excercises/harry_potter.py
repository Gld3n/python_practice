import time

""" 
Not an accurate use of the characteristics of each house.
I asked for help to a friend of mine, I'm a Muggle (I love HP actually).
I apologize beforehand for any inconvenience.
This is just an implementation of the excercise.
"""

hufflepuff, slytherin, gryffindor, ravenclaw = 0, 0, 0, 0

def verification():
    global hufflepuff, slytherin, gryffindor, ravenclaw

    try:
        election = int(input(""))
    except ValueError:
        print("You need to provide a number between 1 and 4")
        election = int(input(""))

    while election >=1 and election <= 4:
        if election == 1:
            hufflepuff += 1
            break

        elif election == 2:
            slytherin += 1
            break

        elif election == 3:
            gryffindor += 1
            break

        elif election == 4:
            ravenclaw += 1
            break
    print(hufflepuff, slytherin, gryffindor, ravenclaw)


def election_one():
    print("""You consider yourself:
    1. Slick
    2. Ingenious
    3. Impulsive
    4. Loyal
    
Please choose by number.""")
    
    verification()

def election_two():
    print("""You consider yourself:
    1. bb
    2. 
    3. 
    4. 
    
Please choose by number.""")
    
    verification()

def election_three():
    print("""You consider yourself:
    1. ccc
    2. 
    3. 
    4. 
    
Please choose by number.""")

    verification()

def election_four():
    print("""You consider yourself:
    1. dddd
    2. 
    3. 
    4. 
    
Please choose by number.""")

    verification()


print("==============================================================================================")
print("You will be selected for one of the houses depending on your choice. Be honest... if you wish).\n")

count = 0
while count <= 5:
    if count == 0:
        election_one()
    elif count == 1:
        election_two()
    elif count == 3:
        election_three()
    elif count == 4:
        election_four()
    elif count >= 5:
        print("The end.")
        break

    count += 1


if hufflepuff > (slytherin and gryffindor and ravenclaw):
    print("1")
elif slytherin > (hufflepuff and gryffindor and ravenclaw):
    print("2")
elif gryffindor > (hufflepuff and slytherin and ravenclaw):
    print("3")
elif ravenclaw > (hufflepuff and slytherin and gryffindor):
    print("4")    
elif hufflepuff == (slytherin and gryffindor and ravenclaw ):
    print("5")


time.sleep(1)
print("Result")