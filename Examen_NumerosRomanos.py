"""
NOMBRE: Alexys Martín Coate Reyes
MARTÍCULA: A01746998
INSTRUCCIONES:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""
def main():
    num = input("Dame un número entero: ")
    print("El número romano es: ", calcularNumRomano(num))

def prueba():
    for num in range(0,4000):
        num = str(num)
        print(calcularNumRomano(num))
        #print(num + "=" + calcularNumRomano(num))

def calcularNumRomano(num):
    #Lista de carácteres y diccionario de excepciones
    charsL = ["I","V","X","L","C","D","M"]
    charsD = {1:"I", 4:"IV",5:"V", 9:"IX",
             10:"X", 40:"XL",50:"L", 90:"XC",
             100:"C", 400:"CD",500:"D", 900:"CM",
             1000:"M"}

    if type(num) != str:
        print("Se debe ingresar una String que sea un número entero!!!")
        return None
    if num == "0":
        print("No existe el 0 en Romano")

    #Inicialización del resultado
    numRomano = ""
    #Cantidad de dígitos que tiene el número
    posValue = len(num)

    for number in num:

        #Se definen los valores a ocupar (MIN, MEDIO, MAXIMO) al reemplazar los valores
        if posValue > 3:
            min = charsL[len(charsL)-1]
        else:
            min = charsL[(posValue - 1) * 2]
            medio = charsL[(posValue - 1) * 2 + 1]
            max = charsL[(posValue - 1) * 2 + 2]

        #Se desarrolla el número de acuerdo a su valor posicional
        numeroDesarrollado = int(number)*pow(10,posValue-1)
        #Parte posicional del número
        number = int(number)

        #Añadir carácteres romanos
        #Su el caracter romano es una excepción y está en el diccionario
        if numeroDesarrollado in charsD:
            numRomano += charsD[numeroDesarrollado]
        #Si el valor es 0 entonces se omite
        elif number == 0:
            posValue -= 1
            continue
        #Si el valor es menor a 3 se repite hasta 3 veces el símbolo mínimo
        elif number <= 3:
            while(number != 0):
                numRomano += min
                number -= 1
        #Si el valor es menor a 8 se repite 1 vez el símbolo medio y hasta 3 veces el símbolo mínimo
        elif number <= 8:
            numRomano += medio
            while(number > 5):
                numRomano += min
                number -= 1

        #Impresión de los nuevos símbolos de acuerdo al valor posicional
        #print("MIN: ",min)
        #print("MEDIO: ", medio)
        #print("MAX: ", max)
        #print()

        posValue -= 1

    return numRomano

#prueba()
main()