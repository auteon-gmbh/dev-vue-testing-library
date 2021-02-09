type WatchObject<T> = {
  on(eventName: `${string & keyof T}Change`): void
}

type User = {
  name: string
  birthday: Date
}

declare function makeWatched<T>(object: T): T & WatchObject<T>

export const user = makeWatched<User>({ name: "John", birthday: new Date() })

user.on("birthdayChange")
