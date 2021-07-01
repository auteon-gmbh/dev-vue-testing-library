const registerdUsers = {
  1: true,
  2: false,
  3: true,
}
const users = [
  { name: 'Joe', id: '1' },
  { name: 'Nancy', id: '2' },
  { name: 'Mary', id: '3' },
]

const updatedRegisteredUsers = users.reduce((result, user) => {
  const isUserRegistered = registerdUsers[user.id]

  if (isUserRegistered) {
    return [...result, { ...user, registerd: true }]
  }

  return [...result, { ...user, registered: false }]
}, [])
