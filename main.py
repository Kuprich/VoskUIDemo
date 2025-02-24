import voskUtils.utils as ut
from voskUtils.recasepunc import WordpieceTokenizer


def start_app():
    result = ut.recognize('src/audio.wav')
    print('result without recasepunc: ' + result['text'])
    
    recase_text = ut.recase_punc(result['text'])
    print('\n\nresult with recasepunc: ' + recase_text)
    

if __name__ == "__main__":
    start_app()
    

