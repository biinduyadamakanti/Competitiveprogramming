import unittest


def reverse_words(L):
    e= "".join(str(x) for x in L)
    r=e.split(" ")
    s=''
    l=[]
    for i in range(len(r)-1,-1,-1):
        s+=r[i]
        if i!=0:
            s+=" "
    
    return list(s)
















# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        message=reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        message=reverse_words(message)
        expected = list('cake thief')
        # print(expected)
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        message=reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        message=reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        message=reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        message=reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)