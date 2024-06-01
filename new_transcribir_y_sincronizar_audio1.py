import whisper
import torch
from datetime import timedelta

# Cargar el modelo de Whisper en GPU si está disponible
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("large").to(device)
result = model.transcribe("audio1.mp3")

# Crear archivo SRT
def convert_to_srt(text, start_time, duration):
    def format_timedelta(td):
        total_seconds = int(td.total_seconds())
        milliseconds = int(td.microseconds / 1000)
        return f"{total_seconds // 3600:02}:{(total_seconds % 3600) // 60:02}:{total_seconds % 60:02},{milliseconds:03}"

    srt_content = ""
    lines = text.split('. ')
    counter = 1
    current_time = start_time
    for line in lines:
        if not line.strip():
            continue
        end_time = current_time + duration
        srt_content += f"{counter}\n"
        srt_content += f"{format_timedelta(current_time)} --> {format_timedelta(end_time)}\n"
        srt_content += f"{line.strip()}.\n\n"
        current_time = end_time
        counter += 1
    return srt_content

start_time = timedelta(seconds=0)
duration = timedelta(seconds=3)  # Puedes ajustar esta duración según tus necesidades

srt_content = convert_to_srt(result["text"], start_time, duration)

with open("audio1.srt", "w", encoding="utf-8") as f:
    f.write(srt_content)

print("Transcripción completa. Revisar 'audio1.srt'.")
