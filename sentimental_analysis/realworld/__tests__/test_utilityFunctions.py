import unittest
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from utilityFunctions import (
    removeLinks,
    stripEmojis,
    stripPunctuations,
    stripExtraWhiteSpaces,
    removeSpecialChar,
    sentiment_scores
)

class TestTextProcessing(unittest.TestCase):

    def test_removeLinks(self):
        text = "Visit us at http://example.com for more info."
        result = removeLinks(text)
        self.assertEqual(result, "Visit us at  for more info.")

    def test_stripEmojis(self):
        text = "I absolutely love this vacuum! 😊"
        result = stripEmojis(text)
        self.assertEqual(result, "I absolutely love this vacuum! ")

    def test_stripPunctuations(self):
        text = "The SuperClean 3000 is fantastic! Highly recommend."
        result = stripPunctuations(text)
        self.assertEqual(result, "The SuperClean 3000 is fantastic Highly recommend")

    def test_stripExtraWhiteSpaces(self):
        text = "  This vacuum   really   cleans well!  "
        result = stripExtraWhiteSpaces(text)
        self.assertEqual(result, "This vacuum really cleans well!")

    def test_removeSpecialChar(self):
        text = "Amazing product!!! #BestVacuum"
        result = removeSpecialChar(text)
        self.assertEqual(result, "Amazing product BestVacuum ")

    def test_removeSpecialChar(self):
        text = "Hello!!!  World@@@  This is a test... #Python 2024!!!"
        result = removeSpecialChar(text)
        self.assertEqual(result, "Hello  World  This is a test Python 2024")

    def test_no_change_needed_special_characters(self):
        text = "This is a clean sentence with no special characters."
        result = removeSpecialChar(text)
        self.assertEqual(result, "This is a clean sentence with no special characters")

    def test_no_change_needed_punctuation(self):
        text = "The SuperClean 3000 vacuum works well."
        result = stripPunctuations(text)
        self.assertEqual(result, "The SuperClean 3000 vacuum works well")

    def test_empty_string_removeLinks(self):
        text = ""
        result = removeLinks(text)
        self.assertEqual(result, "")

    def test_empty_string_stripEmojis(self):
        text = ""
        result = stripEmojis(text)
        self.assertEqual(result, "")

    def test_empty_string_stripPunctuations(self):
        text = ""
        result = stripPunctuations(text)
        self.assertEqual(result, "")

    def test_empty_string_stripExtraWhiteSpaces(self):
        text = ""
        result = stripExtraWhiteSpaces(text)
        self.assertEqual(result, "")

    def test_empty_string_removeSpecialChar(self):
        text = ""
        result = removeSpecialChar(text)
        self.assertEqual(result, "")

    def test_empty_string_removeSpecialChar(self):
        text = ""
        result = removeSpecialChar(text)
        self.assertEqual(result, "")

    def test_sentiment_scores_positive(self):
        text = "This vacuum is the best I've ever used! Highly efficient and easy to handle."
        result = sentiment_scores(text)
        self.assertGreater(result['compound'], 0)

    def test_sentiment_scores_negative(self):
        text = "I am very disappointed with this product. It does not work as expected."
        result = sentiment_scores(text)
        self.assertLess(result['compound'], 0)

    def test_sentiment_scores_neutral(self):
        text = "The vacuum is okay, but it has some issues."
        result = sentiment_scores(text)
        self.assertAlmostEqual(result['compound'], 0, delta=0.2)

if __name__ == '__main__':
    unittest.main()