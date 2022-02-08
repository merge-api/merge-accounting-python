# Invoice

# The Invoice Object ### Description The `Invoice` object is used to represent a company's invoices.  ### Usage Example Fetch from the `LIST Invoices` endpoint and view a company's invoices.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**type** | **object, none_type** | The invoice&#39;s type. | [optional] 
**contact** | **str, none_type** |  | [optional] 
**number** | **str, none_type** | The invoice&#39;s number. | [optional] 
**issue_date** | **datetime, none_type** | The invoice&#39;s issue date. | [optional] 
**due_date** | **datetime, none_type** | The invoice&#39;s due date. | [optional] 
**paid_on_date** | **datetime, none_type** | The invoice&#39;s paid date. | [optional] 
**currency** | **object, none_type** | The invoice&#39;s currency. | [optional] 
**total_discount** | **float, none_type** | The invoice&#39;s total discount. | [optional] 
**sub_total** | **float, none_type** | The invoice&#39;s sub-total. | [optional] 
**total_tax_amount** | **float, none_type** | The invoice&#39;s total tax amount. | [optional] 
**total_amount** | **float, none_type** | The invoice&#39;s total amount. | [optional] 
**balance** | **float, none_type** | The invoice&#39;s remaining balance. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s invoice entry was updated. | [optional] 
**payments** | **[str, none_type]** | Array of &#x60;Payment&#x60; object IDs. | [optional] 
**line_items** | [**[InvoiceLineItem]**](InvoiceLineItem.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


