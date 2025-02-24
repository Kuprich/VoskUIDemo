import voskUtils.utils as ut
from voskUtils.recasepunc import WordpieceTokenizer


def start_app():
    result = ut.recognize('src/aud2.ogg')
    print('result without recasepunc: ' + result)
    
    recase_text = ut.recase_punc(result)
    print('\n\nresult with recasepunc: ' + recase_text)
    

if __name__ == "__main__":
    start_app()
    

