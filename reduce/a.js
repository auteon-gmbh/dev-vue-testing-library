const numbers = [1, 2, 3, 4]

// const sumOfNumbers = numbers.reduce((sum, currentNumber) => {
//   // console.log('sum', sum)
//   // console.log('currentNumber', currentNumber)
//   return sum + currentNumber
// }, 0)

// console.log('sumOfNumbers=', sumOfNumbers)

let sumOfNumbers = 0

numbers.forEach((number) => {
  sumOfNumbers += number
})

console.log(sumOfNumbers)
