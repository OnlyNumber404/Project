import random
mylist = []
one = random.randint(1,10)
for i in range(1,one):
    mylist.append(i)
    print(i)
two = random.choice(mylist)
print("Has Choice = ",two)