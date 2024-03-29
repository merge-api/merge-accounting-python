# AccountingAttachment

# The Accounting Attachment Object ### Description The `AccountingAttachment` object is used to represent a company's attachments.  ### Usage Example Fetch from the `LIST AccountingAttachments` endpoint and view a company's attachments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**file_name** | **str, none_type** | The attachment&#39;s name. | [optional] 
**file_url** | **str, none_type** | The attachment&#39;s url. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


