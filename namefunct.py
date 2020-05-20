def person(name):
  """person(name): Returns the Person's name"""
  print(name)



#another function
def maximum(*numbers):
    """maximim(numbers): returns the maximum number"""
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
                print(maxnum)


person('Lawrence')            
maximum(5, 2, 10, 8)
print(maximum.__doc__)
print(person.__doc__)

##learn later these are called modules which is a group of python functions. 
##Can be imported into other files using the name of the file (namefunct.py) 
##and the functions would be access like namefunct.person('Lawrence')
            
