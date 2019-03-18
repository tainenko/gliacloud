from part1.Integration import *

class TestIntegration:
    def foo(self,floor,ceil):

        return ceil**3/3+ceil-floor**3/3-floor

    def test_integration(self):
        assert integrate(anonymous,0,10)-self.foo(0,10)<=20

