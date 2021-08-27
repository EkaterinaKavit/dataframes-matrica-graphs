stack=[3,4,5]

# Append добавляет новый элемент в конец списка
stack.append(6)
stack.append(7)
print(stack)

# pop удалит последний эл-т
stack.pop()
print(stack)

#List Comprehensions
#1 way
squares=[]
for x in range (10):
    squares.append(x**2)
print (squares)

#2way
squares=list(map(lambda x:x**2,range(10)))
print(squares)

#3way
squares=[x**2 for x in range(10)]
print(squares)

#Another examle
# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
#1 way
combs=[]

for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))

print(combs)

#2 way

combs=[(x,y) for x in [1,2,3] for y in [3,1,4]  if x!=y]
print(combs)

#Another example
vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
vec_doubled=[x*2 for x in vec]
print(vec_doubled)

# filter the list to exclude negative numbers
vec_without_negative=[x for x in vec  if x>=0]
print(vec_without_negative)

# apply a function to all the elements
vec_func=[abs(x) for x in vec]
print(vec_func)

# create a list of 2-tuples like (number, square)
vec_tuple=[(x,x**2) for x in vec]
print(vec_tuple)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec_flatten = [num for elem in vec for num in elem]
print(vec_flatten)