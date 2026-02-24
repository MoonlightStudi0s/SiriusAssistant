import whisper

model = whisper.load_model("Y:/ModelsAI/whisper_models/small.pt")  # tiny, base, small, medium, large
result = model.transcribe("stt/test_audio/chahirov_to_test.mp3", language="ru")
print(result["text"])
