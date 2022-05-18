import unittest
import sys
sys.path.append("..")
from operational_steps import count_steps
from piglatin import get_piglatin
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_return_type_int(self):
        n=count_steps(25)
        test_obj = TestUtils()
        if type(n)==type(1):
            test_obj.yakshaAssert("TestReturnTypeInt", True, "functional")
            print("TestReturnTypeInt = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeInt", False, "functional")
            print("TestReturnTypeInt = Failed")
    def test_return_type_for_piglatin(self):
        s=get_piglatin("This is Venu")
        test_obj = TestUtils()
        if type(s)==type(" "):
            test_obj.yakshaAssert("TestReturnTypeForPiglatin", True, "functional")
            print("TestReturnTypeForPiglatin = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeForPiglatin", False, "functional")
            print("TestReturnTypeForPiglatin = Failed")
