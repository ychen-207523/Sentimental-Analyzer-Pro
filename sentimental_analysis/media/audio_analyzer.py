import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class AudioAnalyzer:

    def __init__(self):
        pass


    def speech_to_text(self, filename):
        r = sr.Recognizer()

        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            # print(text)
            return text


    def sentiment_analyzer_scores(self, sentence):
        analyser = SentimentIntensityAnalyzer()

        score = analyser.polarity_scores(sentence)
        # print("{:-<40} {}".format(sentence, str(score)))
        return score





## Usage
'''
aa = AudioAnalyzer()
text = aa.speech_to_text("test_wv.wav")
print(aa.sentiment_analyzer_scores(text))
'''
