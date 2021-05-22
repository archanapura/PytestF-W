import pytest


class TestCaseB:

    @pytest.mark.dummy
    def testcase2(self,chrome_browser):
        print("second case")