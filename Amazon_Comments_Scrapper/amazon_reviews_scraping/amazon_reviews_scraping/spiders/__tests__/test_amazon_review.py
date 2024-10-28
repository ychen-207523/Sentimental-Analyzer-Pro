import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import amazon_review

class TestAmazonReview(unittest.TestCase):
    def test_extract_asin_from_url_none_case(self):
        response = amazon_review.extract_asin_from_url("");
        self.assertEqual(response,None)

    def test_extract_asin_from_url_correct_url(self):
        response = amazon_review.extract_asin_from_url("https://www.amazon.com/Amazon-Official-Charger-Adapter-eReaders/dp/B01I0IGFKC/ref=asc_df_B01I0IGFKC/?tag=hyprod-20&linkCode=df0&hvadid=693445405897&hvpos=&hvnetw=g&hvrand=18188554830574334573&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197851&hvtargid=pla-571849787458&psc=1&mcid=1ee8356896d23365921828220d1e173e");
        self.assertEqual(response,"B01I0IGFKC")

    def test_get_date_place_none_case(self):
        response = amazon_review.get_date_place("")
        self.assertEqual(response,(None,None))

    def test_get_date_place_param_with_place_and_date(self):
        response = amazon_review.get_date_place("Reviewed in the United States on October 6, 2024")
        self.assertEqual(response,('October 6, 2024','the United States'))

if __name__ == '__main__':
    unittest.main()