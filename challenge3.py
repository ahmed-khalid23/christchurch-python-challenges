import wikipediaapi
import numpy as np
import matplotlib.pyplot as plt
import string
from wordcloud import WordCloud


# Prints summary of hello world page to terminal
wiki_wiki = wikipediaapi.Wikipedia('ChristCollegePythonChallenge3 (ahmedkhalid4931@gmail.com)', 'en')
page_hw = wiki_wiki.page('"Hello,_World!"_program')
print(f'Page Summary: {page_hw.summary}')
print()


# Frequency analysis of Oxford page
page_ox = wiki_wiki.page('Oxford')
# Frequency of letters in Oxford page
freq_ox = [0] * 26
total = 0
for l in page_ox.text:
    l = l.lower()
    if 96 < ord(l) < 123:
        freq_ox[ord(l) - 97] += 1
        total += 1

for i in range(len(freq_ox)):
    freq_ox[i] /= (total / 100)
# Frequency of letters in all English text (source wikipedia)
freq_eng = [
    8.2, 1.5, 2.8, 4.3, 12.7,
    2.2, 2, 6.1, 7, 0.15, 0.77,
    4, 2.4, 6.7, 7.5, 1.9, 0.095,
    6, 6.3, 9.1, 2.8, 0.98, 2.4,
    0.15, 2, 0.074
    ]

letter_stats = {
    'Wikipedia: Oxford' : freq_ox,
    'English Language' : freq_eng
}
labels = list(string.ascii_uppercase)
label_locations = np.arange(26)
width = 0.25
multiplier = 0.1

fig, ax = plt.subplots(layout='constrained')

for attribute, measurment in letter_stats.items():
    offset = width * multiplier
    rects = ax.bar(label_locations + offset, measurment, width, label=attribute)
    multiplier += 1

ax.set_ylabel('Relative Frequency, %')
ax.set_xticks(label_locations + width, labels)
ax.legend(loc='upper right', ncols=1)

#word cloud of sudan page
page_sud = wiki_wiki.page('Sudan')
wordcloud = WordCloud().generate(page_sud.text)
plt.imshow(wordcloud, interpolation='bilinear')

plt.show()