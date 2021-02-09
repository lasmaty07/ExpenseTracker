import datetime

def dateValid(date_text):
  try:
    datetime.datetime.strptime(date_text, '%d/%m/%Y')
  except ValueError:
    raise ValueError("Incorrect data format, should be DD/MM/YYYY")

def firstDateGreater(d1,d2):
  return datetime.datetime(d1)>datetime.datetime(d2)
