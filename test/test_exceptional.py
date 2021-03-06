import unittest
from operational_steps import count_steps
from piglatin import get_piglatin
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_error_type(self):
        test_obj = TestUtils()
        try:
            count_steps("45")
            test_obj.yakshaAssert("TestErrorType",False,"exception")
            print("TestErrorType = Failed")            
        except TypeError:
            test_obj.yakshaAssert("TestErrorType",True,"exception")
            print("TestErrorType = Passed")

    def test_error_type_for_piglatin(self):
        test_obj = TestUtils()
        try:
            get_piglatin(2)
            test_obj.yakshaAssert("TestErrorTypeForPiglatin",False,"exception")
            print("TestErrorTypeForPiglatin = Failed")
        except AttributeError:
            test_obj.yakshaAssert("TestErrorTypeForPiglatin",True,"exception")
            print("TestErrorTypeForPiglatin = Passed")
