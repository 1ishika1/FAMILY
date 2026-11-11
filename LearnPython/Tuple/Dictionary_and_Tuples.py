#Lists are mutable, they are dynamic arrays
x = [4,5]
print(x[0])
x[0] = 10
print(x[0])

#Tuples are immutable
y = (4, 5)
print(y[0])
# y[0] = 10
print(y[0])

def find_pe_and_pb(price, eps, book_value):
    pe = price/eps
    pb = price/book_value
    return pe, pb

pe_ratio, pb_ratio = find_pe_and_pb(100, 5, 20)
print(pe_ratio)
print(pb_ratio)

#Look up by key is faster than look up by index
#Look up by key is O(1) and 
#Insertion/Deletion is O(1) on average
d = {'bjd': 100, 'aapl': 200, 'msft': 300}
print(d['aapl'])
print(d.get('add', 0)) #returns 0 if key is not found
d['aapl'] = 250 #update value
d['www'] = 400 #insert new key-value pair
print(d)
del d['aapl'] #delete key-value pair
print(d)

#Dictionaries are mutable, they are dynamic arrays
#Dictionaries value can also be a dictionary
contact_dict = {
    'rachel':{
        'phone': 123-456-7890,
        'email': 'rachel@example.com'
    }
}
print(contact_dict['rachel']['email'])

for name in d:
    print(name, d[name])

for name, number in d.items():
    print(name, number)

print(d.keys())
print(d.values())