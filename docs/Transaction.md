# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**transaction_type** | **str, none_type** | The type of general transaction. | [optional] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**number** | **str, none_type** | The transaction number. | [optional] 
**transaction_date** | **datetime, none_type** | The transaction date. | [optional] 
**account** | **str, none_type** | The transaction&#39;s account. | [optional] 
**contact** | **str, none_type** | The transaction&#39;s contact. | [optional] 
**total_amount** | **str, none_type** | The transaction&#39;s total amount. | [optional] 
**currency** | **object, none_type** | The transaction&#39;s currency. | [optional] 
**line_items** | [**[TransactionLineItem]**](TransactionLineItem.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


