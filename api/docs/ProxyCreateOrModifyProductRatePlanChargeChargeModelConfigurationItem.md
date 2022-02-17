# ProxyCreateOrModifyProductRatePlanChargeChargeModelConfigurationItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the field that is specified for a specific charge model.  Configuration keys supported are as follows:  * &#x60;formula&#x60; (only available if you have the Multi-Attribute Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.) * &#x60;customFieldPerUnitRate&#x60; (only available if you have the Pre-Rated Per Unit Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.) * &#x60;customFieldTotalAmount&#x60; (only available if you have the Pre-Rated Pricing model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.)  | [optional] 
**value** | **str** | The value of the field that is specified in the &#x60;Key&#x60; field.  Possible values are follows:  * A valid pricing formula to calculate actual rating amount for each usage record. For example, &#x60;usageQuantity()*10&#x60;. Use it with Key &#x60;formula&#x60; when the Multi-Attribute Pricing charge model is used. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information. * A name of a usage custom field that carries the per-unit rate for a usage record. For example, &#x60;perUnitRate__c&#x60;. Use it with Key &#x60;customFieldPerUnitRate&#x60; when the Pre-Rated Per Unit Pricing charge model is used. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information. * A name of a usage custom field that carries the total amount for a usage record. For example, &#x60;totalAmount__c&#x60;. Use it with Key &#x60;customFieldTotalAmount&#x60; when the Pre-Rated Pricing model is used. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

