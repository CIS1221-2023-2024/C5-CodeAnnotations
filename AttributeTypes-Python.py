# Code Annotations - Attributes
class ClassAttributes:
    attribute = "I am a class attribute"
    # A class attribute will remain the same for each object

obj1 = ClassAttributes()
obj2 = ClassAttributes()

print(obj1.attribute)  # Output: I am a class attribute
print(obj2.attribute)  # Output: I am a class attribute


class InstanceAttributes:
    def __init__(self, value):
        self.attribute = value

# Creating two instances (objects) of the InstanceAttributes class
obj1 = InstanceAttributes(23)
obj2 = InstanceAttributes(81)

# Accessing and printing the 'attribute of obj1 and obj2'
# Each object has its own attribute value based on the provided values during creation

print(obj1.attribute)  # Output: 23
print(obj2.attribute)  # Output: 81
