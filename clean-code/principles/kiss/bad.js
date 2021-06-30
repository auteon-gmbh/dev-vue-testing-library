// why is this considered to be "bad"?
const generateWeekday = (day) => {
  switch (day) {
    case 1:
      return 'Monday'
    case 2:
      return 'Tuesday'
    case 3:
      return 'Wednesday'
    case 4:
      return 'Thursday'
    case 5:
      return 'Friday'
    case 6:
      return 'Saturday'
    case 7:
      return 'Sunday'
    default:
      throw new Error('day must be in range 1 to 7')
  }
}