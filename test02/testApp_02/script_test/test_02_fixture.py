import pytest
# 参数传递
@pytest.fixture()
def init_xx():
    print("初始化工作")
    with open("./data.txt", "w") as f:
        f.write("1")

class Test_xx:

    def test_xx(self, init_xx):
        with open("./data.txt", "r") as f:
            # data = f.read()
            # print(data)
            assert f.read() == '1'
