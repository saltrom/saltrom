"""""
num = int(input("Please enter the number to check: "))
numlist = []
for i in range(2,num):
    status = False
    for k in range(2,i):
        if i %k == 0:
            status = True                                 #LONG
            break
    if not status:
        numlist.append(i)
for i in numlist:
    print(i)
print("All numbers here are prime")
"""

"""
num = int(input("Please enter the number to check: "))
if num %2 == 0 or num %3 == 0 or num %4 == 0 or num %5 == 0:
    print("This Number is Not Prime")                              #SHORT
else:
    print("This Number is Prime")
"""

