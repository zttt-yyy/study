# -*- coding: UTF-8 -*-
import unittest
from UserTestCase import UserTestCase
from UserTestCase2 import UserTestCase2

class VideoTestCase (unittest.TestCase) :
    def setUp(self):
        print("set up 开始")

    def tearDown(self):
        print("tearDown 执行结束")

    def testCase1(self):
        print("UserTestCase test case1")

    def testCase2(self):
        print("UserTestCase test case2")
        self.assertEqual(1, 1)

    def testCase3(self):
        print("UserTestCase test case3")
        self.assertEqual(1, 1)

if __name__ == '__main__':
    # 构造测试套件
    suite = unittest.TestSuite()

    # 实例化loader
    loader = unittest.TestLoader()

    # 加载UserTestCase下的全部用例

    suite.addTests(loader.loadTestsFromTestCase(UserTestCase))
    suite.addTests(loader.loadTestsFromTestCase(UserTestCase2))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
