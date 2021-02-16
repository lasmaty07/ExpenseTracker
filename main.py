import logging, json, datetime, time,os
from pathlib import Path
from utils import dateValid
from dotenv import load_dotenv
from flask import Flask,abort
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from model.person import Person
from model.expense import Expense
from bson.objectid import ObjectId

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / 'config.env'
load_dotenv(envars)

LOG_FILENAME = 'ExpenseTracker.log'
LOG_LEVEL=logging.INFO

logging.basicConfig(filename=LOG_FILENAME,level=LOG_LEVEL)

app = Flask(__name__)
app.config['ENV'] = 'Dev'
app.config["MONGO_URI"] = os.getenv("DEV_MONGO_URL_CLUSTER")

mongo = PyMongo(app)

#All the routings in our app will be mentioned here.
@app.route('/api/v1/test', methods=['GET'])
def testapi():
  return {'result' : 'ok'}

@app.route('/api/v1/person', methods=['POST'])
def add_person():
  expenseTracker = mongo.db.persons
  person = Person(request.json['name'], request.json['ingreso'] ,request.json['salida'])
  s = expenseTracker.find_one({'name' : person.name})
  if not(s):
    person_id = expenseTracker.insert({'name': person.name, 'ingreso': person.ingreso, 'salida': person.salida,'saldo':person.saldo})
    new_person = expenseTracker.find_one({'_id': person_id })
    output = {'person_id':str(person_id),'name':new_person['name'], 'ingreso'  : new_person['ingreso'], 'salida' : new_person['salida'], 'saldo': new_person['saldo']}
  else:
    abort(409, description="Duplicate person found")
  return output

@app.route('/api/v1/person/<name>', methods=['GET'])
def get_one_person(name):
  expenseTracker = mongo.db.persons
  s = expenseTracker.find_one({'name' : name})
  if s:
    expenseTracker.delete_one({'name' : name})
  else:
    abort(404, description="Person not found")
  return ''

@app.route('/api/v1/person/<name>', methods=['DELETE'])
def delete_one_person(name):
  expenseTracker = mongo.db.persons
  s = expenseTracker.find_one({'name' : name})
  if s:
    output = {'person_id':str(s['_id']),'name' : s['name'], 'ingreso' : s['ingreso'], 'salida' : s['salida'] }
  else:
    abort(404, description="Person not found")
  return output

@app.route('/api/v1/expense', methods=['POST'])
def add_expense():
  expenseTracker = mongo.db
  
  expense = Expense(request.json['expense_name'], request.json['desc'] ,request.json['costo'],
                    request.json['fecha'],request.json['personas'],request.json['pagadores'])
  
  for pagador in expense.pagadores:
    person = expenseTracker.persons.find_one({'name': pagador['name'] })  
    saldoAux = int(person['saldo']) + int(pagador['importe'])
    expenseTracker.persons.update_one({'name': pagador['name'] },{"$set": {'saldo':saldoAux}})

  expense_id = expenseTracker.expenses.insert({'name': expense.name, 'desc': expense.desc, 'costo': expense.costo, 'fecha': expense.fecha, 'pagadores': expense.pagadores, 'personas': expense.personas})
  
  new_expense = expenseTracker.expenses.find_one({'_id': expense_id })
  output = {'expense_id':str(expense_id),'name':new_expense['name'],  'desc': new_expense['desc'], 'costo': new_expense['costo'], 'fecha': new_expense['fecha'],'pagadores': new_expense['pagadores'], 'personas': new_expense['personas']}
  return output

@app.route('/api/v1/expense/<id>', methods=['GET'])
def get_one_expense(id):
  expenseTracker = mongo.db.expenses
  s = expenseTracker.find_one({'_id' : ObjectId(id)})
  if s:
    output = {'expense': {'expense_id':str(s['_id']),'name' : s['name'], 'desc' : s['desc'], 'costo' : s['costo'] ,'fecha': s['fecha'], 'personas': s['personas']}}
  else:
    abort(404, description="Expense not found")
  return output

@app.route('/api/v1/expense', methods=['GET'])
def get_expenses():
  expenseTracker = mongo.db.expenses
  output = []
  for s in expenseTracker.find():
    output.append({'expense_id':str(s['_id']),'name' : s['name'], 'desc' : s['desc'], 'costo' : s['costo'] ,'fecha': s['fecha'], 'personas': s['personas']})
  return jsonify({ 'expenses' : output })

@app.route('/api/v1/expense/<id>', methods=['DELETE'])
def delete_one_expense(id):
  expenseTracker = mongo.db
  e = expenseTracker.expenses.find_one_and_delete({'_id' : ObjectId(id)})
  if e:
    for p in e['pagadores']:
      person = expenseTracker.persons.find_one({'name': p['name'] })  
      saldoAux = int(person['saldo']) - int(p['importe'])
      expenseTracker.persons.update_one({'name': p['name'] },{"$set": {'saldo':saldoAux}})
    output = ''
  else:
    abort(404, description="Expense not found")
  return output

@app.route('/api/v1/amount/<name>', methods=['GET'])
def get_person_amounts(name):
  expenseTracker = mongo.db
  p = expenseTracker.persons.find_one({'name' : name})
  owes = 0
  for e in expenseTracker.expenses.find({'personas' : name}):
    owes += e['costo']/len(e['personas'])
    
  if p:
    total_balance = owes - p['saldo'] 
    output = {'name': name, 'paid': p['saldo'], 'owes': owes, 'total_balance':total_balance }
  else:
    abort(404, description="Person not found")
  return output

@app.route('/api/v1/amount', methods=['GET'])
def get_amounts():
  expenseTracker = mongo.db
  output = []
  for p in expenseTracker.persons.find():
    owes = 0
    for e in expenseTracker.expenses.find({'personas' : p['name']}):
      owes += e['costo']/len(e['personas'])
      
    total_balance = owes - p['saldo'] 
      
    output.append({'name': p['name'],'owes': owes,'paid': p['saldo'],'total_balance':total_balance})
  return jsonify({ 'amounts' : output })
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)