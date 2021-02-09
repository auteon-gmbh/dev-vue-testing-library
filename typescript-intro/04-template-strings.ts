type Justify = "left" | "center" | "right"
type Align = "top" | "middle" | "bottom"

type Position = `${Align} ${Justify}`
type ShoutingPosition = Uppercase<Position>
