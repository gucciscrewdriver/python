
matrix = [['EX', 'OH', 'EX'], ['OH', 'EX', 'OH'], ['EX', 'OH', 'EX']]

"""for x in matrix:
    for i in x:
        print(i)
    print"""

x = 0
i = 0

while x < len(matrix):
    #print(matrix[x])
    i = 0
    while i < len(matrix[x]):
        print(matrix[x][i])
        i += 1
    x += 1
    print 

"""print matrix[0]
print matrix[1]
print matrix[2]"""

"""lst = (1, 2, 3, 4, 5)
lst2 = (for x in lst if x <= 4)
print (lst2)"""
