# PostInvoiceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account associated with the invoice.   You must specify either &#x60;accountNumber&#x60; or &#x60;accountId&#x60; for a customer account. If both of them are specified, they must refer to the same customer account.  | [optional] 
**account_number** | **str** | The Number of the account associated with the invoice.  You must specify either &#x60;accountNumber&#x60; or &#x60;accountId&#x60; for a customer account. If both of them are specified, they must refer to the same customer account.  | [optional] 
**auto_pay** | **bool** | Whether invoices are automatically picked up for processing in the corresponding payment run.  | [optional] [default to False]
**comments** | **str** | Comments about the invoice.  | [optional] 
**due_date** | **date** | The date by which the payment for this invoice is due, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**invoice_date** | **date** | The date that appears on the invoice being created, in &#x60;yyyy-mm-dd&#x60; format. The value cannot fall in a closed accounting period.  | 
**invoice_items** | [**list[PostInvoiceItemType]**](PostInvoiceItemType.md) | Container for invoice items. The maximum number of invoice items is 1,000.  | [optional] 
**status** | **str** | The status of invoice. By default, the invoice status is Draft.  When creating an invoice, if you set this field to &#x60;Posted&#x60;, the invoice is created and posted directly.  | [optional] [default to 'Draft']
**transferred_to_accounting** | **str** |  | [optional] 
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


