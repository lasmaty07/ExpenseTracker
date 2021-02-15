import React, { createContext, useReducer } from 'react';
import AppReducer from './AppReducer';
import axios from 'axios';

// Initial state
const initialState = {
  expenses: [],
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
        payload: res.data
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

  return (<GlobalContext.Provider value={{
    expenses: state.expenses,
    error: state.error,
    loading: state.loading,
    getExpense,
    deleteExpense,
    addExpense
  }}>
    {children}
  </GlobalContext.Provider>);
}