# -*- coding: UTF-8 -*-
import unittest


class UserTestCase(unittest.TestCase):
    def setUp(self):
        print("set up 开始")

    def tearDown(self):
        print("tearDown 执行结束")

    def testCase1(self):
        print('testcase1')

    def testCase2(self):
        print('Usertestcase testcase2')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
