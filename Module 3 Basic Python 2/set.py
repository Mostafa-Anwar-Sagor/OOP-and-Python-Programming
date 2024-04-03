number=[12,56,98,78,12,6,98]
number_set=set(number)
print(number_set)
number_set.add(55)
print(number_set)
number_set.remove(6)
print(number_set)
for item in number_set:
    print(item)
if 9 in number_set:
    print('9 exist')
elif 98 in number_set:
    print('98 exist')

a={1,3,5,7}
b={1,2,3,4,5}
print(a&b)
print(a|b)
