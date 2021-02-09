export function wrapAsList<T>(item: T): T[] {
  return [item]
}

const a = wrapAsList("a")
const b = wrapAsList(1)
const c = wrapAsList({ bar: "baz" })
