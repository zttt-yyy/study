# -*- coding: UTF-8 -*-
import unittest
from UserTestCase import UserTestCase



class UserTestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass初始化")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass 资源清理")

    def testCase1(self):
        print("UserTestCase2 test case1")

    def testCase2(self):
        print("UserTestCase2 test case2")
        self.assertEqual(1, 1)

    def testCase3(self):
        print("UserTestCase2 test case3")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # verbosity 默认是1，为0的话最简洁，不输出每个用例执行结果，2 输出用例的详细执行结果
    # unittest.main(verbosity=2)
    # # 构造一个测试套件
    suite = unittest.TestSuite()
    #
    # # 类名('方法名')的集合
    # suite.addTest(UserTestCase2("testCase3"))
    # suite.addTest(userTestCase("testCase2"))
    # suite.addTest(UserTestCase2("testCase2"))
    #
    # # # 批量添加
    suite.addTests([UserTestCase2("testCase3"), UserTestCase2("testCase2"), UserTestCase("testCase2")])
    # #
    # # # 执行测试 TextTestRunner() 文本测试用例运行器，通过该类下面的run()方法来运行suite所组装的测试用例，入参为suite测试套件。
    runner = unittest.TextTestRunner(verbosity=2)
    #
    # # run()方法是运行测试套件的测试用例，入参为suite测试套件
    runner.run(suite)
