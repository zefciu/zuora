# GETPaymentRunDataTransactionElementResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The total amount of the newly generated payment.  **Note:** This field is only available if &#x60;type&#x60; is &#x60;Payment&#x60;.  | [optional] 
**applied_amount** | **float** | The amount allocated to this data record.  | [optional] 
**error_code** | **str** | The error code of the response.  **Note:** This field is only available if &#x60;type&#x60; is &#x60;Payment&#x60;.  | [optional] 
**error_message** | **str** | The detailed information of the error response.  **Note:** This field is only available if &#x60;type&#x60; is &#x60;Payment&#x60;.  | [optional] 
**id** | **str** | The ID of the current transaction.  | [optional] 
**status** | **str** | The status of the newly generated payment.  **Note:** This field is only available if &#x60;type&#x60; is &#x60;Payment&#x60;.  | [optional] 
**type** | **str** | The type of the current transaction.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


