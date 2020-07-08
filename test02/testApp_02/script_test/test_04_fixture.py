import pytest
# 自动运行
# 默认是函数级别，可以修改
@pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(autouse=True)
def init_xx():
    print("初始化工作")
    with open("./data.txt", "w") as f:
        f.write("5")

class Test_xx:

    def test_xx(self):
        with open("./data.txt", "r") as f:
            # data = f.read()
            # print(data)
            assert f.read() == '5'

    def test_yy(self):
        with open("./data.txt", "r") as f:
            assert f.read() == "3"
