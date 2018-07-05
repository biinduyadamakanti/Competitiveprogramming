import unittest


def sort_scores(scores, high):
    """sorts a list of scores. high is the highest possible"""

    count = {}

    for x in scores:
        score = count.get(x, 0)
        count[x] = score + 1

    sorts = []
    for i in range(high + 1):   # i = 0, 1, ... k-1
        if i in count:
            eyes =[i]*count[i]
            sorts.extend(eyes)
    
    sorts.reverse()

    print("scores %s sorted is %s" % (scores, sorts))
    return sorts



















# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([3, 8, 5, 3, 2], 11)
        expected = [8,5,6,3,3,2]
        self.assertEqual(actual, expected)
    def test_no_scores(self):
        actual = sort_scores([10,10,20],20)
        expected = [20,10,10]
        self.assertEqual(actual, expected)
     

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30,30,60], 100)
        expected = [60, 30,30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)