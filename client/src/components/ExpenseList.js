import React, { useContext, useEffect } from 'react';
import { Expense } from './Expense';

import { GlobalContext } from '../context/GlobalState';

export const ExpenseList = () => {
  const { expenses, getExpense } = useContext(GlobalContext);

  useEffect(() => {
    getExpense();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <h3>Gastos</h3>
      <ul className="list">
        {expenses.map(expense => (<Expense key={expense._id} expense={expense} />))}
      </ul>
    </>
  )
}
