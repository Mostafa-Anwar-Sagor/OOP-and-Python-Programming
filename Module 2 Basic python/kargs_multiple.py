def full_name(first,last):
    name=f'Full name is: {first} {last}'
    return name
name=full_name('alu' , 'kodu')
print(name)

#def famous(**kargs)
def famous_name(first,last,title,**addition):
    name=f'{title} {first} {last}'
    # print(addition)
    for key,value in addition.items():
        print(key,value)
    return name
name=famous_name(first='taheri' ,last='ali',title="hujur",addtion="sheikh")
print('hujurname: ',name)