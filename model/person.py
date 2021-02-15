import utils

class Person:
  def __init__(self, name, ingreso, salida):
    utils.dateValid(ingreso)
    utils.dateValid(salida)
    if utils.firstDateGreater(ingreso,salida):
      raise Exception('El egreso no puede ser anterior al ingreso')   
    
    self.name = name
    self.ingreso = ingreso
    self.salida = salida
    self.saldo = 0
  
  def addExpense(self,importe):
    self.saldo += importe

