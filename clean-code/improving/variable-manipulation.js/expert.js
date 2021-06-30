function calculateTotal(items, options) {
  let total = items.reduce((total, current, index) => {
    return (total += current.price * current.quantity)
  }, 0)
  total = total - total * (options.discount || 0)
  total = total * 1.1
  total = total + (options.shipment || 5)
  return total
}

const testItems = [
  { price: 15, quan: 2 },
  { price: 20, quan: 1 },
  { price: 5, quan: 4 },
]

// console.log(calculateTotal())
// console.log(calculateTotal(testItems))
// console.log(calculateTotal(undefined, {}))
console.log(calculateTotal([], {}))
console.log(calculateTotal(testItems, {}))
console.log(calculateTotal(testItems, { shipment: 0 }))
console.log(calculateTotal(testItems, { discount: 0.75 }))
console.log(calculateTotal(testItems, { shipment: 12 }))
