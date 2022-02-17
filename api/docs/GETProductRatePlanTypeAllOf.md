# GETProductRatePlanTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Rate plan description.  | [optional] 
**effective_end_date** | **date** | Final date the rate plan is active, as &#x60;yyyy-mm-dd&#x60;. After this date, the rate plan status is &#x60;Expired&#x60;.  | [optional] 
**effective_start_date** | **date** | First date the rate plan is active (i.e., available to be subscribed to), as &#x60;yyyy-mm-dd&#x60;.  Before this date, the status is &#x60;NotStarted&#x60;.  | [optional] 
**id** | **str** | Unique product rate-plan charge ID.  | [optional] 
**name** | **str** | Name of the product rate-plan charge. (Not required to be unique.)  | [optional] 
**product_rate_plan_charges** | [**list[GETProductRatePlanChargeType]**](GETProductRatePlanChargeType.md) | Field attributes describing the product rate plan charges:  | [optional] 
**status** | **str** | Possible vales are: &#x60;Active&#x60;, &#x60;Expired&#x60;, &#x60;NotStarted&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


