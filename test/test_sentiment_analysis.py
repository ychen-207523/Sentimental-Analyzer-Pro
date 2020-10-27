from pydoc import text
import sentimental_analysis.audio.audio_analyzer


def speech_to_text_test():
    pass

def sentiment_analyzer_scores_test(analyser=None):
    assert score==analyser.polarity_scores(sentence)
