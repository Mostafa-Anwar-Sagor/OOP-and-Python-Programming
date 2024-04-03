number=[12,45,98,68]
number.append(56)
print(number)
# number.insert(0,71)
print(number)
number.insert(2,81)
print(number)
if 98 in number:
    number.remove(98)
    print(number)
last=number.pop()
print(last,number)
if 5 in number:
  index=number.index(5)
  print(index)

sorted=number.sort()
print(number)
number.reverse()
print(number)