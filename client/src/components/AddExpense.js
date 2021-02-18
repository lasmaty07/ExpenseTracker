import React, {useState, useContext, useEffect} from 'react'
import { GlobalContext } from '../context/GlobalState';
import { toast } from 'react-toastify';


export const AddExpense = () => {
  const [expense_name, setName] = useState('');
  const [desc, setDesc] = useState('');
  const [personas, setPersonas] = useState('');
  const [fecha, setFecha] = useState('');
  const [costo, setCosto] = useState(0);
  const [pagadores, setPagadores] = useState([{ name: "", importe: "" }]);
  //const [errors, setErrors] = useState([{ expense_name: "", desc: "", personas: "", fecha: "", costo: "", pagadores: "" }]);
  const [errors, setErrors] = useState('');

  const { addExpense, error} = useContext(GlobalContext);

  const validateForm = errors => {
    let valid = true;
    Object.values(errors).forEach(val => val.length > 0 && (valid = false));
    return valid;
  };
  
  const handleChange = (e) => {
    e.preventDefault();
    const { name, value } = e.target;

    switch (name) {
      case 'expense_name': 
        if (value.length == 0) {setErrors([{ expense_name: "El nombre del gasto no puede ser vacio" }]);}
        setName(value)
        break;    
      case 'desc': 
        if (value.length == 0) {setErrors([{ desc: "El nombre del gasto no puede ser vacio" }]); }
        setDesc(value)
        break;
      case 'personas': 
        if (value.length == 0) {setErrors([{ personas: "El nombre del gasto no puede ser vacio" }]); }
        setPersonas(value.split(','))
        break;
      case 'fecha': 
        if (value.length == 0) {setErrors([{ fecha: "El nombre del gasto no puede ser vacio" }]); }
        setFecha(value)
        break;
      case 'costo': 
        if (value <= 0 ) {setErrors([{ costo: "El nombre del gasto no puede ser vacio" }]); }
        setCosto(value)
        break;
      case 'pagadores': 
        if (value.length == 0 ) {setErrors([{ pagadores: "El nombre del gasto no puede ser vacio" }]); }
        break;
      default:
        break;
    }
  }
 
  function onSubmit (e) {
    e.preventDefault();

    
    const newExpense = {
      expense_name,
      desc,
      pagadores: pagadores,
      personas,
      fecha,
      costo: +costo
    }

    if(validateForm(errors)) {
      addExpense(newExpense);

    
      console.log('Error: ' + error);
      setName('');
      setDesc('');
      setPersonas('');
      setFecha('');
      setCosto('');
      setPagadores([{ name: "", importe: "" }]);
    } else  {
      console.error('Invalid Form')
    }
  }


  const handleInputChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...pagadores];
    list[index][name] = value;
    setPagadores(list);
  };
   
  const handleRemoveClick = index => {
    const list = [...pagadores];
    list.splice(index, 1);
    setPagadores(list);
  };
   
  const handleAddClick = () => {
    setPagadores([...pagadores, { name: "", importe: "" }]);
  };

  return (
    <>
      <h3>Agregar nuevo gasto</h3>
      <form onSubmit={onSubmit}>
        <div className="form-control">
          <label htmlFor="amount">Gasto</label>
          <input type="text" name='expense_name' value={expense_name} onChange={(e) => handleChange(e)} placeholder="Nombre gasto" />   
          {errors.length > 0 && <span className='error'>{errors.length}</span>}
          <input type="text" name='desc' value={desc} onChange={(e) => handleChange(e)} placeholder="Descripción gasto" />     
          <input type="date" name='fecha' value={fecha} onChange={(e) => handleChange(e)} placeholder="Fecha" />
          <input type="number" name='costo' value={costo} onChange={(e) => handleChange(e)} placeholder="Monto" />
          <input type="text" name='personas' value={personas} onChange={(e) => handleChange(e)} placeholder="Personas (separado por coma)" />
          <label htmlFor="">Pagaron</label>
          <div>
            {pagadores.map((x, i) => {
              return (
                <div className="box">
                  <input name="name" type="text-short" value={x.name} onChange={e => handleInputChange(e, i)} />
                  <input name="importe" type="number-short" value={x.importe} onChange={e => handleInputChange(e, i)}/> 
                    {pagadores.length !== 1 && <button className="delete-btn" onClick={() => handleRemoveClick(i)}>X</button>}
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