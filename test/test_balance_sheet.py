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
from MergeAccountingClient.model.remote_data import RemoteData
from MergeAccountingClient.model.report_item import ReportItem
globals()['RemoteData'] = RemoteData
globals()['ReportItem'] = ReportItem
from MergeAccountingClient.model.balance_sheet import BalanceSheet
from MergeAccountingClient.api_client import ApiClient


class TestBalanceSheet(unittest.TestCase):
    """BalanceSheet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBalanceSheet(self):
        """Test BalanceSheet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BalanceSheet()  # noqa: E501

        """
        No test json responses were defined for BalanceSheet
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (BalanceSheet,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
