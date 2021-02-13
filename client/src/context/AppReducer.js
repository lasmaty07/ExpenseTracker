export default (state, action) => {
  switch(action.type) {
    case 'GET_EXPENSES':
      return {
        ...state,
        loading: false,
        transactions: action.payload
      }
    case 'DELETE_EXPENSE':
      return {
        ...state,
        transactions: state.transactions.filter(transaction => transaction._id !== action.payload)
      }
    case 'ADD_EXPENSE':
      return {
        ...state,
        transactions: [...state.transactions, action.payload]
      }
    case 'TRANSACTION_ERROR':
      return {
        ...state,
        error: action.payload
      }
    default:
      return state;
  }
}