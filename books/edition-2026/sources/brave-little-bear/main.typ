#import "workbook-common.typ": *
#import "report-theme.typ": report-theme
#show: report-theme.with(title: "الدب الصغير الشجاع — طبعة 2026", author: "عالم لولو للصغار", rhythm: "report", body-size: 14pt, running-header: false)
#set text(font: ("Noto Naskh Arabic", "Noto Sans"), size: 14pt, lang: "ar", region: "eg")
#set heading(numbering: none)

#page(margin: (top: 18%, bottom: 16%, x: 2.2cm), numbering: none, header: none)[
  #align(center)[
    #block(fill: terracotta, inset: 12pt, width: 100%)[#text(font: "Noto Sans Arabic", size: 15pt, weight: "bold", fill: white)[عالم لولو للصغار]]
    #v(30pt)
    #text(font: "Noto Sans Arabic", size: 28pt, weight: "bold", fill: sage)[الدب الصغير الشجاع]
    #v(8pt)
    #text(font: "Noto Sans", size: 15pt, fill: terracotta)[Cesur Küçük Ayı · The Brave Little Bear]
    #v(25pt)
    #text(font: "Noto Color Emoji", size: 52pt)[🐻 🌿]
    #v(24pt)
    #card(fill: pale-green, border: sage)[#align(center)[قصة عن اللطف، والتفكير بهدوء، وطلب المساعدة.]]
    #v(18pt)
    #text(size: 13pt)[قصة قصيرة للقراءة المشتركة · طبعة 2026]
  ]
]
#page(numbering: none, header: none)[
  #outline(title: [صفحات القصة], indent: 1em)
  #v(0.8em)
  #card(fill: pale-yellow, border: honey)[اقرؤوا القصة معًا. يمكن للطفل أن يشير إلى الصور أو يختار كلمة يحبها. توقّفوا عند أي صفحة للحديث عن المشاعر، ولا تجعلوا الأسئلة اختبارًا.]
  #v(0.8em)
  #small-note[العربية والتركية والإنجليزية هنا طرق مختلفة لسرد القصة نفسها.]
  #v(0.7em)
  #card(fill: pale-pink, border: terracotta)[القصة خيالية؛ إذا رأيت شخصًا في خطر، أخبر شخصًا بالغًا ولا تقترب من الماء.]
]
#counter(page).update(1)

= صباح مشمس
#v(0.6em)
#card(fill: pale-yellow, border: honey, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 52pt)[🐻 ☀️]]]
#v(0.8em)
#card(fill: pale-green)[في صباحٍ مشمس، استيقظ الدب الصغير في بيته الدافئ.]
#v(0.5em)
#card(fill: pale-blue)[Güneşli bir sabah, Küçük Ayı sıcak yuvasında uyandı.]
#v(0.5em)
#card[On a sunny morning, Little Bear woke up in his cozy home.]

#pagebreak()
= صوت قرب النهر
#v(0.6em)
#card(fill: pale-blue, border: sage, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 50pt)[🐻 🌊 👂]]]
#v(0.8em)
#card(fill: pale-green)[قرب النهر، سمع صوتًا خافتًا يطلب المساعدة.]
#v(0.5em)
#card(fill: pale-blue)[Nehir yakınında yardım isteyen ince bir ses duydu.]
#v(0.5em)
#card[Near the river, he heard a tiny voice asking for help.]

#pagebreak()
= أرنب على صخرة
#v(0.6em)
#card(fill: pale-blue, border: sage, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 50pt)[🐻 🐰 🌊]]]
#v(0.8em)
#card(fill: pale-green)[رأى أرنبًا عالقًا على صخرةٍ وسط الماء.]
#v(0.5em)
#card(fill: pale-blue)[Suyun ortasındaki bir kayanın üzerinde sıkışmış bir tavşan gördü.]
#v(0.5em)
#card[He saw a rabbit stuck on a rock in the water.]

#pagebreak()
= أفكر بهدوء
#v(0.6em)
#card(fill: pale-pink, border: terracotta, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🐻 💭]]]
#v(0.8em)
#card(fill: pale-green)[خاف الدب قليلًا، لكنه توقف وفكر في طريقة آمنة للمساعدة.]
#v(0.5em)
#card(fill: pale-blue)[Küçük Ayı biraz korktu, ama durup yardım etmek için güvenli bir yol düşündü.]
#v(0.5em)
#card[Little Bear felt a little scared, but paused to think of a safe way to help.]

