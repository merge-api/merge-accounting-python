# JournalEntry

# The JournalEntry Object ### Description The `JournalEntry` object is used to represent a company's journey entries.  ### Usage Example Fetch from the `GET JournalEntry` endpoint and view a company's journey entry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**transaction_date** | **datetime, none_type** | The journal entry&#39;s transaction date. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s journal entry was created. | [optional] 
**payments** | **[str, none_type]** | Array of &#x60;Payment&#x60; object IDs. | [optional] 
**memo** | **str, none_type** | The journal entry&#39;s private note. | [optional] 
**currency** | **object, none_type** | The journal&#39;s currency. | [optional] 
**lines** | [**[JournalLine]**](JournalLine.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


