from punc import recase_punc
from pathlib import Path
import wave
import vosk
from pydub import AudioSegment

from vosk import Model, KaldiRecognizer

from punct.recasepunc import WordpieceTokenizer
import json
        

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

def recognize(audio_path:str): 
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
            _ = rec.Result()
        else:
            _ = rec.PartialResult()
        
    result = json.loads(rec.FinalResult())
    return result
    
# text = 'этот теста веса пятьдесят раз два три четыре пять как она будет слышно я пока не знаю но тестовая тв запись давай проверим числа один два три четыре пять тысяча девятьсот пятьдесят семь восемь тысяч пятьсот триста двадцать пять стоп'
# audio_path = prepare_audio('src/audio_source.wav')
# result_text = recognize(audio_path)['text']
# print(result_text)


if __name__ == "__main__":
    recase_punc('этот теста веса пятьдесят раз два три четыре пять как она будет слышно я пока не знаю но тестовая тв запись давай проверим числа один два три четыре пять тысяча девятьсот пятьдесят семь восемь тысяч пятьсот триста двадцать пять стоп')

