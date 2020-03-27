import pandas

grammar = []
variable = []
terminal = []
operator_terminal = []
identifier_terminal = []
with open('input.txt', 'r') as file:
    for line in file:
        print(line)
        line = line.split(' ')
        for i in line:
            i = i.replace('\n', '')
            if i != '->' and i not in grammar:
                grammar.append(i)

for g in grammar:
    g = str(g)
    if g.isupper():
        variable.append(g)
    else:
        terminal.append(g)
        if g.isalpha():
            identifier_terminal.append(g)
        else:
            operator_terminal.append(g)


print("Variable: ", end = " ")
print(variable)
print("Operator Terminal: ", end = "" )
print(operator_terminal)
print("Terminal: ", end="")
print(terminal)
print("Identifier Terminal: ", end="")
print(identifier_terminal)

terminal.append('$')

i = 0

terminal_dct = {i: terminal.index(i) for i in terminal}

matrix = []
def assignPrecedence(i, j):
    ele = list(terminal_dct.keys())[list(terminal_dct.values()).index(i)]
    ele1 = list(terminal_dct.keys())[list(terminal_dct.values()).index(j)]
    for identifier in identifier_terminal:
        if ele == identifier:
            return '.>'
        elif ele1 == identifier:
            return '<.'
        
    if ele == '+' and ele1 == '*':
        return '<.'
    elif ele == '*' and ele1 == '+':
        return '.>'
    elif ele == '+' or ele == '*' and ele1 == '$':
        return '.>'
    elif ele1 == '+' or ele1 == '*' and ele == '$':
        return '<.'
        



for i in range(0, len(terminal_dct)):
    matrix.append([])
    for j in range(0, len(terminal_dct)):
        if i == j:
            for k in identifier_terminal:
                if list(terminal_dct.keys())[list(terminal_dct.values()).index(i)] == k:
                    matrix[i].append('-')
                else:
                    matrix[i].append('.>')
        else:
            precedence =  assignPrecedence(i, j)
            matrix[i].append(precedence)
            

print("Precedence Table")
table = pandas.DataFrame(matrix, terminal, terminal)
print(table)


ipbuffer = input("Enter Input buffer with SPACE: ")

print("Entered input buffer is : "+ipbuffer)

a = "$"
stack = []
finishipbuffer = []
b = ipbuffer.split(" ")

def checkPrecedence(a, b):
    a = terminal_dct[a]
    b = terminal_dct[b]
    return matrix[a][b]

stack.append(a)
rot = True
print("Stack    | input buffer")
print(str(stack)+"\t| ", end = "")
print(b)
while rot:
    for ele in b:
        if stack[-1] == '$' and str(ele) == '$':
            print(str(stack)+"\t| ", end = "")
            print(b)
            print("String accepted")
            rot = False
            break

        else:
            a = str(stack[-1])
            if checkPrecedence(a, str(ele)) == '<.' or checkPrecedence(a, str(ele)) == "":
                stack.append(str(ele))
                b.remove(ele)
                finishipbuffer.append(ele)
                print(str(stack)+"\t| ", end = "")
                print(b)

            elif checkPrecedence(a, str(ele)) == '.>':
                if stack[-1] != '$':
                    stack.pop()
                else:
                    rot = False
