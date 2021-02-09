import utils

class Person:
  def __init__(self, name, ingreso, salida):
    self.name = name
    self.ingreso = ingreso
    self.salida = salida
    utils.dateValid(ingreso)
    utils.dateValid(salida)
    if firstDateGreater(ingreso)
      raise 'El egreso no puede ser anterior al ingreso'

