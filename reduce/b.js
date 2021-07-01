const users = [
  { name: 'Joe', id: '1', registered: true },
  { name: 'Nancy', id: '2', registered: false },
  { name: 'Mary', id: '3', registered: true },
]

// Combining filter and map

// const namesOfRegisteredUsers = users
//   .filter((user) => user.registered)
//   .map((user) => user.name)

const namesOfRegisteredUsers = users.reduce(
  (names, user) => (user.registered ? [...names, user.name] : names),
  []
)

console.log(namesOfRegisteredUsers)
