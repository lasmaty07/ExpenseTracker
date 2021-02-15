export default (state, action) => {
  switch(action.type) {
    case 'GET_EXPENSES':
      return {
        ...state,
        loading: false,
        expenses: action.payload
      }
    case 'DELETE_EXPENSE':
      return {
        ...state,
        expenses: state.expenses.filter(expense => expense._id !== action.payload)
      }
    case 'ADD_EXPENSE':
      return {
        ...state,
        expenses: [...state.expenses, action.payload]
      }
    case 'EXPENSE_ERROR':
      return {
        ...state,
        error: action.payload
      }
    default:
      return state;
  }
}