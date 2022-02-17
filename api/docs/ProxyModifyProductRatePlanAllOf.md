# ProxyModifyProductRatePlanAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_currencies** | **list[str]** | A list of 3-letter currency codes representing active currencies for the product rate plan. Use a comma to separate each currency code.  If the request body contains this field, the value of this field must contain the desired list of active currencies. The new list can never have more than four differences from the existing list.  This field cannot be used to modify the status of more than four currencies in a single request. For example, in a single request, you can only activate four currencies, or deactivate four currencies, or activate two and deactivate two. Making more than four changes to currencies always requires more than one call.  When specifying this field in the update request, you must provide the full list of active currencies you want, not just incremental changes. For each active currency update, provide the following currencies in the list:  Current active currencies + at most four changes (additions or deletions)  | [optional] 
**description** | **str** | A description of the product rate plan. **Character limit**: 500 **Values**: a string of 500 characters or fewer  | [optional] 
**effective_end_date** | **date** |  The date when the product rate plan expires and can&#39;t be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**effective_start_date** | **date** |  The date when the product rate plan becomes available and can be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**name** | **str** | The name of the product rate plan. The name doesn&#39;t have to be unique in a Product Catalog, but the name has to be unique within a product. **Character limit**: 100 **Values**: a string of 100 characters or fewer  | [optional] 
**product_id** | **str** | The ID of the product that contains the product rate plan. **Character limit**: 32 **Values**: a string of 32 characters or fewer  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


