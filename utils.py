import datetime

def dateValid(date_text):
  try:
    datetime.datetime.strptime(date_text, '%d/%m/%Y')
  except ValueError:
    raise ValueError("Incorrect data format, should be DD/MM/YYYY")

def firstDateGreater(d1,d2):
  d11 = datetime.datetime.strptime(d1, '%d/%m/%Y')
  d22 = datetime.datetime.strptime(d2, '%d/%m/%Y')
  return d11 > d22