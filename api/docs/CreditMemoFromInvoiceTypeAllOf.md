# CreditMemoFromInvoiceTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_apply_to_invoice_upon_posting** | **bool** | Whether the credit memo automatically applies to the invoice upon posting.  | [optional] 
**auto_post** | **bool** | Whether to automatically post the credit memo after it is created.   Setting this field to &#x60;true&#x60;, you do not need to separately call the [Post credit memo](https://www.zuora.com/developer/api-reference/#operation/PUT_PostCreditMemo) operation to post the credit memo.  | [optional] [default to False]
**comment** | **str** | Comments about the credit memo.  | [optional] 
**effective_date** | **date** | The date when the credit memo takes effect.  | [optional] 
**exclude_from_auto_apply_rules** | **bool** | Whether the credit memo is excluded from the rule of automatically applying credit memos to invoices.  | [optional] 
**invoice_id** | **str** | The ID of the invoice that the credit memo is created from.  * If this field is specified, its value must be the same as the value of the &#x60;invoiceId&#x60; path parameter. Otherwise, its value overrides the value of the &#x60;invoiceId&#x60; path parameter.  * If this field is not specified, the value of the &#x60;invoiceId&#x60; path parameter is used.  | [optional] 
**items** | [**list[CreditMemoItemFromInvoiceItemType]**](CreditMemoItemFromInvoiceItemType.md) | Container for items. The maximum number of items is 1,000.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 
**tax_auto_calculation** | **bool** | Whether to automatically calculate taxes in the credit memo.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


