import unittest

def prashanth(num):
    sai = 0
    while num>0:
        num = num//10
        sai +=1
    print("No of Digits = {}".format(sai))
    return sai

class Test(unittest.TestCase):

    def test_no_1(self):
        self.assertEqual(prashanth(25896),5)
    def test_no_2(self):
        self.assertNotEqual(prashanth(256),2)
    def test_no_3(self):
        self.assertEqual(prashanth(25898996),8)
    def test_no_4(self):
        self.assertNotEqual(prashanth(2589696),5)
        
if __name__ == '__main__':
    unittest.main()
