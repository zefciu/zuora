# OrderActionRatePlanChargeModelDataOverride

Container for charge model configuration data.  **Note**: This field is only available if you have the High Water Mark, Pre-Rated Pricing, or Multi-Attribute Pricing charge models enabled. The charge models are available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_model_configuration** | [**OrderActionRatePlanChargeModelDataOverrideChargeModelConfiguration**](OrderActionRatePlanChargeModelDataOverrideChargeModelConfiguration.md) |  | [optional] 
**tiers** | [**list[OrderActionRatePlanChargeTier]**](OrderActionRatePlanChargeTier.md) | List of cumulative pricing tiers in the charge.  **Note**: When you override tiers of the charge with a High Water Mark Pricing charge model, you have to provide all of the tiers, including the ones you do not want to change. The new tiers will completely override the previous ones. The High Water Mark Pricing charge models are available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


