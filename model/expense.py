from model.person import Person
import utils

class Expense:
  def __init__(self, name, desc, costo, fecha, personas,pagadores):
    #utils.dateValid(fecha)
    if not(int(costo) > 0 ):
      raise Exception('Error: el costo del gasto debe ser mayor a cero')

    if not(pagadores):
      raise Exception('Error: El gasto no puede no tener quien pagó')

    sumatoria = 0  
    listaPagadores = list(pagadores) 
    for pagador in listaPagadores:
      sumatoria += int(pagador['importe'])

    if int(costo)!= sumatoria:
      raise Exception('Error: la sumatoria de los gatos individuales debe sumar el total')

    self.name = name
    self.desc = desc
    self.costo = int(costo)
    self.fecha = fecha 
    self.personas = personas
    self.pagadores = pagadores