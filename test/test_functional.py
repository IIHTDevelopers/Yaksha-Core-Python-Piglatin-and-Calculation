import unittest
from operational_steps import count_steps
from piglatin import get_piglatin
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_result_for_25(self):
        n=count_steps(25)
        test_obj = TestUtils()
        if n==8:
            test_obj.yakshaAssert("TestResultFor25", True, "functional")
            print("TestResultFor25 = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeInt", False, "functional")
            print("TestResultFor25 = Failed")

    def test_result_for_15(self):
        n=count_steps(15)
        test_obj = TestUtils()
        if n==5:
            test_obj.yakshaAssert("TestResultFor15", True, "functional")
            print("TestResultFor15 = Passed")
        else:
            test_obj.yakshaAssert("TestResultFor15", False, "functional")
            print("TestResultFor15 = Failed")

    def test_result_for_zero(self):
        n=count_steps(1)
        test_obj = TestUtils()
        if n==0:
            test_obj.yakshaAssert("TestResultForZero", True, "functional")
            print("TestResultForZero = Passed")
        else:
            test_obj.yakshaAssert("TestResultForZero", False, "functional")
            print("TestResultForZero = Failed")

    def test_result_for_hellow(self):
        s=get_piglatin("Hellow")
        test_obj = TestUtils()
        if s=="ellowHa":
            test_obj.yakshaAssert("TestResultForHellow", True, "functional")
            print("TestResultForHellow = Passed")
        else:
            test_obj.yakshaAssert("TestResultForHellow", False, "functional")
            print("TestResultForHellow = Failed")

    def test_result_for_how_are_you(self):
        s=get_piglatin("how are you")
        test_obj = TestUtils()
        if s=="owha reaa ouya":
            test_obj.yakshaAssert("TestResultForHowAreYou", True, "functional")
            print("TestResultForHowAreYou= Passed")
        else:
            test_obj.yakshaAssert("TestResultForHowAreYou", False, "functional")
            print("TestResultForHowAreYou= Failed")

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
        s=get_piglatin("Hellow ")
        test_obj = TestUtils()
        if type(s)==type(" "):
            test_obj.yakshaAssert("TestReturnTypeForPiglatin", True, "functional")
            print("TestReturnTypeForPiglatin = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeForPiglatin", False, "functional")
            print("TestReturnTypeForPiglatin = Failed")
