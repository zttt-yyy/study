# -*- coding: UTF-8 -*-
import unittest
import os


def load_all_case():
    """加载制定路径的全部测试用例"""
    print(os.getcwd())
    case_path = os.path.join(os.getcwd(), "case")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*Case.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_all_case())
