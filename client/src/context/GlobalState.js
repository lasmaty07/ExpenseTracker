import React, { createContext, useReducer } from 'react';
import AppReducer from './AppReducer';
import axios from 'axios';

// Initial state
const initialState = {
  expenses: [],
  persons: [],
  error: null,
  loading: true
}

// Create context
export const GlobalContext = createContext(initialState);

// Provider component
export const GlobalProvider = ({ children }) => {
  const [state, dispatch] = useReducer(AppReducer, initialState);

  // Actions
  async function getExpense() {
    try {
      const res = await axios.get('/api/v1/expense');

      dispatch({
        type: 'GET_EXPENSES',
        payload: res.data.expenses
      });
    } catch (err) {
      dispatch({
        type: 'EXPENSE_ERROR',
        payload: err.response.status
      });
    }
  }

  async function deleteExpense(id) {
    try {
      await axios.delete(`/api/v1/expense/${id}`);

      dispatch({
        type: 'DELETE_EXPENSE',
        payload: id
      });
    } catch (err) {
      dispatch({
        type: 'EXPENSE_ERROR',
        payload: err.response.status
      });
    }
  }

  async function addExpense(expense) {
    const config = {
      headers: {
        'Content-Type': 'application/json'
      }
    }

    try {
      const res = await axios.post('/api/v1/expense', expense, config);

      dispatch({
        type: 'ADD_EXPENSE',
        payload: res.data
      });
    } catch (err) {
      dispatch({
        type: 'EXPENSE_ERROR',
        payload: err.response.status
      });
    }
  }

  async function getAmounts() {
    try {
      const res = await axios.get('/api/v1/amount');

      dispatch({
        type: 'GET_AMOUNTS',
        payload: res.data.amounts
      });
    } catch (err) {
      dispatch({
        type: 'AMOUNT_ERROR',
        payload: err.response.status
      });
    }
  }

  return (<GlobalContext.Provider value={{
    expenses: state.expenses,
    persons: state.persons,
    error: state.error,
    loading: state.loading,
    getExpense,
    deleteExpense,
    addExpense,
    getAmounts
  }}>
    {children}
  </GlobalContext.Provider>);
}