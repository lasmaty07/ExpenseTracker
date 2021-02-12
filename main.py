import logging, json, datetime, time,os
from pathlib import Path
from utils import dateValid
from dotenv import load_dotenv,dotenv_values
from flask import Flask,abort
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from model.person import Person
from model.expense import Expense

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

@app.route('/person', methods=['POST'])
def add_person():
  expenseTracker = mongo.db.persons
  person = Person(request.json['name'], request.json['ingreso'] ,request.json['salida'])
  s = expenseTracker.find_one({'name' : person.name})
  if not(s):
    person_id = expenseTracker.insert({'name': person.name, 'ingreso': person.ingreso, 'salida': person.salida})
    new_person = expenseTracker.find_one({'_id': person_id })
    output = {'person_id':str(person_id),'name':new_person['name'], 'ingreso'  : new_person['ingreso'], 'salida' : new_person['salida']}
  else:
    abort(409, description="Duplicate person found")
  return output

@app.route('/person/<name>', methods=['GET'])
def get_one_person(name):
  expenseTracker = mongo.db.persons
  s = expenseTracker.find_one({'name' : name})
  if s:
    expenseTracker.delete_one({'name' : name})
  else:
    abort(404, description="Person not found")
  return output

@app.route('/person/<name>', methods=['DELETE'])
def get_one_person(name):
  expenseTracker = mongo.db.persons
  s = expenseTracker.find_one({'name' : name})
  if s:
    output = {'person_id':str(s['_id']),'name' : s['name'], 'ingreso' : s['ingreso'], 'salida' : s['salida'] }
  else:
    abort(404, description="Person not found")
  return output

@app.route('/expense', methods=['POST'])
def add_expense():
  expenseTracker = mongo.db
  expense = Expense(request.json['name'], request.json['desc'] ,request.json['costo'],request.json['fecha'],request.json['personas'],request.json['pagador'])
  person = expenseTracker.persons.find_one({'name': expense.pagador })
  expenseTracker.persons.update_one({'name': expense.pagador },{"$set": {'saldo':person['saldo']}})
  expense_id = expenseTracker.expenses.insert({'name': expense.name, 'desc': expense.desc, 'costo': expense.costo, 'fecha': expense.fecha, 'personas': expense.personas})
  saldoAux = int(person['saldo']) + int(expense.costo)
  expenseTracker.persons.update_one({'name': expense.pagador },{"$set": {'saldo':saldoAux}})

  new_expense = expenseTracker.expenses.find_one({'_id': expense_id })
  output = {'expense_id':str(expense_id),'name':new_expense['name'],  'desc': new_expense['desc'], 'costo': new_expense['costo'], 'fecha': new_expense['fecha'], 'personas': new_expense['personas']}
  return output

@app.route('/expense/<name>', methods=['GET'])
def get_one_expense(name):
  expenseTracker = mongo.db.expenses
  s = expenseTracker.find_one({'name' : name})
  if s:
    output = {'expense_id':str(s['_id']),'name' : s['name'], 'desc' : s['desc'], 'costo' : s['costo'] ,'fecha': s['fecha'], 'personas': s['personas']}
  else:
    abort(404, description="Expense not found")
  return output

@app.route('/expense/<name>', methods=['DELETE'])
def delete_one_expense(name):
  expenseTracker = mongo.db.expenses
  s = expenseTracker.find_one({'name' : name})
  if s:
    expenseTracker.delete_one({'name' : name})
  else:
    abort(404, description="Expense not found")
  return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)