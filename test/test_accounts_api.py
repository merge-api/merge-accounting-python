"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeAccountingClient
from MergeAccountingClient.api.accounts_api import AccountsApi  # noqa: E501


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts_list(self):
        """Test case for accounts_list

        """
        pass

    def test_accounts_retrieve(self):
        """Test case for accounts_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()