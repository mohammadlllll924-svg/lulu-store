#import "workbook-common.typ": *
#import "report-theme.typ": report-theme

#show: report-theme.with(
  title: "ألوان وحروف مع لولو — طبعة 2026",
  author: "عالم لولو للصغار",
  rhythm: "report",
  body-size: 14pt,
  running-header: false,
)
#set text(font: ("Noto Naskh Arabic", "Noto Sans"), size: 14pt, lang: "ar", region: "eg")
#set heading(numbering: none)

#page(margin: (top: 18%, bottom: 16%, x: 2.2cm), numbering: none, header: none)[
  #align(center)[
    #block(fill: honey, inset: 12pt, width: 100%)[
      #text(font: "Noto Sans Arabic", size: 15pt, weight: "bold", fill: white)[عالم لولو للصغار]
    ]
    #v(30pt)
    #text(font: "Noto Sans Arabic", size: 27pt, weight: "bold", fill: sage)[ألوان وحروف مع لولو]
    #v(7pt)
    #text(font: "Noto Sans", size: 15pt, fill: terracotta)[Renkler ve Harfler Lulu ile]
    #v(16pt)
    #text(size: 14pt)[أنشطة عربي–تركي للأطفال من 3 إلى 6 سنوات]
    #v(30pt)
    #text(font: "Noto Color Emoji", size: 48pt)[🌈 🔤]
    #v(24pt)
    #card(fill: pale-green, border: sage)[#align(center)[تعلّمٌ صغير، ولعبٌ كثير، ومحاولةٌ جديدة كل يوم!]]
    #v(25pt)
    #text(size: 11pt, fill: gray)[طبعة 2026 · للطباعة المنزلية والروضة]
  ]
]

#page(numbering: none, header: none)[
  #outline(title: [كيف نستخدم الكتاب؟], indent: 1em)
  #v(1em)
  #card(fill: pale-yellow, border: honey)[
    اقرأوا الكلمة بالعربية ثم بالتركية، وأشيروا إلى اللون أو الشكل معًا. اختاروا نشاطًا واحدًا في كل مرة، واتركوا للطفل حرية التلوين والرسم والتوقف متى شاء.
  ]
  #v(0.8em)
  #small-note[لا نحتاج إلى إجابات كاملة؛ الاستماع والمحاولة والحديث اللطيف جزء من التعلّم.]
]
#counter(page).update(1)

= حروف نراها ونسمعها
#v(0.5em)
#card(fill: pale-green)[
  #align(center)[#text(size: 17pt, weight: "bold", fill: sage)[أ — أسد] #h(1em) #text(font: "Noto Sans", size: 17pt, weight: "bold")[A — Arı]]
  #v(0.45em)
  #align(center)[#text(font: "Noto Color Emoji", size: 36pt)[🦁] #h(1.5em) #text(font: "Noto Color Emoji", size: 36pt)[🐝]]
  #v(0.35em)
  #align(center)[الأسد يبدأ بـ «أ»، وArı تعني نحلة وتبدأ بـ A. لكل لغة كلماتها الجميلة.]
]
#v(0.8em)
#card(fill: pale-pink)[
  #align(center)[#text(size: 17pt, weight: "bold", fill: terracotta)[ب — بطة] #h(1em) #text(font: "Noto Sans", size: 17pt, weight: "bold")[B — Balık]]
  #v(0.45em)
  #align(center)[#text(font: "Noto Color Emoji", size: 36pt)[🦆] #h(1.5em) #text(font: "Noto Color Emoji", size: 36pt)[🐟]]
  #v(0.35em)
  #align(center)[بطة بالعربية، وBalık تعني سمكة بالتركية. ردّدوا الصوت الأول معًا.]
]
#v(1em)
#small-note[نشاط: اختاروا غرضًا قريبًا يبدأ اسمه بحرف «أ» أو «ب».]

