#list,array,collection is same
number=[45,56,12,89,32,89,59,46,93]
print(number[3],number[-3])

#list(start:end)
print(number[2:6])
print(number[1:7])
#list(start:step)
print(number[1:7:1])
print(number[1:7:2])
print(number[7:2:-1])
print(number[7:2:-2])
print(number[4:])
print(number[:5])
print(number[:])#shortcut to copy a list 
print(number[::-1])#shortcut reverse a list