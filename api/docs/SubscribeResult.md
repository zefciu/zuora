# SubscribeResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**charge_metrics_data** | [**SubscribeResultChargeMetricsData**](SubscribeResultChargeMetricsData.md) |  | [optional] 
**credit_memo_data** | [**list[ActionSubscribeCreditMemoData]**](ActionSubscribeCreditMemoData.md) | Container for credit memo data.  **Note**: This field is only available if you have the Invoice Settlement feature enabled and set the &#x60;X-Zuora-WSDL-Version&#x60; request header to &#x60;107&#x60; or later.  | [optional] 
**credit_memo_id** | **str** | The ID of the credit memo.  **Note**: This field is only available if you have the Invoice Settlement feature enabled and set the &#x60;X-Zuora-WSDL-Version&#x60; request header to &#x60;107&#x60; or later.  | [optional] 
**credit_memo_number** | **str** | The number of the credit memo.  **Note**: This field is only available if you have the Invoice Settlement feature enabled and set the &#x60;X-Zuora-WSDL-Version&#x60; request header to &#x60;107&#x60; or later.  | [optional] 
**credit_memo_result** | [**CreditMemoResult**](CreditMemoResult.md) |  | [optional] 
**errors** | [**list[ActionsErrorResponse]**](ActionsErrorResponse.md) |  | [optional] 
**gateway_response** | **str** |  | [optional] 
**gateway_response_code** | **str** |  | [optional] 
**invoice_data** | [**list[ActionSubscribeInvoiceData]**](ActionSubscribeInvoiceData.md) |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_result** | [**SubscribeResultInvoiceResult**](SubscribeResultInvoiceResult.md) |  | [optional] 
**payment_id** | **str** |  | [optional] 
**payment_transaction_number** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**subscription_number** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**total_mrr** | **float** |  | [optional] 
**total_tcv** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


