#let sage = rgb("#4f6a58")
#let terracotta = rgb("#c97855")
#let honey = rgb("#e7b75c")
#let cream = rgb("#fbf7ef")
#let pale-green = rgb("#e8f0e7")
#let pale-pink = rgb("#fae8df")
#let pale-blue = rgb("#e7f0f5")
#let pale-yellow = rgb("#fff2d2")
#let ink = rgb("#3d443d")
#let line-color = rgb("#c9d2c8")

#let card(body, fill: white, border: line-color, inset: 10pt) = block(
  fill: fill,
  stroke: 0.8pt + border,
  inset: inset,
  width: 100%,
)[#body]
}

#let banner(title, subtitle: none) = block(
  fill: sage,
  inset: (x: 12pt, y: 8pt),
  width: 100%,
)[
  #align(center)[
    #text(font: "Noto Sans Arabic", size: 17pt, weight: "bold", fill: white)[#title]
    #if subtitle != none [
      #v(2pt)
      #text(font: "Noto Sans", size: 10pt, fill: white)[#subtitle]
    ]
  ]
]

#let word-card(arabic, turkish, english, icon: "") = card(fill: cream, border: terracotta, inset: 9pt)[
  #align(center)[
    #if icon != "" [#text(font: "Noto Color Emoji", size: 25pt)[#icon] #v(3pt)]
    #text(font: "Noto Naskh Arabic", size: 19pt, weight: "bold", fill: sage)[#arabic]
    #linebreak()
    #text(font: "Noto Sans", size: 12pt, weight: "bold")[#turkish]
    #linebreak()
    #text(font: "Noto Sans", size: 10pt, fill: gray)[#english]
  ]
]

#let write-lines(count: 4, gap: 18pt) = {
  for _ in range(count) {
    line(length: 100%, stroke: 0.65pt + line-color)
    v(gap)
  }
}

#let dotted-trace(content, size: 34pt) = align(center)[
  #text(font: "Noto Naskh Arabic", size: size, fill: luma(205))[#content]
]

#let small-note(content) = text(font: "Noto Naskh Arabic", size: 10pt, fill: gray)[#content]
