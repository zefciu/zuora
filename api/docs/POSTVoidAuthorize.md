# POSTVoidAuthorize

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account. This field is generally required, but is optional if you are using the Ingenico ePayments gateway. | [optional] 
**account_number** | **str** | The number of the customer account. This field is generally required, but is optional if you are using the Ingenico ePayments gateway. | [optional] 
**gateway_order_id** | **str** | The order ID for the specific gateway. | 
**payment_gateway_id** | **str** | The ID of the payment gateway instance. This field is required if you do not specify the &#x60;accountId&#x60; and &#x60;accountNumber&#x60; fields. | [optional] 
**transaction_id** | **str** | The ID of the transaction. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


