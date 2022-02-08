"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeAccountingClient
from MergeAccountingClient.api.balance_sheets_api import BalanceSheetsApi  # noqa: E501


class TestBalanceSheetsApi(unittest.TestCase):
    """BalanceSheetsApi unit test stubs"""

    def setUp(self):
        self.api = BalanceSheetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_balance_sheets_list(self):
        """Test case for balance_sheets_list

        """
        pass

    def test_balance_sheets_retrieve(self):
        """Test case for balance_sheets_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()