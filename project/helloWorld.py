def elevate (num1 , num2):
    return num1**num2

def printAnyThing(text = None):
    print(text) if text != None else "No exist anything"
    print(elevate(int(input()), int(input())))
    



printAnyThing(input())