# Expense

# The Expense Object ### Description The `Expense` object is used to represent a company's expenses  ### Usage Example Fetch from the `GET Expense` endpoint and view a company's expense.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**transaction_date** | **datetime, none_type** | When the transaction occurred. | [optional] 
**remote_created_at** | **datetime, none_type** | When the expense was created. | [optional] 
**account** | **str, none_type** |  | [optional] 
**contact** | **str, none_type** |  | [optional] 
**total_amount** | **float, none_type** | The expense&#39;s total amount. | [optional] 
**currency** | **object, none_type** | The expense&#39;s currency. | [optional] 
**lines** | [**[ExpenseLine]**](ExpenseLine.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


