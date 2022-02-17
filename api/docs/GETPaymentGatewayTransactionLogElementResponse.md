# GETPaymentGatewayTransactionLogElementResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **str** | The timestamp of the logs created in ISO-8601 format.  | [optional] 
**created_by** | **str** | The ID of the user who created the transaction.  | [optional] 
**currency** | **str** | The type of currenty, in which the transaction was made.  | [optional] 
**gateway_id** | **str** | The ID of the gateway, through which the transaction was processed.  | [optional] 
**gateway_name** | **str** | The name of the gateway, through which the transaction was processed.  | [optional] 
**gateway_type** | **str** | The type of the valid gateway, through which the transactioin was processed.  | [optional] 
**gateway_version** | **str** | The version of the gateway, through which the transaction was processed.  | [optional] 
**id** | **str** | The unique ID of the transaction log.  | [optional] 
**operation_id** | **str** | The ID of the transaction operation.  | [optional] 
**operation_type** | **str** | The type of transaction operation, such as &#x60;Payment&#x60;, &#x60;Refund&#x60;, &#x60;Validation&#x60;.  | [optional] 
**payment_method_type** | **str** | The type of the payment method used for the transaction, such as &#x60;Credit Card&#x60;, &#x60;ACH&#x60;, etc.  | [optional] 
**receive_time** | **str** | The time when Zuora received the response.  | [optional] 
**request** | **str** | The request parameters when sending the request.  | [optional] 
**response** | **str** | The response body of the received response.  | [optional] 
**response_code** | **str** | The code associated with the response. The value can be &#x60;Success&#x60;, &#x60;Failure&#x60;, or &#x60;Error&#x60;.  | [optional] 
**send_time** | **str** | The time when Zuora sent the request.  | [optional] 
**tenant_id** | **str** | The tenant ID of the user requesting the logs.  | [optional] 
**updated_by** | **str** | The ID of the user who last updated the transaction.  | [optional] 
**updated_time** | **str** | The timestamp of logs updated in ISO-8601 format.  | [optional] 
**z_reference_id** | **str** | The payment or refund Id.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


