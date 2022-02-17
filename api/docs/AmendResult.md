# AmendResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_ids** | **list[str]** | A list of the IDs of the associated amendments. There can be as many as three amendment IDs. Use a comma to separate each amendment ID.  | [optional] 
**charge_metrics_data** | [**ChargeMetricsData**](ChargeMetricsData.md) |  | [optional] 
**credit_memo_datas** | [**list[ActionAmendCreditMemoData]**](ActionAmendCreditMemoData.md) |  | [optional] 
**credit_memo_id** | **str** |  | [optional] 
**errors** | [**list[ActionsErrorResponse]**](ActionsErrorResponse.md) |  | [optional] 
**gateway_response** | **str** |  | [optional] 
**gateway_response_code** | **str** |  | [optional] 
**invoice_datas** | [**list[ActionAmendInvoiceData]**](ActionAmendInvoiceData.md) | This array of invoices contains one invoice only as one invoice is generated for one subscription.  | [optional] 
**invoice_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**payment_transaction_number** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**total_delta_mrr** | **float** | &#x60;TotalDeltaMrr&#x60; is calculated by the following formula:   TotalDeltaMrr &#x3D; newSubscription.CMRR - originalSubscription.CMRR   See [here](https://knowledgecenter.zuora.com/Billing/Subscriptions/Customer_Accounts/A_How_to_Manage_Customer_Accounts/E_Key_Metrics/B_Monthly_Recurring_Revenue#Contracted_MRR) for the definition of CMRR. The new subscriptin represents the later version of an subscription after an amendment. The original subscription represents the original version of the subscription before the amendment.   | [optional] 
**total_delta_tcv** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


