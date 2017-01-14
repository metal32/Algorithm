""" DEFENSIVE PROGRAMMING EXAMPLE 
Here we consider that users are bound to make mistake so we have to take some defensive measures as they don't make even any silly mistakes

EXAMPLE: To calculate hypotenuse """
## Below function will make sure that your input value is of Float type otherwise it will throw an error and keep n running infinitely.
import math
def toGetFloat(requiredMsg,errorMsg):
    input_ok=False
    while not input_ok:
        val=input(requiredMsg)
        if type(val)==type(1.0):
            input_ok=True
        else:
            print errorMsg
    return val
base=toGetFloat("Enter the base value :","Error: base must be a float")
height=toGetFloat("Enter the height value :","Error: height must be a float")
hypotenuse=math.sqrt(base**2+height**2)
print "The base and height value of a right triangle are respectively {} , {}.\n Hence the hyptenuse will be {}.".format(base,height,hypotenuse)


 

