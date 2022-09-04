def function(a, b):
    c = a + b
    return c

print(function(1, 2))

Flag = True
def advertising(array, int):
    for i in array:
        if i == int:
            Flag = False
    if Flag == False:
        print("Found!")
    else:
        print("Not Found!")
        
advertising([1, 2, 3], 3)
