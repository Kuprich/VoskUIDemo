from pathlib import Path
import wave
import vosk
from pydub import AudioSegment

from vosk import Model, KaldiRecognizer, SetLogLevel

vosk.MODEL_DIRS = ['src/voskModels']
MODEL_NAME = 'vosk-model-small-ru-0.22'
EXPORTED = 'src/exported'

def prepare_audio(input_file: str) -> str:
    file_name = Path(input_file).stem
    original_audio = AudioSegment.from_file(input_file)
    mono_audio = original_audio.set_channels(1)
    mono_audio.export(
        result := f"{EXPORTED}/{file_name}.wav",
        format="wav",
        parameters=["-sample_fmt", "s16"],
    )
    return result

SetLogLevel(0)

audio_path = prepare_audio('src/audio_source.wav')
wf = wave.open(audio_path)



model = Model(model_name=MODEL_NAME)

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(False)
rec.SetPartialWords(False)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
