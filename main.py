#Variables
name = "Beau"
age = 39

# To get the type of data
#print(type(name))
print(type(name) == str)

print(isinstance(age, float))

def hello(name='my friend'):
    print("Hello " + name)

hello()
