import sys
import time
from transformers import logging
from punc.recasepunc import CasePuncPredictor
from punc.recasepunc import WordpieceTokenizer
from punc.recasepunc import Config

from transformers import TRANSFORMERS_CACHE

logging.set_verbosity_error()

predictor = CasePuncPredictor('src/checkpoint', lang="ru")

# text = " ".join(open(sys.argv[1]).readlines())
text = """
все смешалось в доме облонских жена узнала что муж был в связи с бывшею
в их доме француженкою-гувернанткой и объявила мужу что не может жить с
ним в одном доме положение это продолжалось уже третий день и мучительно
чувствовалось и самими супругами и всеми членами семьи и домочадцами
все члены семьи и домочадцы чувствовали что нет смысла в их сожительстве
и что на каждом постоялом дворе случайно сошедшиеся люди более связаны
между собой чем они члены семьи и домочадцы облонских жена не выходила
из своих комнат мужа третий день не было дома дети бегали по всему
дому как потерянные англичанка поссорилась с экономкой и написала
записку приятельнице прося приискать ей новое место повар ушел еще
вчера со двора во время обеда черная кухарка и кучер просили расчета
На третий день после ссоры князь степан аркадьич облонский стива как
его звали в свете в обычный час то есть в восемь часов утра
проснулся не в спальне жены а в своем кабинете на сафьянном диване
он повернул свое полное выхоленное тело на пружинах дивана как бы желая
опять заснуть надолго с другой стороны крепко обнял подушку и прижался к
ней щекой но вдруг вскочил сел на диван и открыл глаза
"""

text = 'этот теста веса пятьдесят раз два три четыре пять как она будет слышно я пока не знаю но тестовая тв запись давай проверим числа один два три четыре пять тысяча девятьсот пятьдесят семь восемь тысяч пятьсот триста двадцать пять стоп'
tokens = list(enumerate(predictor.tokenize(text)))

results = ""
for token, case_label, punc_label in predictor.predict(tokens, lambda x: x[1]):
    prediction = predictor.map_punc_label(predictor.map_case_label(token[1], case_label), punc_label)
    if token[1][0] != '#':
       results = results + ' ' + prediction
    else:
       results = results + prediction

print (results.strip())
