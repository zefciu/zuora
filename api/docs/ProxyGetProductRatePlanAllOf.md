# ProxyGetProductRatePlanAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_currencies** | **list[str]** | A list of 3-letter currency codes representing active currencies for the product rate plan.   This field cannot be queried in conjunction with any other fields except &#x60;id&#x60; at the same time.   | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the &#x60;ProductRatePlan&#x60; object. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the &#x60;ProductRatePlan&#x60; object was created. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**description** | **str** | A description of the product rate plan. **Character limit**: 500 **Values**: a string of 500 characters or fewer  | [optional] 
**effective_end_date** | **date** |  The date when the product rate plan expires and can&#39;t be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**effective_start_date** | **date** |  The date when the product rate plan becomes available and can be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**name** | **str** | The name of the product rate plan. The name doesn&#39;t have to be unique in a Product Catalog, but the name has to be unique within a product. **Character limit**: 100 **Values**: a string of 100 characters or fewer  | [optional] 
**product_id** | **str** | The ID of the product that contains the product rate plan. **Character limit**: 32 **Values**: a string of 32 characters or fewer  | [optional] 
**updated_by_id** | **str** | The ID of the last user to update the object. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** | The date when the object was last updated. **Character limit**: 29 **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


