import React, {useContext} from 'react';
import { GlobalContext } from '../context/GlobalState';
import { numberWithCommas } from '../utils/format';

export const Expense = ({ expense }) => {
  const { deleteExpense } = useContext(GlobalContext);

  // const sign = expense.costo < 0 ? '-' : '+';

  return (
    <li >
      {expense.name}<span>${numberWithCommas(Math.abs(expense.costo))}</span>
      <button onClick={() => deleteExpense(expense.expense_id)} className="delete-btn">x</button>
    </li>
  )
}