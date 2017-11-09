from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/BME590Lecture22")


class User(MongoModel):
    #  email = fields.EmailField(primary_key=True)
    #  first_name = fields.CharField()
    #  last_name = fields.CharField()
    name = fields.CharField()
    age = fields.IntegerField()
    bmi = fields.FloatField()


u1 = User(name='Sonali', age='24', bmi='fit')

u.save()