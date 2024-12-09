import random

amount = 0
x = random.randint(1,100)

for i in range(1,x):
    if x%(i+1) == 0:
        amount+=1

if amount == 2:
    print("es primo")
else:
    print("no es primo")

print(x)