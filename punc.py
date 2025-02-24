import sys
import time
from transformers import logging
from punc.recasepunc import CasePuncPredictor
from punc.recasepunc import WordpieceTokenizer
from punc.recasepunc import Config

from transformers import TRANSFORMERS_CACHE

def recase_punc(text:str = 'этот теста веса пятьдесят раз два три четыре пять как она будет слышно я пока не знаю но тестовая тв запись давай проверим числа один два три четыре пять тысяча девятьсот пятьдесят семь восемь тысяч пятьсот триста двадцать пять стоп'):

   # logging.set_verbosity_error()

   predictor = CasePuncPredictor('src/checkpoint', lang="ru")

   # text = " ".join(open(sys.argv[1]).readlines())

   tokens = list(enumerate(predictor.tokenize(text)))

   results = ""
   for token, case_label, punc_label in predictor.predict(tokens, lambda x: x[1]):
      prediction = predictor.map_punc_label(predictor.map_case_label(token[1], case_label), punc_label)
      if token[1][0] != '#':
         results = results + ' ' + prediction
      else:
         results = results + prediction

   print (results.strip())
   
recase_punc()