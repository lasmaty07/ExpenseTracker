from utils import dateValid

class Person:
  def __init__(self, name, ingreso, salida):
    self.name = name
    self.ingreso = ingreso
    self.salida = salida
    dateValid(ingreso)
    dateValid(salida)

