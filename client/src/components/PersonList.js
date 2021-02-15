import React, { useContext, useEffect } from 'react';
import { Person } from './Person';

import { GlobalContext } from '../context/GlobalState';

export const PersonList = () => {
  const { persons, getAmounts } = useContext(GlobalContext);

  useEffect(() => {
    getAmounts();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <h3>Personas</h3>
      <ul className="list">
        {persons.map(person => (<Person key={person._id} person={person} />))}
      </ul>
    </>
  )
}
