import unittest

from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_null_french_to_english(self):
        self.assertNotEqual(french_to_english('null'), 'Hello')

    def test_null_english_to_french(self):
        self.assertNotEqual(english_to_french('null'), 'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
            
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()
