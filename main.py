def even(a):
    if a % 2 == 0:
        return True
    else:
        return False
# -
inpt = int(input('Enter number: '))
while inpt != 1:        
        if even(inpt):
            inpt = inpt / 2
            print(inpt)
        else:
            inpt = inpt * 3 + 1
            print(inpt)