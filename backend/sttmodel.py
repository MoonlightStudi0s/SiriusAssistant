import whisper

def make_description(name):
    filename = name
    model = whisper.load_model("Y:/ModelsAI/whisper_models/small.pt")
    result = model.transcribe("backend/files/{filename}.mp3", language="ru")

    with open('stt/output.txt', 'w', encoding='utf-8') as f:
        f.write(result["text"])

    return 1