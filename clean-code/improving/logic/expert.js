/**
 * converts a number to a string for accounting
 * @param {Number} number
 * @returns {String}
 */
const numberToAccountingString = (number) => {
  if (number == null) throw new Error('Input is not a number')
  if (number < 0) return `(${Math.abs(number)})`
  return number.toString()
}

// test cases
console.log(numberToAccountingString(undefined))
console.log(numberToAccountingString(0))
console.log(numberToAccountingString(10))
console.log(numberToAccountingString(-5))
