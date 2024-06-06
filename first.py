a=10
b=20.0
c=3+2j
print (a+b)
print(type(a))
print(type(b))
print(type(c))
d=("abey")
e=("thomson")
print(type(d))
print(d)
print(d+e)
f=True
print(type(f))
g=['abey','dilsha']
print(g)
print(type(g))
h=('abey','dilsha')
print(type(h))
i={'abey','dilsha'}
print(type(i))

list1 = list((2,4,6,8,10))
print(type(list1))
list2 = ['hello', (1,2,3,4),['world']]
print(type(list2))

j = {'stud1' :{
    'name' : 'abin',
    'age' : 18,
    'marks' : {
        'maths' : 88,
        'english' : 85
    }},
    'stud2' :{
    'name' : 'juan',
    'age' : 17,
    'marks' : {
        'maths' : 80,
        'english' : 65
    }
    }

}
print(j)
print(type(j))

print(j['stud2'])
print(j.get('stud1').get('name'))

set1 ={1,2,3,4,5}
set2 = {'a','b','c','d',21,22,23,'a',22,'23'}
print(set1)
print(set2)
