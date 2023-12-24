from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Specify the model and tokenizer
model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

@app.route('/summary', methods=['GET'])
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    transcript = get_transcript(video_id)
    if transcript:
        summary = get_summary(transcript)
        return summary, 200
    else:
        return "Error fetching transcript", 500

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = [i['text'] for i in transcript]
        transcript = ' '.join(transcript)
        return transcript
    except Exception as e:
        print(f'An error occurred fetching transcript: {e}')
        return None

def get_summary(transcript):
    # Tokenize the input transcript
    inputs = tokenizer(transcript, return_tensors="pt", max_length=1024, truncation=True)

    # Generate the summary
    summary_ids = model.generate(**inputs)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

if __name__ == '__main__':
    app.run(debug=True)
