# -*- coding: utf-8 -*-
import unittest

from service.settings.settings import *


class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("**************************************** setUpClass ****************************************")

    @classmethod
    def tearDownClass(cls):
        print("************************************** tearDownClass ***************************************")

    def setUp(self):
        print("****** setUp *******")

    def tearDown(self):
        print("***** tearDown *****")

    def test_example(self):
        print("This is a test example.")
        print(TIMEZONE)

        # df_time_used = instance.query_sample()
        # print(df_time_used)
