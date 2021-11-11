import unittest
from ..translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # Test None returns empty string
        self.assertEqual(englishToFrench(None), '')
        # Test empty string returns empty string
        self.assertEqual(englishToFrench(''), '')

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # Test None returns empty string
        self.assertEqual(frenchToEnglish(None), '')
        # Test empty string returns empty string
        self.assertEqual(frenchToEnglish(''), '')

unittest.main()


