# POSTSubscriptionCancellationResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_date** | **date** | The date that the subscription was canceled.  | [optional] 
**credit_memo_id** | **str** | The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This container is only available if you set the Zuora REST API minor version to 207.0 or later in the request header, and you have  [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  | [optional] 
**invoice_id** | **str** | ID of the invoice, if one is generated.  | [optional] 
**paid_amount** | **float** | Amount paid.  | [optional] 
**payment_id** | **str** | ID of the payment, if a payment is collected.  | [optional] 
**subscription_id** | **str** | The subscription ID.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**total_delta_mrr** | **float** | Change in the subscription monthly recurring revenue as a result of the update.  | [optional] 
**total_delta_tcv** | **float** | Change in the total contracted value of the subscription as a result of the update.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


