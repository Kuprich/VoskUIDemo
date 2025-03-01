import vosk_service.utils as ut
from vosk_service.recasepunc import WordpieceTokenizer
import flet as ft

from vosk_ui import VoskApp
# from vosk_ui import VoskApp

# result = ut.recognize('src/aud2.ogg')s
# print('result without recasepunc: ' + result)

# recase_text = ut.recase_punc(result)
# print('\n\nresult with recasepunc: ' + recase_text)


if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Vosk UI v 1.0"
        page.padding = 10
        app = VoskApp(page)
        page.add(app)
        page.update()

    ft.app(main)
