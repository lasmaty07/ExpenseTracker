import React, {useState, useContext} from 'react'
import { GlobalContext } from '../context/GlobalState';

export const AddExpense = () => {
  const [expense_name, setName] = useState('');
  const [desc, setDesc] = useState('');
  const [pagador, setPagador] = useState('');
  const [personas, setPersonas] = useState('');
  const [fecha, setFecha] = useState('');
  const [costo, setCosto] = useState(0);

  const { addExpense } = useContext(GlobalContext);

  const onSubmit = e => {
    e.preventDefault();

    const newExpense = {
      expense_name,
      desc,
      pagador,
      personas,
      fecha,
      costo: +costo
    }

    addExpense(newExpense);
  }

  return (
    <>
      <h3>Add new expense</h3>
      <form onSubmit={onSubmit}>
        <div className="form-control">
          <label htmlFor="amount">Gasto</label>
          <input type="text" value={expense_name} onChange={(e) => setName(e.target.value)} placeholder="Nombre gasto" />
          <input type="text" value={desc} onChange={(e) => setDesc(e.target.value)} placeholder="Descripción gasto" />       
          <input type="date" value={fecha} onChange={(e) => setFecha(e.target.value)} placeholder="Fecha" />       
          <input type="text" value={pagador} onChange={(e) => setPagador(e.target.value)} placeholder="Pagado por" />
          <input type="number" value={costo} onChange={(e) => setCosto(e.target.value)} placeholder="Monto" />
          <input type="text" value={personas} onChange={(e) => setPersonas(e.target.value.split(','))} placeholder="Personas (separado por coma)" />
        </div>
        <button className="btn">Agregar gasto</button>
      </form>
    </>
  )
}