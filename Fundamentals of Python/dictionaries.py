'''
key value pair

my_dict = {key1:value1, key2:value2, key3:value3}

keys are unique identifiers for values in adictionary, they are immutable(strings, numbers or tuples) and each key is unique 

values are data associated with keys and can be of any data types including other dictionaries.



empty_dictionary = {}
my_dict = {'name':'John', 'age':25}

to access value:
name = my_dict['name']
age = my_dict['age']


to modify and add elements:
my_dict['age'] = 28
my_dict['gender'] = 'Male'


METHODS:
keys(): returns list of all the keys
values(): returns list of all values
items(): returns list of key-value pairs as tuples
get(key,default): returns values for given key or a default value if the key is not present
pop(key): removes and returns the value associated with the key.


Iterating over dictionary:
for key in my_dict:
    print(key)

for value in my_dict:
    print(value)

for key,value in  my_dict.items():
    print(key,value)



Nested dictionary:

nested_dict = {'person':{'name':'Alice','age':30,'address':{'city':'wonderland','zipcode':'12345'}}}

checking for key existence:
if 'name' in my_dict:
    print('Name exists:', my_dict['name'])

Dictionary comprehension: used to create dictionaries in a concise manner

squares = {x: x*x for x in range(5)}
//{0:0,1:1,2:4:3:9,4:16}

Dictionary constructor: can create dictionary using dict constructor
new_dict =dict(name = 'Bob', age=22)

Ordered dictionary:op[]
//to maintain the order of the keys as they were inserted, ordered dictionary can be used
from collections import OrderedDict
ordered_dict = OrderedDict([('a',1),('b',2),['c',3]])

'''