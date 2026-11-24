#import "workbook-common.typ": *
#import "report-theme.typ": report-theme
#show: report-theme.with(title: "مغامرات لولو — كتاب التلوين، طبعة 2026", author: "عالم لولو للصغار", rhythm: "report", body-size: 14pt, running-header: false)
#set page(width: 5.12in, height: 7.68in, margin: (x: 0.55in, y: 0.5in))
#set text(font: ("Noto Naskh Arabic", "Noto Sans"), size: 14pt, lang: "ar", region: "eg")
#set heading(numbering: none)

#page(margin: (top: 10%, bottom: 10%, x: 0.55in), numbering: none, header: none)[
  #align(center)[
    #block(fill: honey, inset: 12pt, width: 100%)[#text(font: "Noto Sans Arabic", size: 15pt, weight: "bold", fill: white)[عالم لولو للصغار]]
    #v(30pt)
    #text(font: "Noto Sans Arabic", size: 29pt, weight: "bold", fill: sage)[مغامرات لولو]
    #v(8pt)
    #text(font: "Noto Sans Arabic", size: 21pt, weight: "bold", fill: terracotta)[كتاب التلوين]
    #v(25pt)
    #text(font: "Noto Color Emoji", size: 50pt)[🖍️ 🌳 🐰]
    #v(25pt)
    #card(fill: pale-green, border: sage)[#align(center)[25 رسمة للتلوين، والتخيّل، وصنع حكايات جديدة.]]
    #v(18pt)
    #text(size: 13pt)[للطباعة المنزلية والروضة · طبعة 2026]
  ]
]
#page(numbering: none, header: none)[
  #align(center)[#text(font: "Noto Sans Arabic", size: 22pt, weight: "bold", fill: sage)[كيف نبدأ مغامرتنا؟]]
  #v(1em)
  #card(fill: pale-yellow, border: honey)[
    اختاروا صفحةً يحبها الطفل. جهّزوا ألوانًا مناسبة لعمره، ثم اتركوه يختار الألوان بنفسه. يمكن للكبير أن يسأل: «ماذا يحدث في الصورة؟» أو أن يترك مساحة هادئة للتلوين.
  ]
  #v(1em)
  #card(fill: pale-blue)[
    #text(size: 16pt, weight: "bold")[أفكار صغيرة أثناء التلوين]
    #v(0.5em)
    • سمّوا لونًا أو شكلًا بالعربية أو التركية. \
    • اطلبوا من الطفل أن يخبركم عن شخصية في الصورة. \
    • لا يشترط أن يبقى اللون داخل الخط؛ المهم أن يستمتع. \
    • أشرفوا على الطفل عند استخدام الأقلام أو الأدوات.
  ]
  #v(1em)
  #small-note[داخل هذا الكتاب 25 صفحة تلوين أصلية، تليها مساحة فارغة لرسم مغامرة جديدة.]
]
#page(numbering: none, header: none)[
  #align(center)[#text(font: "Noto Sans Arabic", size: 22pt, weight: "bold", fill: sage)[مغامرتي الجديدة]]
  #v(0.7em)
  #text(size: 14pt)[ارسم ما تحب، ثم احكِ لنا ماذا يحدث في الصورة.]
  #v(0.7em)
  #rect(width: 100%, height: 320pt, fill: white, stroke: 1pt + line-color)
  #v(0.7em)
  الاسم: #line(length: 60%, stroke: 0.8pt + line-color)
]
