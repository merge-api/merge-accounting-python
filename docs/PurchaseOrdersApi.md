# MergeAccountingClient.PurchaseOrdersApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_orders_list**](PurchaseOrdersApi.md#purchase_orders_list) | **GET** /purchase-orders | 
[**purchase_orders_retrieve**](PurchaseOrdersApi.md#purchase_orders_retrieve) | **GET** /purchase-orders/{id} | 


# **purchase_orders_list**
> PaginatedPurchaseOrderList purchase_orders_list(x_account_token)



Returns a list of `PurchaseOrder` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeAccountingClient
from MergeAccountingClient.api import purchase_orders_api
from MergeAccountingClient.model.paginated_purchase_order_list import PaginatedPurchaseOrderList
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/accounting/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeAccountingClient.Configuration(
    host = "https://api.merge.dev/api/accounting/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeAccountingClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "line_items,delivery_address" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.purchase_orders_list(x_account_token)
        pprint(api_response)
    except MergeAccountingClient.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.purchase_orders_list(x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id)
        pprint(api_response)
    except MergeAccountingClient.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedPurchaseOrderList**](PaginatedPurchaseOrderList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_orders_retrieve**
> PurchaseOrder purchase_orders_retrieve(x_account_token, id)



Returns a `PurchaseOrder` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeAccountingClient
from MergeAccountingClient.api import purchase_orders_api
from MergeAccountingClient.model.purchase_order import PurchaseOrder
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/accounting/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeAccountingClient.Configuration(
    host = "https://api.merge.dev/api/accounting/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeAccountingClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "line_items,delivery_address" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.purchase_orders_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeAccountingClient.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.purchase_orders_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields)
        pprint(api_response)
    except MergeAccountingClient.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

