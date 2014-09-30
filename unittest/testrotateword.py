import rotateword
import unittest

class inputtype(unittest.TestCase):
    def testinput(self):
        """invalid order of input"""
        self.assertRaises(rotateword.TypeError,rotateword.rotate, 5 ,"hello")
    def testoutputcheck(self):
        a=rotateword.rotate("hello",2)
        b=rotateword.rotate(a,26-2)
        self.assertEqual("hello",b)

if __name__=="__main__":
    unittest.main()
