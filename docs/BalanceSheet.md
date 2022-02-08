# BalanceSheet

# The BalanceSheet Object ### Description The `BalanceSheet` object is used to represent a company's balance sheet.  ### Usage Example Fetch from the `LIST BalanceSheets` endpoint and view a company's balance sheets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**name** | **str, none_type** | The balance sheet&#39;s name. | [optional] 
**date** | **datetime, none_type** | The balance sheet&#39;s date. The balance sheet data will reflect the company&#39;s financial position this point in time. | [optional] 
**net_assets** | **float, none_type** | The balance sheet&#39;s net assets. | [optional] 
**assets** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**liabilities** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**equity** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**remote_generated_at** | **datetime, none_type** | The time that balance sheet was generated by the accounting system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

