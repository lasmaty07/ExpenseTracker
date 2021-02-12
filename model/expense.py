import utils

class Expense:
  def __init__(self, name, desc, costo, fecha, personas,pagador):
    utils.dateValid(fecha)
    if not(int(costo) > 0 ):
      raise Exception('Error: el costo del gasto debe ser mayor a cero')

    if not(pagador):
      raise Exception('Error: El gasto no puede no tener quien pagó')

    self.name = name
    self.desc = desc
    self.costo = int(costo)
    self.fecha = fecha 
    self.personas = personas
    self.pagador = pagador