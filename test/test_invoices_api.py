"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeAccountingClient
from MergeAccountingClient.api.invoices_api import InvoicesApi  # noqa: E501


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self):
        self.api = InvoicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_invoices_list(self):
        """Test case for invoices_list

        """
        pass

    def test_invoices_retrieve(self):
        """Test case for invoices_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
