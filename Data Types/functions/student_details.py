""" Using normal function """
""" This is positional arguments, have a correct positional order"""
def student(name,id,course,place):
    print("Student Details:",name,id,course,place)
student("silpa",12,"python","Malappuram")
print("_____________________________________")
"""Using arbitary Arguments"""
""" No: of arguments unknown """
""" Single * is used """
def names(*args):
    print("names:",args)
names('silpa','reethu','aruna')
print("______________________________________")
""" Using keyword Arguments"""
""" keyword arguments number is unknown"""
""" get it as dictionary formate """
""" ** is used"""
def students(**kwargs):
    print("student Details :",kwargs['name'],kwargs['id'],kwargs['course'])
students(name='silpa',id=12,course='python',place='malappuram')

print("________________________________________________")
""" Default parameter 
    Set value of parameter during function definition itself .in this case no need to pass arguments during
 function call"""
""" And also can set another value during function call"""
def country(country='india'):
    print("im from ", country)
country()
country('italy')
country('usa')