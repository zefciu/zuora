# DebitMemoCollectResponseAllOfProcessedPayment

The information about the payment that newly processed to the debit memo. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The total amount of the payment.  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the payment.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the payment. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**id** | **str** | The unique ID of the created payment. For example, 4028905f5a87c0ff015a87eb6b75007f.  | [optional] 
**number** | **str** | The unique identification number of the payment. For example, P-00000001.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the payment.  | [optional] 
**status** | **str** | The status of the payment.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


