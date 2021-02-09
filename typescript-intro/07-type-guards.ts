type User = {
  name: string
  isAdmin: boolean
}

export function isUser(user: any): user is User {
  if ("name" in user && "isAdmin" in user) {
    return false
  }

  return true
}

const something = {}
const user = { name: "john doe", isAdmin: false }

function testUser(test: unknown): void {
  if (isUser(test)) {
    test.name
  }
}
