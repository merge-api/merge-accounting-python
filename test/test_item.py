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
globals()['RemoteData'] = RemoteData
from MergeAccountingClient.model.item import Item
from MergeAccountingClient.api_client import ApiClient


class TestItem(unittest.TestCase):
    """Item unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testItem(self):
        """Test Item"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Item()  # noqa: E501

        """
        No test json responses were defined for Item
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Item,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
