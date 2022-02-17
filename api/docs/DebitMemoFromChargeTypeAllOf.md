# DebitMemoFromChargeTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account associated with the debit memo.  **Note**: When creating debit memos from product rate plan charges, you must specify &#x60;accountNumber&#x60;, &#x60;accountId&#x60;, or both in the request body. If both fields are specified, they must correspond to the same account.  | [optional] 
**account_number** | **str** | The Number of the account associated with the debit memo.  **Note**: When creating debit memos from product rate plan charges, you must specify &#x60;accountNumber&#x60;, &#x60;accountId&#x60;, or both in the request body. If both fields are specified, they must correspond to the same account.  | [optional] 
**auto_pay** | **bool** | Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.  | [optional] 
**auto_post** | **bool** | Whether to automatically post the debit memo after it is created.   Setting this field to &#x60;true&#x60;, you do not need to separately call the [Post a debit memo](https://www.zuora.com/developer/api-reference/#operation/PUT_PostDebitMemo) operation to post the debit memo.  | [optional] [default to False]
**charges** | [**list[DebitMemoFromChargeDetailType]**](DebitMemoFromChargeDetailType.md) | Container for product rate plan charges. The maximum number of items is 1,000.  | [optional] 
**comment** | **str** | Comments about the debit memo.  | [optional] 
**due_date** | **date** | The date by which the payment for the debit memo is due, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**effective_date** | **date** | The date when the debit memo takes effect.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


