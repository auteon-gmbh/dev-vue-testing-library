const pipe =
  (...funcs) =>
  (input) =>
    funcs.reduce((accumulator, func) => func(accumulator), input)

const users = [
  { name: 'Joe', id: '1', registered: true, age: 30 },
  { name: 'Nancy', id: '2', registered: false, age: 35 },
  { name: 'Mary', id: '3', registered: true, age: 90 },
]

const getRegisteredUsers = (users) => users.filter((user) => user.registered)
const getSeniorUsers = (users) => users.filter((user) => user.age > 65)
const getNamesOfUsers = (users) => users.map((user) => user.name)

const getSeniorRegisteredUsers = pipe(getRegisteredUsers, getSeniorUsers)

// console.log(getSeniorRegisteredUsers(users))

const getNamesOfSeniorRegisteredUsers = pipe(
  getRegisteredUsers,
  getSeniorUsers,
  getNamesOfUsers
)

console.log(getNamesOfSeniorRegisteredUsers(users))
