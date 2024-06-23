num = 12
name = 'Shubham'

print(f"my {name} and {num}")

s='hello'
print(s[1:4])

l=[1,2,3]
l.append([4,5,6])
print(l)

d = {'k1':'Shubham'}
print(d['k1'][2])

print(set(d['k1']))
#A set is a list of only unique elements

seq=[1,2,3,4,5]
def time2(ag):
    return ag*2

print(list(map(time2,seq)))
print(list(map(lambda n:n*4,seq)))

print(list(filter(lambda n:n%2==1,seq)))

s='Hi there Sam!'

d= {'k1':[1,2,3,{'t':['a','b','c',{'d':[1,2,3,'e']}]}]}
print(d['k1'][3]['t'][3]['d'][3])

