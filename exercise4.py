temperatures=[10,-20,-289,100]
for i in temperatures:
    fahrenheit = i*9/5+32
    if fahrenheit<-459:
        print("That temperature doesn't make sense!")
    else:
        print (fahrenheit)
"""temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f
    else:
        return "That temperature doesn't make sense!"
for t in temperatures:
    print(c_to_f(t))"""
