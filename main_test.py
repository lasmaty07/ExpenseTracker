from datetime import date
import unittest

from model.person import *
from model.expense import *


class TestPerson(unittest.TestCase):
    def test_invalid_creation(self):
        with self.assertRaises(Exception) as context:
            Person("Matt", "30/12/2022", "10/10/2021")

        self.assertTrue(
            "El egreso no puede ser anterior al ingreso" in str(context.exception)
        )

    def test_valid_creation(self):
        name = "Matt"
        date1 = "30/12/2018"
        date2 = "10/10/2021"
        p = Person(name, date1, date2)
        self.assertIsInstance(p, Person)
        self.assertEqual(p.name, name)
        self.assertEqual(p.ingreso, date1)
        self.assertEqual(p.salida, date2)
        self.assertEqual(p.saldo, 0, "this should be zero")

    def test_sum_saldo(self):
        p = Person("Matt", "30/12/2018", "10/10/2021")
        p.addExpense(30)
        self.assertEqual(p.saldo, 30)
        p.addExpense(10)
        self.assertEqual(p.saldo, 40)


class TestExpense(unittest.TestCase):
    def test_expense_creation(self):
        name = "Cena"
        desc = "cena"
        costo = 500
        fecha = "25/07/2021"
        personas = {"matt"}
        pagadores = [{"name": "nico", "importe": 100}, {"name": "matt", "importe": 400}]
        e = Expense(name, desc, costo, fecha, personas, pagadores)
        self.assertIsInstance(e, Expense)

    def test_expense_error_sum(self):
        name = "Cena"
        desc = "cena"
        costo = 300
        fecha = "25/07/2021"
        personas = {"matt"}
        pagadores = [{"name": "nico", "importe": 100}, {"name": "matt", "importe": 400}]

        with self.assertRaises(Exception) as context:
            Expense(name, desc, costo, fecha, personas, pagadores)

        self.assertTrue(
            "Error: la sumatoria de los gatos individuales debe sumar el total"
            in str(context.exception)
        )

    def test_expense_error_costo(self):
        name = "Cena"
        desc = "cena"
        costo = 0
        fecha = "25/07/2021"
        personas = {"matt"}
        pagadores = [{"name": "nico", "importe": 100}, {"name": "matt", "importe": 400}]

        with self.assertRaises(Exception) as context:
            Expense(name, desc, costo, fecha, personas, pagadores)

        self.assertTrue(
            "Error: el costo del gasto debe ser mayor a cero" in str(context.exception)
        )

    def test_expense_error_pagador(self):
        name = "Cena"
        desc = "cena"
        costo = 500
        fecha = "25/07/2021"
        personas = {"Matt"}
        pagadores = []

        with self.assertRaises(Exception) as context:
            Expense(name, desc, costo, fecha, personas, pagadores)

        self.assertTrue(
            "Error: El gasto no puede no tener quien pagó" in str(context.exception)
        )

    def test_expense_error_persona(self):
        name = "Cena"
        desc = "cena"
        costo = 500
        fecha = "25/07/2021"
        personas = {}
        pagadores = [{"name": "nico", "importe": 100}, {"name": "matt", "importe": 400}]

        with self.assertRaises(Exception) as context:
            Expense(name, desc, costo, fecha, personas, pagadores)

        self.assertTrue(
            "Error: El gasto no puedeno aplicar a nadie" in str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
