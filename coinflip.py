from random import randint

success=0
attempts=10000

for i in range(attempts):
    if randint(0,1)+randint(0,1)+randint(0,1)+randint(0,1)==3:
        success+=1;

print("attempts=",attempts)
print("success=",success)