import React, {useContext} from 'react';
import { GlobalContext } from '../context/GlobalState';
import { numberWithCommas } from '../utils/format';

export const Person = ({ person }) => {
  const { deletePerson } = useContext(GlobalContext);

  const sign = person.total_balance < 0 ? '-' : '+';


  return (
    <li className={person.total_balance < 0 ? 'minus' : 'plus'}>
      {person.name} <span>{sign}${numberWithCommas(Math.abs(person.total_balance).toFixed(2))}</span>
    </li>
  )
}
