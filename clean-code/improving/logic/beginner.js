function numberToString(number) {
  // fehlerfälle abfangen

  if (number < 0) {
    return '(' + Math.abs(number) + ')'
  } else {
    // unnötig
    return number.toString()
  }
}

// test cases
console.log(toAccounting(undefined))
console.log(toAccounting(null))
console.log(toAccounting(0))
console.log(toAccounting(10))
console.log(toAccounting(-5))