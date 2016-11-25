#! /usr/bin/env python

# playing with classes


## inheritance example


class SchoolMember(object):
    """Represents any school member."""
    def __init__(self, name, age):                    # constructor
        self.name = name
        self.age = age
        print '   (SchoolMember Initialized: %s)' % self.name
    
    def __repr__(self):
        return "%s" % self.name
    
    def initialize(self):
        print '(Initialized SchoolMember: %s)' % self.name
    
    def tellme(self):
        """Tell my details."""
        print 'Name: %s   Age: %s   ' % (self.name, self.age),


## you pretty much ignore SchoolMember attribute of the class here.

class Teacher(SchoolMember):
    """Represents a teacher."""
    
    def __init__(self, name, age, salary):            # constructor
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        # SchoolMember.initialize(self)
        print '(Initialized Teacher: %s)' % self.name
    
    def __repr__(self):
        return "%s" % self.name
    
    def tellme(self):
        SchoolMember.tellme(self)
        print 'Salary: %d' % self.salary


class Student(SchoolMember):
    """Represents a student."""
    
    def __init__(self, name, age, marks):            # constructor
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        # SchoolMember.initialize(self)
        print '(Initialized Student: %s)' % self.name
    
    def __repr__(self):
        return "%s" % self.name
    
    def tellme(self):
        SchoolMember.tellme(self)
        print 'Marks: %d' % self.marks


t = Teacher('Mr. Wilson', 32, 12000)
s = Student('Zander', 6, 75)
m = SchoolMember('Bigglesworth', 8)
print
members = [t, s, m]
for member in members:
    member.tellme() # works for both Teachers and Students

pass
