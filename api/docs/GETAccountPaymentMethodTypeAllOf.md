# GETAccountPaymentMethodTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_payment_method_id** | **str** | ID of the default payment method for the account.  | [optional] 
**payment_gateway** | **str** | The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.  | [optional] 
**returned_payment_method_type** | [**list[GETPaymentMethodResponseForAccount]**](GETPaymentMethodResponseForAccount.md) | Container for a specific type of payment method on the customer account. For example, &#x60;creditcard&#x60;, &#x60;debitcard&#x60;, &#x60;creditcardreferencetransaction&#x60;, &#x60;ach&#x60;, etc. Each &#x60;returnedPaymentMethodType&#x60; array contains one or more payment methods of that payment method type.  **Note:** The response could return more than one payment method type arrays. See **Response samples** as an example.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


