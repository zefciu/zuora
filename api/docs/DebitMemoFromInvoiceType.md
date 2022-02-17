# DebitMemoFromInvoiceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_pay** | **bool** | Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.  | [optional] 
**auto_post** | **bool** | Whether to automatically post the debit memo after it is created.   Setting this field to &#x60;true&#x60;, you do not need to separately call the [Post debit memo](https://www.zuora.com/developer/api-reference/#operation/PUT_PostDebitMemo) operation to post the debit memo.  | [optional] [default to False]
**comment** | **str** | Comments about the debit memo.   | [optional] 
**effective_date** | **date** | The date when the debit memo takes effect.  | [optional] 
**invoice_id** | **str** | The ID of the invoice that the debit memo is created from.  * If this field is specified, its value must be the same as the value of the &#x60;invoiceId&#x60; path parameter. Otherwise, its value overrides the value of the &#x60;invoiceId&#x60; path parameter.  * If this field is not specified, the value of the &#x60;invoiceId&#x60; path parameter is used.   | [optional] 
**items** | [**list[DebitMemoItemFromInvoiceItemType]**](DebitMemoItemFromInvoiceItemType.md) | Container for items. The maximum number of items is 1,000.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 
**tax_auto_calculation** | **bool** | Whether to automatically calculate taxes in the debit memo.  | [optional] [default to True]
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the debit memo&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


