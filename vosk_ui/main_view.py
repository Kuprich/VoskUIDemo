import flet as ft
from vosk_ui import shared_controls


BUTTON_WIDTH = 170
FILE_EXTENSIONS = ["mp3", "wav", "aac", "flac", "ogg",
                         "m4a", "wma", "aiff", "alac", "opus", "amr", "mid", "ac3"]

class MainView(ft.Row):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._build_controls()
    
    def _build_controls(self):
        self.file_button = self._build_file_button()
        self.controls = [self.file_button]

    def _build_file_button(self):
        file_button = shared_controls.build_elevated_button(
            text="Select audio file",
            icon=ft.icons.AUDIO_FILE_OUTLINED,
            tooltip="Select audio from FileExplorer",
            width=170,
            # on_click=lambda _: self.pick_files_dialog.pick_files(
            #     allow_multiple=False, allowed_extensions=self.FILE_EXTENSIONS
            # ),
        )
        file_button.width = BUTTON_WIDTH

        return file_button