# -------------------------------------------------
# Wesley Smith
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# -------------------------------------------------
# This program uses classes to help advise a student
# from any major if they are having trouble in their
# major or in math. Can be used for multiple majors
# with the same basic requirements for each major
# (name, major name, etc.)
# -------------------------------------------------

# The generic class that gives initial values of false for math and major troubles
class Generic_Major:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.major = "Generic"
        self.math = False
        self.major_trbl = False

    # Grabs the first name
    def get_first_name(self):
        return self.first.capitalize()

    # Grabs the last name
    def get_last_name(self):
        return self.last.capitalize()

    # Returns the major given
    def get_major(self):
        return str(self.major)

    # Grabs the current status of the major troubles/ either true or false
    def get_major_troubles(self):
        return self.major_trbl
    
    # Grabs the state of math troubles/ true or false
    def get_math_troubles(self):
        return self.math

    # This function can overwrite the state of troubles to change it to True or False
    def set_major_troubles(self, condition):
        self.major_trbl = condition

    # Changes the troubles value to either True or False
    def set_math_troubles(self, condition):
        self.math = condition

    # The basic advising function for a general major if major troubles = True
    def major_advising(self):
        if self.get_major_troubles() == True:
            print("Because you are having troubles with your major:")
            print("--> Visit your professor during office hours")
            print("--> Visit your academic advisor")

    # The advising function for if they are having trouble in math
    # This function is used throughout the program in each class,
    # through inheritance
    def math_advising(self):
        if self.get_math_troubles() == True:
            print("Because you are having troubles with math:")
            print("--> Visit the Math Learning Center in Wilson 1-112")

# This is our new instance of the CLS Major class, which inherits values from the Generic Class
# Since the advice for this major is the same as the generic major, we don't
# need a new advising function
class CLS_Major(Generic_Major): # The inherited class is in the parenthesis
    def __init__(self, first, last):
        Generic_Major.__init__(self, first, last) # Inherits the first and last functions from generic
        self.major = "College of Letters and Sciences" # Changes the major to match our class

class COE_Major(Generic_Major):
    def __init__(self, first, last):
        Generic_Major.__init__(self, first, last)
        self.major = "College of Engineering"

    # Changes the advising function to fit the advice for the COE Major rather than the Generic Major
    def major_advising(self):
        if self.get_major_troubles() == True:
            print("Because you are having troubles with your major:")
            print("--> visit the EMPower Student Center in Roberts 313")
            print("--> Visit your professor during office hours")
            print("--> Visit your academic advisor")

# The Computer Engineering Major inherits the advising list from COE Major
# so we don't need to put in the major_advising function again
class Computer_Engineering_Major(COE_Major):
    def __init__(self, first, last):
        COE_Major.__init__(self, first, last)
        self.major = "Computer Engineering" # Changes major name

# Same as Computer Engineering, but Physics inherits from the CLS Major
# instead of the COE, and needs an additional advising option of Barnard Hall 230
class Physics_Major(CLS_Major):
    def __init__(self, first, last):
        CLS_Major.__init__(self, first, last)
        self.major = "Physics"

    def major_advising(self):
        if self.get_major_troubles() == True:
            print("Because you are having troubles with your major:")
            print("--> visit the Physics Learning Center in Barnard Hall 230")
            print("--> Visit your professor during office hours")
            print("--> Visit your academic advisor")

class Computer_Science_Major(COE_Major):
    def __init__(self, first, last):
        COE_Major.__init__(self, first, last)
        self.major = "Computer Science"

    def major_advising(self):
        if self.get_major_troubles() == True:
            print("Because you are having troubles with your major:")
            print("--> Visit the CS Student Success Center in Barnard Hall 259")
            print("--> Visit a CS professional advisor in Barnard Hall 357")
            print("--> visit the EMPower Student Center in Roberts 313")
            print("--> Visit your professor during office hours")
            print("--> Visit your academic advisor")

# -------------------------------------------------

def advise(student):
    print("Student: " + student.get_first_name() + " " + student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_math_troubles()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)


# -------------------------------------------------

main()
