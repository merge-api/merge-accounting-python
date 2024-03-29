# Contact

# The Contact Object ### Description The `Contact` object is used to represent a Contact. This can be either a supplier or a customer.  ### Usage Example Fetch from the `LIST Contacts` endpoint and view a company's contacts.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**name** | **str, none_type** | The contact&#39;s name. | [optional] 
**is_supplier** | **bool, none_type** | Whether the contact is a supplier. | [optional] 
**is_customer** | **bool, none_type** | Whether the contact is a customer. | [optional] 
**email_address** | **str, none_type** | The contact&#39;s email address. | [optional] 
**tax_number** | **str, none_type** | The contact&#39;s tax number. | [optional] 
**status** | **object, none_type** | The contact&#39;s status | [optional] 
**currency** | **str, none_type** | The currency the contact&#39;s transactions are in. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s contact was updated. | [optional] 
**addresses** | **[str, none_type]** | &#x60;Address&#x60; object IDs for the given &#x60;Contacts&#x60; object. | [optional] 
**phone_numbers** | [**[AccountingPhoneNumber]**](AccountingPhoneNumber.md) | &#x60;AccountingPhoneNumber&#x60; object for the given &#x60;Contacts&#x60; object. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


