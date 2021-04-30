import os
print()
print()

dir = [d for d in os.listdir() if d != __file__]

for d in dir:
    print(d)
    print()
    for f in os.listdir(d):
        print("<img src='img/portfolioItems/"+d+"/"+f+"' alt=''>")
    print()
    print()



