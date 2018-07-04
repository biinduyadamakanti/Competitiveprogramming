
import unittest


def reverse(w):

    # Reverse the input list of chars in place
    l=len(w)-1
    l1=len(w)
    if(l1 ==0 or l1==1):
        return w
    for i in range(l1//2):
        b=w[l-i]
        w[l-i]=w[i]
        w[i]=b
    return w

















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)