import flet as ft
from vosk_ui.main_view import MainView


class VoskApp(ft.Row):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self._build_controls()

    def _build_controls(self):
        single_view = MainView()
        self.controls = [single_view]
