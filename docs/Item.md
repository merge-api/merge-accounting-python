# Item

# The Item Object ### Description The `Item` object is used to represent an item that a company buys, sells, or resells, such as products and services.  ### Usage Example Fetch from the `LIST Items` endpoint and view a company's items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**name** | **str, none_type** | The item&#39;s name. | [optional] 
**status** | **object, none_type** | The item&#39;s status. | [optional] 
**unit_price** | **float, none_type** | The item&#39;s unit price. | [optional] 
**purchase_price** | **float, none_type** | The item&#39;s purchase price. | [optional] 
**purchase_account** | **str, none_type** |  | [optional] 
**sales_account** | **str, none_type** |  | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s item note was updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


