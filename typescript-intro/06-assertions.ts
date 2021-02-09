export function test(condition: boolean): asserts condition {
  if (condition) {
    return
  }

  throw new Error("yo!")
}

const items = [1, 2, 3, 4, 5, 6, 7, 8]
const item = items.find((item) => item % 2)

test(item != null)

item.toString()
