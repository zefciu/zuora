# CreditMemoFromChargeTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account associated with the credit memo.  | 
**auto_post** | **bool** | Whether to automatically post the credit memo after it is created.   Setting this field to &#x60;true&#x60;, you do not need to separately call the [Post a credit memo](https://www.zuora.com/developer/api-reference/#operation/PUT_PostCreditMemo) operation to post the credit memo.  | [optional] [default to False]
**charges** | [**list[CreditMemoFromChargeDetailType]**](CreditMemoFromChargeDetailType.md) | Container for product rate plan charges. The maximum number of items is 1,000.  | [optional] 
**comment** | **str** | Comments about the credit memo.  | [optional] 
**effective_date** | **date** | The date when the credit memo takes effect.  | [optional] 
**exclude_from_auto_apply_rules** | **bool** | Whether the credit memo is excluded from the rule of automatically applying unapplied credit memos to invoices and debit memos during payment runs. If you set this field to &#x60;true&#x60;, a payment run does not pick up this credit memo or apply it to other invoices or debit memos.  | [optional] [default to False]
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


