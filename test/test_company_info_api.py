"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeAccountingClient
from MergeAccountingClient.api.company_info_api import CompanyInfoApi  # noqa: E501


class TestCompanyInfoApi(unittest.TestCase):
    """CompanyInfoApi unit test stubs"""

    def setUp(self):
        self.api = CompanyInfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_company_info_list(self):
        """Test case for company_info_list

        """
        pass

    def test_company_info_retrieve(self):
        """Test case for company_info_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
