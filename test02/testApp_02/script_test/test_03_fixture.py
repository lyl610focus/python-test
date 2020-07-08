import pytest
# 函数传递
@pytest.fixture()
def init_xx():
    print("初始化工作")
    with open("./data.txt", "w") as f:
        f.write("2")

@pytest.mark.usefixtures("init_xx")
class Test_xx:

    def setup_class(self):
        print("---------------setup")

    def teardown_class(self):
        print("------------------teardown")

    def test_xx(self):
        with open("./data.txt", "r") as f:
            # data = f.read()
            # print(data)
            assert f.read() == '2'

    def test_yy(self):
        with open("./data.txt", "r") as f:
            assert f.read() == "3"
