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


someList=["something", 'somethong2', "something3"]

for x in someList:
    # print(x)
    if (x=="something"):
        print("nothing!!!")
    else: break

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

