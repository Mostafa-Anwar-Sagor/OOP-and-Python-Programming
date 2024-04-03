number=[12,56,98,78,56,12,26,98]
person=['kala chan','kali pur',23,'student']

person={'name':'kala pakhi','address':'kali pur','age':23,'job':'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language']='python'
person['name']='sada pakhi'
del person['age']
print(person)
#dictionary looping
for key,value in person.item:
    print(key,value)