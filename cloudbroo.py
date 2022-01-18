import matplotlib.pyplot as plt
import fileupload
from wordcloud import WordCloud, STOPWORDS
import sys, os

import wordcloud
os.chdir(sys.path[0])

text = open("texto.txt",mode="r",encoding="utf-8").read()
stopwords = STOPWORDS


wc = WordCloud(
    background_color="white",
    stopwords =stopwords,
    height = 600,
    width = 400
)
wc.generate(text)
#wc.to_file("loco_pata_madres.png")

plt.imshow(wc, interpolation = 'nearest')
plt.axis('off')
plt.show()
