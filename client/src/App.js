import React from 'react';
import { Header } from './components/Header';
import { AddExpense } from './components/AddExpense';
import { PersonList } from './components/PersonList';
import { ExpenseList } from './components/ExpenseList';

import { GlobalProvider } from './context/GlobalState';

import './App.css';


function App() {
  return (
    <GlobalProvider>
      <Header />
      <div className="container">
        <PersonList />
        <ExpenseList />
        <AddExpense />
      </div>
    </GlobalProvider>
  );
}

export default App;
