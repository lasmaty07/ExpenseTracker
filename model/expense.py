import utils

class Expense:
  def __init__(self, name, desc, costo, fecha, personas):
    utils.dateValid(fecha)
    if not(int(costo) > 0 ):
      raise Exception('Error: el costo del gasto debe ser mayor a cero')

    self.name = name
    self.desc = desc
    self.costo = int(costo)
    self.fecha = fecha 
    self.personas = personas    