#pagebreak()
= حروف تركية مميزة
#v(0.5em)
تحتوي التركية على حروف نراها كثيرًا في الكلمات اليومية. اسمعوا الصوت، ثم ابحثوا عن الحرف داخل الكلمة.
#v(0.8em)
#grid(columns: (1fr, 1fr), gutter: 8pt,
  card(fill: pale-yellow)[#align(center)[#text(size: 28pt, weight: "bold")[Ç] #linebreak() #text(size: 15pt)[Çiçek] #linebreak() زهرة 🌼]],
  card(fill: pale-blue)[#align(center)[#text(size: 28pt, weight: "bold")[Ş] #linebreak() #text(size: 15pt)[Şemsiye] #linebreak() مظلة ☂️]],
  card(fill: pale-pink)[#align(center)[#text(size: 28pt, weight: "bold")[Ö] #linebreak() #text(size: 15pt)[Ördek] #linebreak() بطة 🦆]],
  card(fill: pale-green)[#align(center)[#text(size: 28pt, weight: "bold")[Ü] #linebreak() #text(size: 15pt)[Üzüm] #linebreak() عنب 🍇]],
)
#v(1em)
#card[صلوا بين الحرف والكلمة بإصبعكم، ثم جرّبوا سماع أول صوت فيها.]

#pagebreak()
= ألوان حولنا
#v(0.5em)
سمّوا اللون بالعربية والتركية، ثم لوّنوا الدوائر بالألوان المناسبة.
#v(0.7em)
#grid(columns: (1fr, 1fr), gutter: 12pt,
  card(fill: pale-pink)[#align(center)[#text(size: 23pt, fill: rgb("#d75a55"))[●] #linebreak() أحمر · Kırmızı]],
  card(fill: pale-yellow)[#align(center)[#text(size: 23pt, fill: rgb("#e4b83e"))[●] #linebreak() أصفر · Sarı]],
  card(fill: pale-blue)[#align(center)[#text(size: 23pt, fill: rgb("#5998c6"))[●] #linebreak() أزرق · Mavi]],
  card(fill: pale-green)[#align(center)[#text(size: 23pt, fill: rgb("#6a9b65"))[●] #linebreak() أخضر · Yeşil]],
)
#v(1em)
#text(size: 16pt, weight: "bold")[ارسموا شيئًا أصفر في هذا الإطار:]
#v(0.5em)
#rect(width: 100%, height: 110pt, fill: white, stroke: 1pt + line-color)

#pagebreak()
= أشكال وأحجام
#v(0.5em)
#grid(columns: (1fr, 1fr), gutter: 12pt,
  card(fill: pale-blue)[#align(center)[#text(size: 34pt, fill: rgb("#568bb4"))[●] #linebreak() دائرة · Daire]],
  card(fill: pale-pink)[#align(center)[#text(size: 34pt, fill: rgb("#cc7860"))[■] #linebreak() مربع · Kare]],
  card(fill: pale-yellow)[#align(center)[#text(size: 34pt, fill: rgb("#d8a832"))[▲] #linebreak() مثلث · Üçgen]],
  card(fill: pale-green)[#align(center)[#text(size: 34pt, fill: rgb("#62896b"))[★] #linebreak() نجمة · Yıldız]],
)
#v(1em)
#card[نشاط: ابحثوا في الغرفة عن شيء دائري وشيء مربع، وقولوا اسميهما بالعربية أو التركية.]
#v(0.7em)
#rect(width: 100%, height: 90pt, fill: white, stroke: 1pt + line-color)

#pagebreak()
= نعدّ من واحد إلى خمسة
#v(0.5em)
#grid(columns: (1fr, 1fr, 1fr, 1fr, 1fr), gutter: 6pt,
  card(fill: pale-pink, inset: 6pt)[#align(center)[#text(size: 23pt, weight: "bold")[١] #linebreak() bir]],
  card(fill: pale-yellow, inset: 6pt)[#align(center)[#text(size: 23pt, weight: "bold")[٢] #linebreak() iki]],
  card(fill: pale-green, inset: 6pt)[#align(center)[#text(size: 23pt, weight: "bold")[٣] #linebreak() üç]],
  card(fill: pale-blue, inset: 6pt)[#align(center)[#text(size: 23pt, weight: "bold")[٤] #linebreak() dört]],
  card(fill: cream, inset: 6pt)[#align(center)[#text(size: 23pt, weight: "bold")[٥] #linebreak() beş]],
)
#v(1.2em)
#text(size: 16pt, weight: "bold")[عدّوا النجوم ثم اكتبوا العدد:]
#v(0.7em)
#align(center)[★  ★  ★  #h(1em) #line(length: 35%, stroke: 0.7pt + line-color)]
#v(0.8em)
#align(center)[●  ●  #h(1em) #line(length: 40%, stroke: 0.7pt + line-color)]
#v(0.8em)
#align(center)[▲  ▲  ▲  ▲  #h(1em) #line(length: 30%, stroke: 0.7pt + line-color)]

#pagebreak()
= حيوانات وكلمات
#v(0.5em)
#grid(columns: (1fr, 1fr), gutter: 10pt,
  word-card("قطة", "Kedi", "Cat", icon: "🐈"),
  word-card("كلب", "Köpek", "Dog", icon: "🐕"),
  word-card("أرنب", "Tavşan", "Rabbit", icon: "🐇"),
  word-card("زهرة", "Çiçek", "Flower", icon: "🌼"),
)
#v(0.8em)
#card(fill: pale-yellow)[اختاروا كلمة واحدة، وابحثوا عن صورة لها في كتاب أو لعبة. يمكنكم الاكتفاء بالإشارة إذا لم ترغبوا في الترديد.]

#pagebreak()
= نتتبع ونرسم
#v(0.5em)
#card(fill: pale-blue)[#align(center)[#text(size: 18pt, weight: "bold")[ابدأ من النقطة، واتبع الخط بإصبعك أولًا.]]]
#v(1em)
#dotted-trace("أ   أ   أ   أ   أ", size: 31pt)
#v(1.3em)
#write-lines(count: 3, gap: 16pt)
#v(0.7em)
#dotted-trace("ب   ب   ب   ب   ب", size: 31pt)
#v(1.3em)
#write-lines(count: 2, gap: 16pt)
#small-note[القلم السميك والوقت الهادئ يساعدان الطفل على المحاولة براحة.]

#pagebreak()
= لعبة البحث عن الألوان
#v(0.5em)
#card(fill: pale-green)[ابحثوا معًا عن غرض آمن في البيت لكل لون. ارسموا الغرض أو اكتبوا اسمه بمساعدة الكبار.]
#v(1em)
#grid(columns: (1fr, 1fr), gutter: 12pt,
  card(fill: pale-pink)[#align(center)[أحمر · Kırmızı #v(0.6em) #rect(width: 100%, height: 62pt, fill: white, stroke: 0.8pt + line-color)]],
  card(fill: pale-yellow)[#align(center)[أصفر · Sarı #v(0.6em) #rect(width: 100%, height: 62pt, fill: white, stroke: 0.8pt + line-color)]],
  card(fill: pale-blue)[#align(center)[أزرق · Mavi #v(0.6em) #rect(width: 100%, height: 62pt, fill: white, stroke: 0.8pt + line-color)]],
  card(fill: pale-green)[#align(center)[أخضر · Yeşil #v(0.6em) #rect(width: 100%, height: 62pt, fill: white, stroke: 0.8pt + line-color)]],
)

#pagebreak()
= شهادة إنجاز
#v(1em)
#card(fill: pale-yellow, border: honey, inset: 18pt)[
  #align(center)[
    #text(font: "Noto Sans Arabic", size: 24pt, weight: "bold", fill: sage)[أحسنت يا بطل!] \
    #v(0.6em)
    أكملت أنشطة الألوان والحروف مع لولو. \
    #v(1.2em)
    الاسم: #line(length: 55%, stroke: 0.8pt + line-color) \
    #v(1em)
    التاريخ: #line(length: 52%, stroke: 0.8pt + line-color) \
    #v(1.3em)
    #text(font: "Noto Color Emoji", size: 30pt)[🌟 🌟 🌟]
  ]
]
#v(1em)
#align(center)[كل محاولة تستحق ابتسامة.]
