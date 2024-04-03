name='sakib\'s khan'#escape
name2="Shakib khan"
#multiline string
name3="""
    shakib khan
    Number one
"""
print(name3)
for char in name2:
    print(char )
print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])
#list mutable means changeable

# name2[0]='R'
# print(name2)
if 'khan' in name2:
    print('exist')
print(name2.upper())
