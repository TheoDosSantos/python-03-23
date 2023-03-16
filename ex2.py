import json

class Person(object):
    def __init__(self, firstname, lastname, age, gender, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.job = job

    def get_firstname(self):
        return self.firstname
        # Return first name

    def set_firstname(self, u):
        self.firstname = u
        # Update first name, u must be a string

    def get_lastname(self):
        return self.lastname
        # Return last name

    def set_lastname(self, u):
        self.lastname = u
        # Update last name, u must be a string

    def get_age(self):
        return self.age
        # Return age

    def set_age(self, u):
        self.age = u
        # Update age, u must be an integer number

    def get_gender(self):
        return self.gender
        # Return gender

    def set_gender(self, u):
        self.gender = u
        # Update gender, u must be a string

    def get_job(self):
        return self.job
        # Return job

    def set_job(self, u):
        self.job = u
        # Update job, u must be a string

    def get_infos(self):
        return json.dumps({'First name' : self.firstname, 'Last name' : self.lastname, 'Age' : self.age, 'Gender' : self.gender, 'Job' : self.job}, indent=3)
        # Return a JSON Object literal with all datas set

person_1 = Person('Theo', 'DOS SANTOS', 23, 'Man', 'Web developer')
# To instance this class :
#   firsname me be a string
#   lastname me be a string
#   age me be a integer number
#   gender me be a string
#   job me be a string

print(person_1.get_infos())
# Displaying the JSON Object
