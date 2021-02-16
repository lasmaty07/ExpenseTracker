import React, {useState, useContext} from 'react'
import { GlobalContext } from '../context/GlobalState';

export const AddExpense = () => {
  const [expense_name, setName] = useState('');
  const [desc, setDesc] = useState('');
  const [personas, setPersonas] = useState('');
  const [fecha, setFecha] = useState('');
  const [costo, setCosto] = useState(0);
  const [pagadores, setInputList] = useState([{ name: "", importe: "" }]);

  const { addExpense } = useContext(GlobalContext);

  const onSubmit = e => {
    e.preventDefault();

    const newExpense = {
      expense_name,
      desc,
      pagadores: pagadores,
      personas,
      fecha,
      costo: +costo
    }

    console.log(addExpense(newExpense));

    setName('');
    setDesc('');
    setPersonas('');
    setFecha('');
    setCosto('');
    setInputList([{ name: "", importe: "" }]);
  }

  const handleInputChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...pagadores];
    list[index][name] = value;
    setInputList(list);
  };
   
  // handle click event of the Remove button
  const handleRemoveClick = index => {
    const list = [...pagadores];
    list.splice(index, 1);
    setInputList(list);
  };
   
  // handle click event of the Add button
  const handleAddClick = () => {
    setInputList([...pagadores, { name: "", importe: "" }]);
  };

  return (
    <>
      <h3>Agregar nuevo gasto</h3>
      <form onSubmit={onSubmit}>
        <div className="form-control">
          <label htmlFor="amount">Gasto</label>
          <input type="text" value={expense_name} onChange={(e) => setName(e.target.value)} placeholder="Nombre gasto" />
          <input type="text" value={desc} onChange={(e) => setDesc(e.target.value)} placeholder="Descripción gasto" />       
          <input type="date" value={fecha} onChange={(e) => setFecha(e.target.value)} placeholder="Fecha" />       
          <input type="number" value={costo} onChange={(e) => setCosto(e.target.value)} placeholder="Monto" />
          <input type="text" value={personas} onChange={(e) => setPersonas(e.target.value.split(','))} placeholder="Personas (separado por coma)" />
          <label htmlFor="">Pagaron</label>
          <div>
            {pagadores.map((x, i) => {
              return (
                <div className="box">
                  <input
                    name="name"
                    type="text-short"
                    value={x.name}
                    onChange={e => handleInputChange(e, i)}
                  />
                  <input
                    name="importe"
                    type="number-short"
                    value={x.importe}
                    onChange={e => handleInputChange(e, i)}
                  /> {pagadores.length !== 1 && <button className="delete-btn" onClick={() => handleRemoveClick(i)}>X</button>}
                  <div className="btn-box">                    
                    {pagadores.length - 1 === i && <button className="add-btn" onClick={handleAddClick}>+</button>}
                  </div>
                </div>
              );
            })}
          </div>       
        </div>
        <button className="btn">Agregar gasto</button>
      </form>
    </>
  )
}