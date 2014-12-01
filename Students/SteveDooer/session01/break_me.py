#Explore Errors

#Create a NameError
#nameerrors value is not referenced before being called

def createNameError():
	return nameerrors

#Create a TypeError
#Cannot add int and str together beacause they are different types

def createTypeError():
	a = 5
	b = "you"
	return a + b

# Create a SyntaxError():
# Misplaced period on return line

def createSyntaxError():
	return whoops.

# Create a Attribute Error
# Float object does not have a length attribute

def createAttributeError():
	a = 5.3
	return a.length


# createNameError()
# createTypeError()
# createSyntaxError()
# createAttributeError()