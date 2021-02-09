import logging, json, datetime, time,os
from pathlib import Path
from utils import dateValid
from dotenv import load_dotenv,dotenv_values
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from model.person import Person

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / 'config.env'
load_dotenv(envars)

LOG_FILENAME = 'ExpenseTracker.log'
LOG_LEVEL=logging.INFO

logging.basicConfig(filename=LOG_FILENAME,level=LOG_LEVEL)

app = Flask(__name__)
app.config['ENV'] = 'Dev'
app.config["MONGO_URI"] = "mongodb://192.168.1.4:27017/expensetrackerdev"

mongo = PyMongo(app)

#All the routings in our app will be mentioned here.
@app.route('/test', methods=['GET'])
def testapi():
  return {'result' : 'ok'}

@app.route('/addPerson', methods=['POST'])
def add_person():
  expenseTracker = mongo.db.persons
  person = Person(request.json['name'], request.json['ingreso'] ,request.json['salida'])
  person_id = expenseTracker.insert({'name': person.name, 'ingreso': person.ingreso, 'salida': person.salida})
  new_person = expenseTracker.find_one({'_id': person_id })
  output = {'person_id':str(person_id),'name':new_person['name'], 'ingreso'  : new_person['ingreso'], 'salida' : new_person['salida']}
  return output

@app.route('/getPerson/<name>', methods=['GET'])
def get_one_person(name):
  expenseTracker = mongo.db.persons
  s = expenseTracker.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'ingreso' : s['ingreso'], 'salida' : s['salida'] }
  else:
    output = "No such person"
  return output


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)