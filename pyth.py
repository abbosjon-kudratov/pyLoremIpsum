a=12
b=13
c=int("4")
t=float(5)
s=str(t)
s = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,

sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
#the same as previous, but using single quotes
#   s='''Lorem ipsum dolor sit amet,
#   consectetur adipiscing elit,
#   sed do eiusmod tempor incididunt
#   ut labore et dolore magna aliqua.'''


def dict_print_function():  #to print the elements inside dictionary
    for x in newAddict:
        print(x, newAddict[x])

def dict_print(**data):   #better function to print dictionary keys and values
    for x in data:
        print(x, data[x])



#LISTS = ordered, changable
someList=["something", 'somethong2', "something3"]
newList=someList.copy()
newList1=list(newList)
newList2=list(("somethig",'sdfsfd','sdfsf'))
newList2.append('newStuff')
newList2.extend(newList)
for x in someList:
    # print(x)
    if (x=="something"):
        someList.pop()
        print("nothing!!!")
        print("The length of the resulting list is now {}".format(len(someList)))  #format method of string used with placeholders
    else: break
print(newList2[1:])
""""
if(a<b):
    print("hello world!!!!")
    print("sdfsf")
    x = 15  # int
    d=45e-2
    e=56E3
    y = 2.8  # float
    z = 1j  # complex
    print(type(x))
    print(type(y))
    print(type(z))
    print(c,t)

    # print(type(s))
    print(s[2:])
    print(s.replace("c", "J"))
    print(s.upper())
    print(s.split(" "))
    age=36
    name="AK"
    txt="my name is {1} and age={0}"
    print(txt.format(age,name))
    x,y=5,1
    if(x>1 or y<0): print('what up!')

else:
    print("you're screwed")
"""

#TUPLES = ordered, but unchangable

newTuple=("apple", 'sausage', 'juice', 'cake')  #cannot change anything here after declaration

if "applsdfe" not in newTuple:
    print("Apple juice is not in this tupple")
    #del newTuple    #to delete it completely

    #make another new tuple:
    newTuple1=tuple(newTuple)
    print(newTuple1)
    del newTuple1

    newTuple2 = tuple(('first', 'second','third', 'first'))
    print(newTuple2)
    print("there are {} {} items in this tuppple!".format(newTuple2.count('first'),"'first'"))



#SETS = unordered and unindexed

newSet1={"ak", 'comedy', 'hkludy'}   #note the curly brackets
#print(newSet1)  #Sets are unordered, so the items will appear in a random order.

testString1=''
for y in newSet1:
    print(y)
    testString1+=(y)
print(testString1)

if('banana' not in newSet1): print("\nbananas are not here")

newSet1.add('lastWord')
newSet1.update(['so20', 'adfadf', 'goof']) #add this stuff to set
print(newSet1)

newSet1.remove('goof') #will raise error if 'goof' is not in set
newSet1.discard('goof') #will not give error if 'goof' is not in set

rand=newSet1.pop()  #this will not return the last element, 'cause there's no order
print(rand)

newSet1.clear()  #empty the set
del newSet1 #completely delete the set

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets  USING THE SET CONSTRUCTOR
print(thisset)



#NOW TIME FOR DICTIONARIES
newAddict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1977
}
print(newAddict)
print(newAddict['brand']+' '+newAddict.get('model')+'is a good car')

x=newAddict['model']
x=newAddict.get('model')  #the same as previous
print(x)

newAddict['brand']='chevvy'
newAddict['model']='camaro'
newAddict['year']=2018
print(newAddict)

for x in newAddict:
    print(x,newAddict[x])

for x,y in newAddict.items(): #same as previous one
    print(x,y)

for x in newAddict.values():
    print(x) #print only values


if 'model' in newAddict:  #check if the key exists , but cannot check the values like this
    print('yes it really exists')
else: print('go to hell')

print('This dictionary has {} items'.format(len(newAddict)))

newAddict['color']='red'

print('Now After adding one property This dictionary has {} items'.format(len(newAddict)))
print('here are they:')
dict_print_function() #it can print only one this predefined dictionary
#OR usinf a better function
dict_print(**newAddict)  #this can print any dictionary

print('\n after popping:')
newAddict.popitem()
dict_print_function()


print('\n after popping model')
newAddict.pop('model')
dict_print_function()


newDictionary1 = newAddict.copy() #copy the dictionary
newDictionary2=dict(newAddict) #copy the dictionary
print(newDictionary2)


thisdict =	dict(brand="Ford", model="Mustang", year=1964)  #note that not double brackets
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
#print(thisdict)
dict_print(**thisdict)



keys = ('brand', 'year', 'location')
values = ('google', 1996, 'California,USA')
companyDict = dict(zip(keys, values))    #CREATING DICTIONARY FROM  2 LISTS or TUPLES
dict_print(**companyDict)


