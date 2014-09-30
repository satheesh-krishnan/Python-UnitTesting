import palindrome
import unittest

class badinput(unittest.TestCase):
  
    def teststring(self):
        
        """palindrome should fail when first input is not string"""
        self.assertRaises(palindrome.NotStringError,palindrome.palin, 4)
    def testinvalidstring(self):
        self.assertRaises(palindrome.InvalidStringError,palindrome.palin, "]/.")
class badoutput(unittest.TestCase):
    def testoutput(self):
        """output value error"""
        self.assertEqual(palindrome.palin("madam"),True)        
if __name__ == "__main__":
    unittest.main()
