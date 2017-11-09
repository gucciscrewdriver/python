lst = [23, 21, 420, 2000, 1, 123]
lst2 = []
#lst2 has only numbers divisible by 5
"""num1 = 8
if num1 % 2 == 0:"""
#lst.append[2]
# All lists in python start with 0
"""for element in lst:
#    if element > 20 and elememt < 100: (or it could also be)
#    if 20 < element < 100:
    if element == 20:
        lst2.append(element)
print lst
print lst2"""

#lst2 = [x for x in lst if x > 25]
lst2 = [x for x in lst if x % 5 == 0]

#print(lst2)

lst3 = ['hello', 'hi', 'wow', 'filthy frank', 'chelsea']
str1 = 'wow'

lst4 = [x[0] for x in lst3 if len(x) <= 6]




matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

#print(matrix[0][2])
x = 0
while(x < 69):
    print(x)
    x = x + 2

for variable in lst3:
    print(variable)
