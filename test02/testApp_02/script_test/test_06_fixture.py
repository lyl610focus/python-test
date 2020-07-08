import pytest

class Test_abs:

    def setup_class(self):
        print("------------setup")

    def teardown(self):
        print("---------teardown")

    # 参数 参数有几个值就运行几次
    @pytest.mark.parametrize("a", [1,2,3])
    def test_aaa(self,a):
        assert a == 1


