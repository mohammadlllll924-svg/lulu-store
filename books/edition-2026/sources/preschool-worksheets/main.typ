#import "workbook-common.typ": *
#import "report-theme.typ": report-theme
#show: report-theme.with(title: "حزمة أوراق العمل الأولى مع لولو — طبعة 2026", author: "عالم لولو للصغار", rhythm: "report", body-size: 14pt, running-header: false)
#set text(font: ("Noto Naskh Arabic", "Noto Sans"), size: 14pt, lang: "ar", region: "eg")
#set heading(numbering: none)

#page(margin: (top: 18%, bottom: 16%, x: 2.2cm), numbering: none, header: none)[
  #align(center)[
    #block(fill: sage, inset: 12pt, width: 100%)[#text(font: "Noto Sans Arabic", size: 15pt, weight: "bold", fill: white)[عالم لولو للصغار]]
    #v(30pt)
    #text(font: "Noto Sans Arabic", size: 26pt, weight: "bold", fill: sage)[حزمة أوراق العمل الأولى]
    #v(8pt)
    #text(font: "Noto Sans", size: 15pt, fill: terracotta)[Lulu İlk Etkinlik Sayfaları]
    #v(18pt)
    #text(font: "Noto Color Emoji", size: 50pt)[✏️ 🔢 ◯]
    #v(20pt)
    #card(fill: pale-green, border: sage)[#align(center)[تتبّعٌ وعدٌّ وأشكالٌ ومساحةٌ للرسم.]]
    #v(18pt)
    #text(size: 13pt)[للأطفال من 3 إلى 6 سنوات · طبعة 2026]
  ]
]
#page(numbering: none, header: none)[
  #outline(title: [دليل الأنشطة], indent: 1em)
  #v(0.8em)
  #card(fill: pale-yellow, border: honey)[اختاروا صفحة قصيرة، واجلسوا قرب الطفل. يمكن للكبير أن يشرح الخطوة أو يشير إلى البداية، ثم يترك للطفل مساحة للمحاولة. لا يلزم إكمال كل الصفحات في جلسة واحدة.]
  #v(0.8em)
  #small-note[استخدموا أدوات مناسبة للعمر، وابقوا قريبين أثناء استخدام الأقلام أو المقص.]
]
#counter(page).update(1)

= أكتب اسمي
#v(0.5em)
#card(fill: pale-blue)[#align(center)[قل اسمك بصوتك، ثم اطلب مساعدة الكبير لكتابته بخط خفيف. تتبّع الحروف بإصبعك أولًا.]]
#v(1.2em)
#text(size: 18pt, weight: "bold")[اسمي:]
#v(1em)
#write-lines(count: 5, gap: 30pt)
#v(1em)
#text(size: 16pt, weight: "bold")[اللون الذي أحبه اليوم:]
#v(0.7em)
#rect(width: 100%, height: 95pt, fill: white, stroke: 1pt + line-color)

#pagebreak()
= أتتبع الحروف
#v(0.5em)
#card(fill: pale-green)[ابدأوا بإصبعكم، ثم جرّبوا القلم بهدوء. لا بأس إن بقي أثر الحرف خفيفًا.]
#v(1.2em)
#text(size: 17pt, weight: "bold")[حروف عربية]
#v(0.5em)
#dotted-trace("ا   ا   ا   ا   ا", size: 38pt)
#v(0.6em)
#dotted-trace("ب   ب   ب   ب   ب", size: 38pt)
#v(1.2em)
#text(font: "Noto Sans", size: 17pt, weight: "bold")[Turkish letters]
#v(0.5em)
#align(center)[#text(font: "Noto Sans", size: 34pt, fill: luma(205))[A   A   A     B   B   B]]
#v(0.8em)
#write-lines(count: 2, gap: 20pt)

