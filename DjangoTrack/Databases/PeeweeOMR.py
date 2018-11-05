"""
ORM -> Object Relation Mapping
Turns objects in your code into rows in a database and vice versa.

Peewee is a light weight ORM for Python

"""

from peewee import * #Convension to import everything from peewee

db = SqliteDatabase('students.db') #Connecting to a database students.db, which we create when running db.connect()


class Student(Model): #This object represents a database table | We also extends Model from peewee to make this model
    username = CharField(max_length = 255, unique =True)
    points = IntegerField(default = 0)
    
    class Meta: 
      database = db


students = [
  {'username':'Hanna', 
  'points':345234},
  {'username':'Emma', 
  'points':34},
  {'username':'GroBente', 
  'points':3454},
  {'username':'Henning', 
  'points':3454},
  
]

def add_students():
  for student in students:
    try:
      Student.create(username = student['username'],
                       points = student['points'])
      
    except IntegrityError:  #Because of the unique atrribute in our student class
      student_record = Student.get(username=student['username'])
      student_record.points = student['points']
      student_record.save()
      

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student
      
if __name__ == '__main__':
  db.connect()
  db.create_tables([Student], safe = True)
  add_students()
  print("Our top student right now is: {0.username}.".format(top_student()))
  #Safe determines wether or not to throw errors if the table(s) you'r attempting to create already exist
  

  """
  .create() -> creates a new instance all at once
  .select() -> finds records in a table
  .save() -> updates an existing row in the database
  .get() -> finds a single record in a table
  .delete_instance() -> deletes a single record from the table
  .order_by() -> specifies how to sort the records
  if__name__ == '__main__' -> a common pattern for making code only run when the script is run and not when it's imported
  db.close() -> Explicitly closes the connection to the database
  .update() -> Offers a way to update a record without .get() and .save()
  
  
  CRUD -> Create, Read, Update, Delete
  
  """