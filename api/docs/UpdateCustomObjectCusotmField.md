# UpdateCustomObjectCusotmField

A reference to a field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**CustomObjectCustomFieldDefinitionUpdate**](CustomObjectCustomFieldDefinitionUpdate.md) |  | [optional] 
**filterable** | **bool** | Indicates whether the field is filterable or not. Applicable to &#x60;addField&#x60; and &#x60;updateField&#x60; actions.  You can change a filterable field to non-filterable and vice versa. You can also add a filterable field. One custom object can have a maximum of 10 filterable fields.  Note that changing filterable fields triggers reindexing. It will take 12-24 hours before all your data are reindexed and available to query.  | [optional] 
**name** | **str** | The name of the custom field to be updated | [optional] 
**required** | **bool** | Indicates whether the field is required or optional.  You can update a required field to optional. On the other hand, you can only update an optional field to required on the custom object with no records.  You can only add a required field to the custom object with no records.  | [optional] 
**target_name** | **str** | Required if the &#x60;type&#x60; of the action is &#x60;renameField&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


