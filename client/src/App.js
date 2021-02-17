import React from 'react';
import { Header } from './components/Header';
import { AddExpense } from './components/AddExpense';
import { PersonList } from './components/PersonList';
import { ExpenseList } from './components/ExpenseList';
import { ToastContainer } from 'react-toastify';

import { GlobalProvider } from './context/GlobalState';

//styles
import './App.css';
import 'react-toastify/dist/ReactToastify.css';


function App() {
  return (
    <GlobalProvider>
      <Header />
      <div className="container">
        <PersonList />
        <ExpenseList />
        <AddExpense />
        <ToastContainer />
      </div>
    </GlobalProvider>
  );
}

export default App;
