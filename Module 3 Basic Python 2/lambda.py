# def double(x):
#     return x*2
double=lambda num:num*2
squared=lambda num:num*num
result=double(44)
output=squared(9)
# print(result,output)
add=lambda x,y:x+y
sum=add(11,33)
# print(sum)
number=[12,56,98,78,56,12,6,98]
# double_num=map(double,number)
double_num=map(lambda x:x*2,number)
squared_num=map(lambda x:x*x,number)
print(number)
# print(list(double_num))
print(list(squared_num))

actor=[
    {'name': 'sabana' ,'age': 65 },
    {'name': 'shabnur' ,'age': 60 },
    {'name': 'sabila' ,'age': 45 },
    {'name': 'suhana' ,'age': 30 },
    {'name': 'sunny' ,'age': 25 },
]

junior=filter(lambda actor: actor['age']<40,actor)
fiver=filter(lambda actor:actor['age']%5==0,actor)
print(list(fiver))
# print(list(junior))

