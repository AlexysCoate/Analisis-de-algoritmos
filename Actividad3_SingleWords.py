"""
Nombre: Alexys Martín Coate Reyes
# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
#   Input:
#       'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#   Output:
#       'alpha beta gamma delta'
# This algoritm must run in time n
"""

a = input("Enter: ")
list = a.split()
list2 = []

for i in list:
    if i not in list2:
        list2.append(i)

print(list2)