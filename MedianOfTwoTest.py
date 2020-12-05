import unittest
from MedianOfTwo import MedianOfTwo

class MedianOfTwoTest(unittest.TestCase):
    def setUp(self):
        self.useCase = MedianOfTwo()
        
    def test_getMedian_firstNonEmpty(self):
        self.assertEqual(2.0, self.useCase.getMedian([2], []))
        
    def test_getMedian_secondNonEmpty(self):
        self.assertEqual(2.0, self.useCase.getMedian([], [2]))
        
    def test_getMedian_secondNonEmptyWithTwoNumbers(self):
        self.assertEqual(2.5, self.useCase.getMedian([], [2, 3]))
        
    def test_getMedian_bothOneNumber(self):
        self.assertEqual(2.5, self.useCase.getMedian([2], [3]))
        
    def test_getMedian_firstOneNumber_secondTwoNumbers(self):
        self.assertEqual(2, self.useCase.getMedian([2], [1,3]))
        
    def test_getMedian_firstLessThanSecond(self):
        self.assertEqual(2.5, self.useCase.getMedian([1,2], [3,4]))
        
    def test_getMedian_firstOutsideSecond(self):
        self.assertEqual(2.5, self.useCase.getMedian([1,4], [2,3]))
        
    def test_getMedian_firstAfterSecond(self):
        self.assertEqual(2.5, self.useCase.getMedian([3,4], [1,2]))
        
    def test_getMedian_firstInsideSecond(self):
        self.assertEqual(2.5, self.useCase.getMedian([2,3], [1,4]))
        
    def test_getMedian_firstInterspersedWithSecond(self):
        self.assertEqual(2.5, self.useCase.getMedian([1,3], [2,4]))
    
if __name__ == '__main__':
    unittest.main()
