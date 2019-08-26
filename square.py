def raise_to_power(x,y):
    
    new_value = x ** y
    
    #This creates a tuple with public output.
    global stuff 
    stuff = (new_value, int(x), int(y))
    

def root(solution, value1, value2):
    print (str(solution) + 'root' + str(value2) +'is ' + str(value1))


raise_to_power(5,4)
squared = raise_to_power
#print your tuple
print (*stuff)

#Finally use the asterisk to expand the tuple as input for the next leg...
#root(*stuff)
