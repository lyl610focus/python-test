import requests
import unittest
import xlrd
'''
url = "http://v.juhe.cn/weather/index"
data = {"cityname":"北京", "key":"f8633c639ed9ac182b1fde486ed7d59f"}
result = requests.get(url=url, params=data)

jason = result.json()
print(jason["error_code"])
'''

# 使用unitest，1、类继承unittest.TestCase 2、setup teatdown 3、名字以test开头的方法 4、断言
class Test(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        print("结束")

    '''
    def test_01(self):
        url = "http://v.juhe.cn/weather/index"
        para = {"cityname" : "南京", "key" : "f8633c639ed9ac182b1fde486ed7d59f"}
        result = requests.get(url, para)
        self.assertEquals(result.json()["error_code"], 0)
    '''

    def test_02(self):
        url = "http://www.kuaidi.com/index-ajaxselectinfo-1202247993797.html"
        result = requests.get(url)
        print(result.json()["4"]["name"])



if __name__ == '__main__':
    unittest.main()
