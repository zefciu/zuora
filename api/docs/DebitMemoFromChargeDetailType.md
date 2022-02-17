# DebitMemoFromChargeDetailType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the debit memo item.  **Note**: This field is only available if you set the &#x60;zuora-version&#x60; request header to &#x60;224.0&#x60; or later.  | [optional] 
**charge_id** | **str** | The ID of the product rate plan charge that the debit memo is created from.  **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | 
**comment** | **str** | Comments about the product rate plan charge.  **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or before.  | [optional] 
**description** | **str** | The description of the product rate plan charge.  **Note**: This field is only available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | [optional] 
**finance_information** | [**DebitMemoFromChargeDetailTypeAllOfFinanceInformation**](DebitMemoFromChargeDetailTypeAllOfFinanceInformation.md) |  | [optional] 
**memo_item_amount** | **float** | The amount of the debit memo item.  **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;224.0&#x60; or later.  | [optional] 
**product_rate_plan_charge_id** | **str** | The ID of the product rate plan charge that the debit memo is created from.  **Note**: This field is only available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | 
**quantity** | **float** | The number of units for the debit memo item.  | [optional] 
**service_end_date** | **date** | The service end date of the debit memo item. If not specified, the effective end date of the corresponding product rate plan will be used.  | [optional] 
**service_start_date** | **date** | The service start date of the debit memo item. If not specified, the effective start date of the corresponding product rate plan will be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


