# GETAccountSummaryType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**GETAccountSummaryTypeBasicInfo**](GETAccountSummaryTypeBasicInfo.md) |  | [optional] 
**bill_to_contact** | [**GETAccountSummaryTypeBillToContact**](GETAccountSummaryTypeBillToContact.md) |  | [optional] 
**invoices** | [**list[GETAccountSummaryInvoiceType]**](GETAccountSummaryInvoiceType.md) | Container for invoices. Only returns the last 6 invoices.  | [optional] 
**payments** | [**list[GETAccountSummaryPaymentType]**](GETAccountSummaryPaymentType.md) | Container for payments. Only returns the last 6 payments.  | [optional] 
**sold_to_contact** | [**GETAccountSummaryTypeSoldToContact**](GETAccountSummaryTypeSoldToContact.md) |  | [optional] 
**subscriptions** | [**list[GETAccountSummarySubscriptionType]**](GETAccountSummarySubscriptionType.md) | Container for subscriptions.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**tax_info** | [**GETAccountSummaryTypeTaxInfo**](GETAccountSummaryTypeTaxInfo.md) |  | [optional] 
**usage** | [**list[GETAccountSummaryUsageType]**](GETAccountSummaryUsageType.md) | Container for usage data. Only returns the last 6 months of usage.  **Note:** If the Active Rating feature is enabled, no usage data is returned in the response body field.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