#pagebreak()
= أعدّ من واحد إلى خمسة
#v(0.5em)
#text(size: 15pt)[أشر إلى كل دائرة وأنت تعدّ، ثم اكتب العدد بمساعدة الكبير.]
#v(0.8em)
#grid(columns: (1fr, 1fr), gutter: 10pt,
  card(fill: pale-pink)[#align(center)[● #h(0.4em) ● #h(0.4em) ● #v(0.6em) العدد: #line(length: 24%, stroke: 0.7pt + line-color)]],
  card(fill: pale-yellow)[#align(center)[● #h(0.4em) ● #v(0.6em) العدد: #line(length: 24%, stroke: 0.7pt + line-color)]],
  card(fill: pale-green)[#align(center)[● #h(0.4em) ● #h(0.4em) ● #h(0.4em) ● #v(0.6em) العدد: #line(length: 24%, stroke: 0.7pt + line-color)]],
  card(fill: pale-blue)[#align(center)[● #v(0.6em) العدد: #line(length: 24%, stroke: 0.7pt + line-color)]],
)
#v(1em)
#small-note[قل العدد الأخير مرة أخرى؛ فهو يخبرنا كم دائرة في المجموعة.]

#pagebreak()
= أعدّ من ستة إلى عشرة
#v(0.5em)
#text(size: 15pt)[عدّوا معًا، ويمكنكم لمس كل نجمة مرة واحدة.]
#v(0.8em)
#card(fill: pale-yellow)[#align(center)[★  ★  ★  ★  ★  ★ #v(0.5em) كم نجمة؟ #line(length: 24%, stroke: 0.7pt + line-color)]]
#v(0.7em)
#card(fill: pale-blue)[#align(center)[★  ★  ★  ★  ★  ★  ★ #v(0.5em) كم نجمة؟ #line(length: 24%, stroke: 0.7pt + line-color)]]
#v(0.7em)
#card(fill: pale-green)[#align(center)[★  ★  ★  ★  ★  ★  ★  ★ #v(0.5em) كم نجمة؟ #line(length: 24%, stroke: 0.7pt + line-color)]]
#v(0.7em)
#card(fill: pale-pink)[#align(center)[★  ★  ★  ★  ★  ★  ★  ★  ★  ★ #v(0.5em) كم نجمة؟ #line(length: 24%, stroke: 0.7pt + line-color)]]

#pagebreak()
= أتعرف إلى الأشكال
#v(0.5em)
#grid(columns: (1fr, 1fr), gutter: 10pt,
  card(fill: pale-blue)[#align(center)[#text(size: 34pt, fill: rgb("#5793bd"))[●] #linebreak() دائرة]],
  card(fill: pale-pink)[#align(center)[#text(size: 34pt, fill: rgb("#c97855"))[■] #linebreak() مربع]],
  card(fill: pale-yellow)[#align(center)[#text(size: 34pt, fill: rgb("#d8a832"))[▲] #linebreak() مثلث]],
  card(fill: pale-green)[#align(center)[#text(size: 34pt, fill: rgb("#62896b"))[★] #linebreak() نجمة]],
)
#v(0.8em)
#card[ارسم دائرة حول المثلث، ثم ارسم خطًا تحت المربع.]
#v(0.8em)
#write-lines(count: 2, gap: 15pt)

#pagebreak()
= أكمل النمط
#v(0.5em)
#card(fill: pale-yellow)[انظر إلى ترتيب الأشكال. ما الشكل الذي يأتي بعد ذلك؟]
#v(1em)
#align(center)[#text(size: 34pt)[●  ▲  ●  ▲  □  □]]
#v(1em)
#card(fill: pale-green)[انظر إلى الألوان: أحمر، أزرق، أحمر، أزرق، □ ، □]
#v(1.2em)
#text(size: 16pt, weight: "bold")[ارسم نمطًا من اختيارك:]
#v(0.7em)
#rect(width: 100%, height: 120pt, fill: white, stroke: 1pt + line-color)

#pagebreak()
= كبير وصغير، أكثر وأقل
#v(0.5em)
#card(fill: pale-blue)[#align(center)[#text(size: 18pt)[◯  ○] #linebreak() أشر إلى الدائرة الأكبر.]]
#v(0.8em)
#card(fill: pale-pink)[#align(center)[● ● ● ●  #h(1em) ● ● #linebreak() أي مجموعة فيها أشياء أكثر؟]]
#v(0.8em)
#card(fill: pale-yellow)[#align(center)[#text(size: 17pt)[طويل  ─────────────   قصير  ───] #linebreak() أشِر إلى الخط الأقصر.]]
#v(1em)
#text(size: 16pt, weight: "bold")[ارسم شيئًا صغيرًا وشيئًا كبيرًا:]
#v(0.6em)
#rect(width: 100%, height: 100pt, fill: white, stroke: 1pt + line-color)

#pagebreak()
= خطوط أتبعها بإصبعي
#v(0.5em)
#card(fill: pale-green)[مرّر إصبعك من النجمة إلى البيت. بعد ذلك، اتبع المسار بالقلم.]
#v(1em)
#align(center)[#text(font: "Noto Color Emoji", size: 25pt)[⭐] #h(1em) #line(length: 55%, stroke: 1pt + line-color) #h(1em) #text(font: "Noto Color Emoji", size: 25pt)[🏠]]
#v(1.2em)
#write-lines(count: 5, gap: 25pt)
#v(1em)
#small-note[إذا تعبَت اليد، خذوا استراحة قصيرة وعودوا عندما ترغبون.]

#pagebreak()
= ارسم حديقة صغيرة
#v(0.5em)
#card(fill: pale-yellow)[ارسم شجرة واحدة، وثلاث زهرات، وطائرين. يمكنك إضافة ما تحب.]
#v(0.8em)
#rect(width: 100%, height: 275pt, fill: white, stroke: 1pt + line-color)
#v(0.7em)
#grid(columns: (1fr, 1fr), gutter: 10pt, card(fill: cream)[كم زهرة رسمت؟ #line(length: 35%, stroke: 0.7pt + line-color)], card(fill: cream)[كم طائرًا؟ #line(length: 35%, stroke: 0.7pt + line-color)])

#pagebreak()
= شهادة إنجاز
#v(1em)
#card(fill: pale-yellow, border: honey, inset: 18pt)[
  #align(center)[
    #text(font: "Noto Sans Arabic", size: 24pt, weight: "bold", fill: sage)[أحسنت!] \
    #v(0.6em)
    أكملت أنشطة لولو خطوةً خطوة. \
    #v(1em)
    الاسم: #line(length: 55%, stroke: 0.8pt + line-color) \
    #v(0.8em)
    التاريخ: #line(length: 52%, stroke: 0.8pt + line-color) \
    #v(1.2em)
    #text(font: "Noto Color Emoji", size: 30pt)[🌟 🌟 🌟]
  ]
]
