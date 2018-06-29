import unittest


def find_rotation_point(words):
  length = len(words)
  first = 0
  last = length-1
  mid = first + (last-first)//2
  return binarySearch(words, first, last, mid)
    
def binarySearch(words,first,last,mid):
  if (first >= last):
    return mid
  if words[mid] > words[last]:
    first = mid+1
    mid = first + (last-first)//2
    return binarySearch(words, first, last, mid)
  if words[mid] < words[first]:
    last = mid
    mid = first + (last-first)/2
    return binarySearch(words, first, last, mid)

















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)