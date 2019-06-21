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

newSet1={"ak", 'comedy', 'hkludy'}
#print(newSet1)  #Sets are unordered, so the items will appear in a random order.

testString1=''
for y in newSet1:
    print(y)
    testString1+=(y)
print(testString1)

if('banana' not in newSet1): print("\nbananas are not here")

newSet1.add('lastWord')
newSet1.update(['so20', 'adfadf', 'goof'])
print(newSet1)