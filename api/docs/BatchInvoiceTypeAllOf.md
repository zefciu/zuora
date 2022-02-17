# BatchInvoiceTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_pay** | **bool** | Whether invoices are automatically picked up for processing in the corresponding payment run.  By default, invoices are automatically picked up for processing in the corresponding payment run.  | [optional] 
**comments** | **str** | Additional information related to the invoice that a Zuora user added to the invoice.  | [optional] 
**due_date** | **date** | The date by which the payment for this invoice is due.  | [optional] 
**id** | **str** | The ID of the invoice to be updated.  | [optional] 
**invoice_date** | **date** | The new invoice date of the invoice. The new invoice date cannot fall in a closed accounting period.  You can only specify &#x60;invoiceDate&#x60; or &#x60;dueDate&#x60; in one request. Otherwise, an error occurs.  | [optional] 
**invoice_items** | [**list[PutInvoiceItemType]**](PutInvoiceItemType.md) | Container for invoice items. The maximum number of items is 1,000.  **Note:** Invoice items can only be updated if you have Unified Invoicing is enabled and the invoice is a standalone invoice.  | [optional] 
**transferred_to_accounting** | **str** | Whether the invoice was transferred to an external accounting system.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


