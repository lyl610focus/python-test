import pytest

class Test_1:
    # _class只会执行一次
    def setup_class(self):
        print("-------setup!!!!!!!!!!!!!!!------")

    def teardown_class(self):
        print("-------teardown-------")

    @pytest.mark.run(order = 3)
    def test_a(self):
        print("----------test_a-----")
        assert 1

    @pytest.mark.run(order = 1)
    def test_b(self):
        print("---------test_b-------")
        assert 0


if __name__ == '__main__':
    pytest.main()

