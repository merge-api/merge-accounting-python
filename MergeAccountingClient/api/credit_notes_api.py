"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergeAccountingClient.api_client import ApiClient, Endpoint as _Endpoint
from MergeAccountingClient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergeAccountingClient.model.credit_note import CreditNote
from MergeAccountingClient.model.paginated_credit_note_list import PaginatedCreditNoteList


class CreditNotesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __credit_notes_list(
            self,
            x_account_token,
            **kwargs
        ):
            """credit_notes_list  # noqa: E501

            Returns a list of `CreditNote` objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.credit_notes_list(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
                created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
                cursor (str): The pagination cursor value.. [optional]
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "payments"
                include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
                include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
                modified_after (datetime): If provided, will only return objects modified after this datetime.. [optional]
                modified_before (datetime): If provided, will only return objects modified before this datetime.. [optional]
                page_size (int): Number of results to return per page.. [optional]
                remote_fields (str): Which fields should be returned in non-normalized form.. [optional]
                remote_id (str, none_type): The API provider's ID for the given object.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaginatedCreditNoteList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            return self.call_with_http_info(**kwargs)

        self.credit_notes_list = _Endpoint(
            settings={
                'response_type': (PaginatedCreditNoteList,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/credit-notes',
                'operation_id': 'credit_notes_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'page_size',
                    'remote_fields',
                    'remote_id',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'remote_id',
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "PAYMENTS": "payments"
                    },
                    ('remote_fields',): {

                        "STATUS": "status",
                        "STATUS,TYPE": "status,type",
                        "TYPE": "type"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'expand':
                        (str,),
                    'include_deleted_data':
                        (bool,),
                    'include_remote_data':
                        (bool,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'page_size':
                        (int,),
                    'remote_fields':
                        (str,),
                    'remote_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_fields': 'remote_fields',
                    'remote_id': 'remote_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'page_size': 'query',
                    'remote_fields': 'query',
                    'remote_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__credit_notes_list
        )

        def __credit_notes_retrieve(
            self,
            x_account_token,
            id,
            **kwargs
        ):
            """credit_notes_retrieve  # noqa: E501

            Returns a `CreditNote` object with the given `id`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.credit_notes_retrieve(x_account_token, id, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.
                id (str):

            Keyword Args:
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "payments"
                include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
                remote_fields (str): Which fields should be returned in non-normalized form.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CreditNote
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.credit_notes_retrieve = _Endpoint(
            settings={
                'response_type': (CreditNote,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/credit-notes/{id}',
                'operation_id': 'credit_notes_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                    'include_remote_data',
                    'remote_fields',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "PAYMENTS": "payments"
                    },
                    ('remote_fields',): {

                        "STATUS": "status",
                        "STATUS,TYPE": "status,type",
                        "TYPE": "type"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'expand':
                        (str,),
                    'include_remote_data':
                        (bool,),
                    'remote_fields':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                    'remote_fields': 'remote_fields',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
                    'include_remote_data': 'query',
                    'remote_fields': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__credit_notes_retrieve
        )
