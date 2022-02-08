"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeAccountingClient
from MergeAccountingClient.model.account import Account
globals()['Account'] = Account
from MergeAccountingClient.model.paginated_account_list import PaginatedAccountList
from MergeAccountingClient.api_client import ApiClient


class TestPaginatedAccountList(unittest.TestCase):
    """PaginatedAccountList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedAccountList(self):
        """Test PaginatedAccountList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedAccountList()  # noqa: E501

        """
        No test json responses were defined for PaginatedAccountList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedAccountList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
