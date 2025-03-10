import json
from pydub import AudioSegment
from transformers import logging
import wave
from vosk import Model, KaldiRecognizer
from pathlib import Path
from vosk_service.recasepunc import CasePuncPredictor, Config
import shutil
import os


MODEL_NAME = 'vosk-model-small-ru-0.22'
# MODEL_NAME = 'vosk-model-ru-0.10'
# MODEL_NAME = 'vosk-model-ru-0.42'

EXPORTED = 'exported'


def _prepare_audio(input_file: str) -> str:

    # clear exported folder
    shutil.rmtree(EXPORTED)
    os.mkdir(EXPORTED)

    file_name = Path(input_file).stem
    original_audio = AudioSegment.from_file(input_file)
    mono_audio = original_audio.set_channels(1)
    mono_audio.export(
        result := f"{EXPORTED}/{file_name}.wav",
        format="wav",
        parameters=["-sample_fmt", "s16"],
    )
    return result


def recase_punc(text: str):
    predictor = CasePuncPredictor('checkpoint', lang="ru")

    tokens = list(enumerate(predictor.tokenize(text)))

    results = ""

    for token, case_label, punc_label in predictor.predict(tokens, lambda x: x[1]):
        prediction = predictor.map_punc_label(
            predictor.map_case_label(token[1], case_label), punc_label)
        if token[1][0] != '#':
            results = results + ' ' + prediction
        else:
            results = results + prediction

    return results.strip()


def recognize(audio_path: str):

    audio_path = _prepare_audio(audio_path)

    wf = wave.open(audio_path)
    model = Model(model_name=MODEL_NAME)

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(False)
    rec.SetPartialWords(False)

    result = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result.append(json.loads(rec.Result())['text'])

    result.append(json.loads(rec.FinalResult())['text'])

    return ' '.join(result)
