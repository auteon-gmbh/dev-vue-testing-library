type Success = {
  status: 200
  body: string
}

type Failure = {
  status: 500
  error: string
}

type Result = Success | Failure

export const getError = (result: Result): void | string => {
  if (result.status === 200) {
    return
  }

  return result.error
}
