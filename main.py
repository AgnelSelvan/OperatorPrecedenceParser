ipbuffer = input("Enter Input buffer with SPACE: ")

print("Entered input buffer is : "+ipbuffer)

a = "$"
stack = []
finishipbuffer = []
b = ipbuffer.split(" ")
print(b)

def highPrecedence(a, b):
    
    return True
def equalPrecedence(a, b):
    return False

def lessPrecedence(a, b):
    return False

for ele in b:
    if a == '$' and str(ele) == '$':
        break

    else:
        if lessPrecedence(a, str(ele)) or equalPrecedence(a, str(ele)):
            stack.append(a)
            finishipbuffer.append(ele)

        elif highPrecedence(a, str(ele)):
            while highPrecedence(ele, stack.pop()):
                stack = stack.pop()
        else:
            print("Error")
        

print(b)
print(stack)
print(finishipbuffer)