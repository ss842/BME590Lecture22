from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask, request, jsonify

app = Flask(__name__)
connect("mongodb://localhost:27017/BME590Lecture22")


class User(MongoModel):
    #  email = fields.EmailField(primary_key=True)
    #  first_name = fields.CharField()
    #  last_name = fields.CharField()
    name = fields.CharField()
    age = fields.IntegerField()
    bmi = fields.FloatField()


# u1 = User(name='Sonali', age='24', bmi='fit')

# u.save()


@app.route("/api/new_patient", methods=['POST'])
def new_patient():
    p = request.json
    patient_name = p['name']
    patient_age = p['age']
    patient_bmi = p['bmi']

    u1 = User(name=patient_name[0], age=patient_age[0], bmi=patient_bmi[0])

    u1.save()

    return 'Successful!' 