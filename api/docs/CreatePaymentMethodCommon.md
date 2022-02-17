# CreatePaymentMethodCommon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key** | **str** | Internal ID of the customer account that will own the payment method.   To create an orphan payment method that is not associated with any customer account, you do not need to specify this field during creation. However, you must associate the orphan payment method with a customer account within 10 days. Otherwise, this orphan payment method will be deleted.  | [optional] 
**auth_gateway** | **str** | Internal ID of the payment gateway that Zuora will use to authorize the payments that are made with the payment method.  If you do not set this field, Zuora will use one of the following payment gateways instead:  * The default payment gateway of the customer account that owns the payment method, if the &#x60;accountKey&#x60; field is set. * The default payment gateway of your Zuora tenant, if the &#x60;accountKey&#x60; field is not set.  | [optional] 
**gateway_options** | [**CreatePaymentMethodCommonGatewayOptions**](CreatePaymentMethodCommonGatewayOptions.md) |  | [optional] 
**make_default** | **bool** | Specifies whether the payment method will be the default payment method of the customer account that owns the payment method. Only applicable if the &#x60;accountKey&#x60; field is set.  | [optional] [default to False]
**mandate_info** | [**CreatePaymentMethodCommonMandateInfo**](CreatePaymentMethodCommonMandateInfo.md) |  | [optional] 
**skip_validation** | **bool** | Specify whether to skip the validation of the information through the payment gateway. For example, when migrating your payment methods, you can set this field to &#x60;true&#x60; to skip the validation.   | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


