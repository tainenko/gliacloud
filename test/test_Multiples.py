from part1.Multiplesof3and5 import *

class TestMultiples:
    def test_multiple3(self):
        assert get_multi_3(3) == 0
        assert get_multi_3(5)==3
        assert get_multi_3(10)==18

    def test_multiple5(self):
        assert get_multi_5(5)==0
        assert get_multi_5(10)==5
        assert get_multi_5(16) == 30

    def test_multiple15(self):
        assert get_multi_15(10)==0
        assert get_multi_15(16)==15
        assert get_multi_15(31) == 45

    def test_multiple_3_and_5(self):
        assert get_multi_3_and_5(10)==23