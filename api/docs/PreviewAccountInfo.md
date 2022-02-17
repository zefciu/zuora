# PreviewAccountInfo

Information about the account that will own the order. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_cycle_day** | **int** | Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as \&quot;AutoSet\&quot;. | 
**currency** | **str** | ISO 3-letter currency code (uppercase). For example, USD.  | 
**custom_fields** | **dict(str, object)** | Container for custom fields of an Account object.  | [optional] 
**sold_to_contact** | [**PreviewContactInfo**](PreviewContactInfo.md) |  | [optional] 
**tax_info** | [**TaxInfo**](TaxInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