#pagebreak()
= أطلب المساعدة
#v(0.6em)
#card(fill: pale-yellow, border: honey, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🐻 📣 🦆]]]
#v(0.8em)
#card(fill: pale-green)[نادى صديقته البطة وطلب منها أن تساعده.]
#v(0.5em)
#card(fill: pale-blue)[Arkadaşı Ördek'e seslendi ve ondan yardım istedi.]
#v(0.5em)
#card[He called his friend Duck and asked her to help.]

#pagebreak()
= فكرة آمنة
#v(0.6em)
#card(fill: pale-green, border: sage, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🦆 🌿 🐰]]]
#v(0.8em)
#card(fill: pale-green)[قالت البطة: «لنقترب بهدوء ونمد هذا الغصن الطويل».]
#v(0.5em)
#card(fill: pale-blue)[Ördek, “Sakin yaklaşalım ve şu uzun dalı uzatalım,” dedi.]
#v(0.5em)
#card[Duck said, “Let's move carefully and reach out with this long branch.”]

#pagebreak()
= نساعد معًا
#v(0.6em)
#card(fill: pale-blue, border: sage, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🐻 🤝 🦆 🐰]]]
#v(0.8em)
#card(fill: pale-green)[أمسك الدب الغصن ومدّه للأرنب، بينما وقفت البطة بثبات على الضفة.]
#v(0.5em)
#card(fill: pale-blue)[Küçük Ayı dalı uzattı; Ördek kıyıda sağlam durdu ve Tavşan dala tutundu.]
#v(0.5em)
#card[Bear held out the branch. Duck stood firmly on the bank, and Rabbit held on.]

#pagebreak()
= وصل الأرنب إلى الأمان
#v(0.6em)
#card(fill: pale-green, border: sage, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🐰 🌱 🐻 🦆]]]
#v(0.8em)
#card(fill: pale-green)[وصل الأرنب إلى اليابسة وشكر صديقيه.]
#v(0.5em)
#card(fill: pale-blue)[Tavşan kıyıya çıktı ve iki arkadaşına teşekkür etti.]
#v(0.5em)
#card[Rabbit reached the shore and thanked his two friends.]

#pagebreak()
= الشجاعة وطلب المساندة
#v(0.6em)
#card(fill: pale-pink, border: terracotta, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🐻 🐰 💬]]]
#v(0.8em)
#card(fill: pale-green)[قال الأرنب: «كنت خائفًا». قال الدب: «وأنا أيضًا، ثم طلبت المساعدة».]
#v(0.5em)
#card(fill: pale-blue)[Tavşan, “Korkmuştum,” dedi. Küçük Ayı, “Ben de korktum; sonra yardım istedim,” dedi.]
#v(0.5em)
#card[“I was scared,” said Rabbit. “So was I. Then I asked for help,” said Bear.]

#pagebreak()
= أصدقاء يتشاركون
#v(0.6em)
#card(fill: pale-yellow, border: honey, inset: 18pt)[#align(center)[#text(font: "Noto Color Emoji", size: 48pt)[🐻 🐰 🦆 🍎]]]
#v(0.8em)
#card(fill: pale-green)[عاد الأصدقاء إلى البيت، وتقاسموا التفاح واحتفلوا بصداقتهم اللطيفة.]
#v(0.5em)
#card(fill: pale-blue)[Arkadaşlar eve döndü, elmaları paylaştı ve güzel dostluklarını kutladı.]
#v(0.5em)
#card[The friends went home, shared apples, and celebrated their kind friendship.]

#pagebreak()
= نتحدث عن القصة
#v(0.5em)
#card(fill: pale-yellow)[ما الشعور الذي مرّ به الدب؟ من ساعد الأرنب؟ ماذا يمكنك أن تفعل إذا احتجت إلى مساعدة؟]
#v(1em)
#text(size: 16pt, weight: "bold")[ارسم وجهًا يعبّر عن شعورك بعد القصة:]
#v(0.7em)
#rect(width: 100%, height: 125pt, fill: white, stroke: 1pt + line-color)
#v(1em)
#card(fill: pale-green)[#align(center)[تذكّر: طلب المساعدة تصرّف شجاع، ويمكننا أن نساعد بعضنا بأمان.]]
