import whisper

model = whisper.load_model("Y:/ModelsAI/whisper_models/small.pt")
result = model.transcribe("stt/test_audio/chahirov_to_test.mp3", language="ru")

with open('stt/output.txt', 'w', encoding='utf-8') as f:
    f.write(result["text"])
