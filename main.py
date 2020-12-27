import logging, json, datetime, time
from person import Person
from utils import dateValid

LOG_FILENAME = 'ExpenseTracker.log'
LOG_LEVEL=logging.INFO

logging.basicConfig(filename=LOG_FILENAME,level=LOG_LEVEL)

try:
  with open('config.json', 'r') as f:
    config = json.load(f)
except IOError as e:
	logging.error(e)

#INFLUXDB_USERNAME = secrets["user"]qwe

personas = set()
p = ''
print('Ingresar Nombre, Entrada y Salida (separado por comas):')
p = input()

while p != 'end':
  print('Ingresar Nombre, Entrada y Salida (separado por comas):')
  p = input()
  try: 
    personas.add(Person(p.split(',')[0],p.split(',')[1],p.split(',')[2]))
  except  Exception as e:
    logging.error(e)
    print(e)
print('fin carga personas')

print(personas)