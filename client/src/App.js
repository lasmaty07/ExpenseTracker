import React from 'react';
import { Header } from './components/Header';
import { AddExpense } from './components/AddExpense';

import { GlobalProvider } from './context/GlobalState';

import './App.css';

function App() {
  return (
    <GlobalProvider>
      <Header />
      <div className="container">
        <AddExpense />
      </div>
    </GlobalProvider>
  );
}

export default App;
