# PUTRefundTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comments about the refund.  | [optional] 
**finance_information** | [**PUTRefundTypeAllOfFinanceInformation**](PUTRefundTypeAllOfFinanceInformation.md) |  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile refunds between your gateway and Zuora Payments.  You can only update the reference ID for external refunds.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


