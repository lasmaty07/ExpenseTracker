import React from 'react';
import { Header } from './components/Header';
import { AddExpense } from './components/AddExpense';
import { PersonList } from './components/PersonList';

import { GlobalProvider } from './context/GlobalState';

import './App.css';


function App() {
  return (
    <GlobalProvider>
      <Header />
      <div className="container">
        <PersonList />
        <AddExpense />
      </div>
    </GlobalProvider>
  );
}

export default App;
