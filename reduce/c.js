const { groupBy } = require('lodash')

// Expected Result:
// {
//     true: [
//       { name: 'Joe', id: '1', registered: true },
//       { name: 'Mary', id: '3', registered: true }
//     ],
//     false: [ { name: 'Nancy', id: '2', registered: false } ]
// }

const users = [
  { name: 'Joe', id: '1', registered: true },
  { name: 'Nancy', id: '2', registered: false },
  { name: 'Mary', id: '3', registered: true },
]

// console.log('grouped by lodash', groupBy(users, 'registered'))

function groupByNotLodash(arr, criteria) {
  return arr.reduce((grouped, currentElement) => {
    const groupingKey = currentElement[criteria]

    if (!grouped.hasOwnProperty(groupingKey)) {
      grouped[groupingKey] = []
    }

    grouped[groupingKey].push(currentElement)

    return grouped
  }, {})
}

console.log('groupByNotLodash', groupByNotLodash(users, 'registered'))
