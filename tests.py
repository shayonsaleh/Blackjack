import unittest
from blackjack import *

class ControlTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)
        
class CardTest(unittest.TestCase):
    def test_init(self):
        testCard = Card(0, 1)
        self.assertEquals(str(testCard), "Ace of Clubs")
        
        
if __name__ == '__main__':
    unittest.main()