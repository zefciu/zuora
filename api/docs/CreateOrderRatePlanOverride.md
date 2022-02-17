# CreateOrderRatePlanOverride

Information about an order action of type `addProduct`.   If you want to create a pending order through the \"Add product\" order action, and if the charge's trigger condition is `Specific Date`, you must set a charge number in the `chargeNumber` field for the \"Add product\" order action. In this case, if you do not set it, Zuora will not generate the charge number for you.  See more information about pending orders in [Pending Order and Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/Pending_Order_and_Subscription).  
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_overrides** | [**list[CreateOrderChargeOverride]**](CreateOrderChargeOverride.md) | List of charges associated with the rate plan.  | [optional] 
**custom_fields** | **dict(str, object)** | Container for custom fields of a Rate Plan object.  | [optional] 
**externally_managed_plan_id** | **str** | Indicates the unique identifier for the rate plan purchased on a third-party store. This field is used to represent a subscription rate plan created through third-party stores.  | [optional] 
**product_rate_plan_id** | **str** | Internal identifier of the product rate plan that the rate plan is based on.  | 
**unique_token** | **str** | Unique identifier for the rate plan. This identifier enables you to refer to the rate plan before the rate plan has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the rate plan. Then when you update the product, you can use the same unique identifier to specify which rate plan to modify.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


