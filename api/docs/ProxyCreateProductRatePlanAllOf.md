# ProxyCreateProductRatePlanAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_currencies** | **list[str]** | A list of 3-letter currency codes representing active currencies for the product rate plan. Use a comma to separate each currency code.  When creating a product rate plan, you can use this field to specify at most four active currencies.   | [optional] 
**description** | **str** | A description of the product rate plan. **Character limit**: 500 **Values**: a string of 500 characters or fewer  | [optional] 
**effective_end_date** | **date** |  The date when the product rate plan expires and can&#39;t be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**effective_start_date** | **date** |  The date when the product rate plan becomes available and can be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**name** | **str** | The name of the product rate plan. The name doesn&#39;t have to be unique in a Product Catalog, but the name has to be unique within a product. **Character limit**: 100 **Values**: a string of 100 characters or fewer  | 
**product_id** | **str** | The ID of the product that contains the product rate plan. **Character limit**: 32 **Values**: a string of 32 characters or fewer  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


