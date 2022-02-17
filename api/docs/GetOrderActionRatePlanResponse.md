# GetOrderActionRatePlanResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_id** | **str** | The Id of the process that handle the operation.  | [optional] 
**reasons** | [**list[CommonResponseTypeReasons]**](CommonResponseTypeReasons.md) |  | [optional] 
**success** | **bool** | Indicates whether the call succeeded.  | [optional] 
**amendment** | [**OrderActionRatePlanAmendment**](OrderActionRatePlanAmendment.md) |  | [optional] 
**externally_managed_plan_id** | **str** | The unique identifier for the rate plan purchased on a third-party store. This field is used to represent a subscription rate plan created through third-party stores.  | [optional] 
**id** | **str** | Unique subscription rate-plan ID. | [optional] 
**last_change_type** | **str** | Latest change type. Possible values are:  - New - Update - Remove  | [optional] 
**order** | [**OrderActionRatePlanOrder**](OrderActionRatePlanOrder.md) |  | [optional] 
**product_id** | **str** | Product ID  | [optional] 
**product_name** | **str** | The name of the product.  | [optional] 
**product_rate_plan_id** | **str** | Product rate plan ID  | [optional] 
**product_sku** | **str** | The unique SKU for the product.  | [optional] 
**rate_plan_name** | **str** | The name of the rate plan.  | [optional] 
**subscription_id** | **str** | Subscription ID.  | [optional] 
**subscription_version** | [**object**](.md) | The version of the subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


