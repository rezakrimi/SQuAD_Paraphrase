from googletrans import Translator
import googletrans
import json
from tqdm import tqdm
import time
import sys

with open('dev-paraphrase.json') as f:
  squad = json.load(f)

translator = Translator()
# data= squad['data'][0:5]


d = squad['data'][int(sys.argv[1])]
paragraphs = d['paragraphs']
for p in tqdm(paragraphs):
    while True:
        try:
            res = translator.translate(p['context'], src='en', dest='fr')
            res = translator.translate(res.text, src='fr', dest='en')
            p['paraphrase'] = res.text
            break
        except:
            print('translation failed')

with open('dev-paraphrase.json', 'w') as f:
    json.dump(squad, f)

