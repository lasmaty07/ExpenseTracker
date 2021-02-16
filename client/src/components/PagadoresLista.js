import React, { useState } from "react";
import { GlobalContext } from '../context/GlobalState';

export const Pagadores = () =>{
  const [inputList, setInputList] = useState([{ name: "", importe: "" }]);

  const handleInputChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...inputList];
    list[index][name] = value;
    setInputList(list);
  };
   
  // handle click event of the Remove button
  const handleRemoveClick = index => {
    const list = [...inputList];
    list.splice(index, 1);
    setInputList(list);
  };
   
  // handle click event of the Add button
  const handleAddClick = () => {
    setInputList([...inputList, { name: "", importe: "" }]);
  };

  return (
    <div>    
      {inputList.map((x, i) => {
        return (
          <div className="box">
            <input
              name="name"
              type="text-short"
              value={x.name}
              onChange={e => handleInputChange(e, i)}
            />
            <input
              className="ml10"
              name="importe"
              type="number-short"
              value={x.importe}
              onChange={e => handleInputChange(e, i)}
            />
            <div className="btn-box">
              {inputList.length !== 1 && <button className="delete-btn" onClick={() => handleRemoveClick(i)}>Remove</button>}
              {inputList.length - 1 === i && <button onClick={handleAddClick}>Add</button>}
            </div>
          </div>
        );
      })}
    </div>
  );
}