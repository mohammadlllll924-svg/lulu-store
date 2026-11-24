#import "workbook-common.typ": *
#import "report-theme.typ": report-theme
#show: report-theme.with(title: "بطاقات لولو المصورة — طبعة 2026", author: "عالم لولو للصغار", rhythm: "report", body-size: 14pt, running-header: false)
#set text(font: ("Noto Naskh Arabic", "Noto Sans"), size: 14pt, lang: "ar", region: "eg")
#set heading(numbering: none)

#page(margin: (top: 18%, bottom: 16%, x: 2.2cm), numbering: none, header: none)[
  #align(center)[
    #block(fill: terracotta, inset: 12pt, width: 100%)[#text(font: "Noto Sans Arabic", size: 15pt, weight: "bold", fill: white)[عالم لولو للصغار]]
    #v(30pt)
    #text(font: "Noto Sans Arabic", size: 27pt, weight: "bold", fill: sage)[بطاقات لولو المصورة]
    #v(8pt)
    #text(font: "Noto Sans", size: 16pt, fill: terracotta)[Resimli Kelime Kartları · Picture Word Cards]
    #v(25pt)
    #text(font: "Noto Color Emoji", size: 48pt)[🍎 ☀️ 🐈]
    #v(25pt)
    #card(fill: pale-green, border: sage)[#align(center)[20 كلمة يومية بثلاث لغات: العربية، والتركية، والإنجليزية.]]
    #v(18pt)
    #text(size: 13pt)[اقصّوا البطاقات بمساعدة شخص بالغ · طبعة 2026]
  ]
]
#page(numbering: none, header: none)[
  #outline(title: [طريقة لعب البطاقات], indent: 1em)
  #v(0.8em)
  #card(fill: pale-yellow, border: honey)[اقرؤوا الكلمات على البطاقة، ثم أشروا إلى الصورة أو مثّلوا معناها. يمكن اللعب بالمطابقة بين بطاقتين أو اختيار كلمة واحدة لاستخدامها في حديث اليوم.]
  #v(0.8em)
  #small-note[لا حاجة إلى حفظ الكلمات كلها؛ أعيدوا البطاقات التي يحبها الطفل.]
]
#counter(page).update(1)

= فاكهة وشمس
#v(0.8em)
#word-card("تفاحة", "Elma", "Apple", icon: "🍎")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("شمس", "Güneş", "Sun", icon: "☀️")

#pagebreak()
= حيوانات أليفة
#v(0.8em)
#word-card("قطة", "Kedi", "Cat", icon: "🐈")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("كلب", "Köpek", "Dog", icon: "🐕")

#pagebreak()
= أشياء نحبها
#v(0.8em)
#word-card("كتاب", "Kitap", "Book", icon: "📘")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("كرة", "Top", "Ball", icon: "⚽")

#pagebreak()
= حيوانات كبيرة
#v(0.8em)
#word-card("أسد", "Aslan", "Lion", icon: "🦁")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("فيل", "Fil", "Elephant", icon: "🐘")

#pagebreak()
= في الحديقة
#v(0.8em)
#word-card("شجرة", "Ağaç", "Tree", icon: "🌳")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("زهرة", "Çiçek", "Flower", icon: "🌼")

#pagebreak()
= ماء وصداقة
#v(0.8em)
#word-card("ماء", "Su", "Water", icon: "💧")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("صديق", "Arkadaş", "Friend", icon: "🤝")

#pagebreak()
= طائر وبيت
#v(0.8em)
#word-card("طائر", "Kuş", "Bird", icon: "🐦")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("بيت", "Ev", "House", icon: "🏠")

#pagebreak()
= طريق ومدرسة
#v(0.8em)
#word-card("سيارة", "Araba", "Car", icon: "🚗")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("مدرسة", "Okul", "School", icon: "🏫")

#pagebreak()
= فطور لذيذ
#v(0.8em)
#word-card("حليب", "Süt", "Milk", icon: "🥛")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("موز", "Muz", "Banana", icon: "🍌")

#pagebreak()
= سمك وقمر
#v(0.8em)
#word-card("سمكة", "Balık", "Fish", icon: "🐟")
#v(1em)
#line(length: 100%, stroke: 0.8pt + line-color)
#v(1em)
#word-card("قمر", "Ay", "Moon", icon: "🌙")
