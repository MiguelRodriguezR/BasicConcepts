def recurPower(base, exp):
    if exp!=0:
        if exp==1:
            return base
        else:
            return base*recurPower(base, exp-1)

    else:
     return 1

print (recurPower(3,4))
