from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    try:
        # Get the transcript for a YouTube video using its URL
        transcript = YouTubeTranscriptApi.get_transcript(video_url)

        return transcript

    except Exception as e:
        print(f'An error occurred: {e}')
        return None

# Replace 'VIDEO_URL' with the URL of the YouTube video you want the transcript for.
video_url = 'cJprHJ4mrPI'
transcript = get_transcript(video_url)

if transcript:
    print('Transcript:')
    for entry in transcript:
        print(f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}")
