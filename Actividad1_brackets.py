"""
NOMBRE: Alexys Martin Coate Reyes
# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('
Sube la url de un archivo de github
"""

str = input('Enter: ')
stack = list()
stackA = list()

try:
    for i in str:
        stack.append(i)
        if i == '(':
            stackA.append('(')
            print(stackA)
        elif i == '[':
            stackA.append('[')
            print(stackA)
        elif i == ')':
            print("Elemento removido")
            if stackA.pop() != '(':
                print(stackA)
                print('Sintaxis incorrecta!!!\n     Falta cerrar con un: ( en la posición',len(stackA)+1)
                break
        elif i == ']':
            print("Elemento removido")
            if stackA.pop() != '[':
                print(stackA)
                print('Sintaxis incorrecta!!!\n     Falta cerrar con un: [ en la posición',len(stackA)+1)
                break
except:
    print("La lista ingresada es muy pequeña o ocurrió algún otro error")
    quit()

print('Stack:',stack)
print(stackA)

if len(stackA) == 0:
    print('La sintaxis es correcta')
else:
    #Si aun quedan elementos significa que no todos los [] o () están cerrados
    print('No se cerraron todos los elementos!!!')
