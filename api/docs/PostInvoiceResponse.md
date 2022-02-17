# PostInvoiceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account associated with the invoice.  | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The total amount of the invoice.  | [optional] 
**amount_without_tax** | [**BigDecimal**](BigDecimal.md) | The invoice amount excluding tax.  | [optional] 
**auto_pay** | **bool** | Whether invoices are automatically picked up for processing in the corresponding payment run.  | [optional] 
**comments** | **str** | Comments about the invoice.  | [optional] 
**due_date** | **date** | The date by which the payment for this invoice is due.  | [optional] 
**id** | **str** | The unique ID of the invoice.  | [optional] 
**invoice_date** | **date** | The date that appears on the invoice being created.  | [optional] 
**invoice_number** | **str** | The unique identification number of the invoice.  | [optional] 
**status** | **str** | The status of the invoice.  | [optional] 
**tax_amount** | [**BigDecimal**](BigDecimal.md) | The amount of taxation.  | [optional] 
**tax_exempt_amount** | [**BigDecimal**](BigDecimal.md) | The calculated tax amount excluded due to the exemption.  | [optional] 
**transferred_to_accounting** | **str** | Whether the invoice was transferred to an external accounting system.  | [optional] 
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


