class DemoClass:
    """ in this class let us create a method n vairable n see how can we access them using an object
    """
    a=10

    def sum(self):
        print("helo sample program")

#  his is an object creation , obj= classname()
object= DemoClass()

# objname. desired methid we can call it
print(object.a)
object.sum()