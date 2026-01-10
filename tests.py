#import all needed modules here
import unittest
from app import Sums
#write all your tests below this line

#write your test suite here, in the main() function
class TestInput(unittest.TestCase):
    def test_Sums(self):
        x=[]
        for i in range(15):
            x.append(1)
        self.assertEqual(Sums(x), [3,3,3,3,3])

def main():
    #call all your tets here, one on each line
    print(f"I ve tested to see if the Sums module is working propperly or not!")
    
#please do not change the lines below
if __name__ == "__main__":
    main()
    unittest.main()