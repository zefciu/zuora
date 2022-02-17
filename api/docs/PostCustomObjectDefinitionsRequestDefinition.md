# PostCustomObjectDefinitionsRequestDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_record_migration** | **bool** | Specifies whether Deployment Manager migrates custom object records when migrating the custom object between tenants.  | [optional] [default to False]
**filterable** | **list[str]** | The set of fields that are allowed to be queried on. Queries on non-filterable fields will be rejected. You can not change a non-filterable field to filterable. | [optional] 
**label** | **str** | A UI label for the custom object | 
**object** | **str** | The API name of the custom object | 
**properties** | [**dict(str, PostCustomObjectDefinitionFieldDefinitionRequest)**](PostCustomObjectDefinitionFieldDefinitionRequest.md) |  | [optional] 
**relationships** | [**list[PostCustomObjectDefinitionsRequestDefinitionRelationships]**](PostCustomObjectDefinitionsRequestDefinitionRelationships.md) | An array of relationships with Zuora objects or other custom objects. You can add at most 2 &#x60;manyToOne&#x60; relationships when creating a custom field definition. | [optional] 
**required** | **list[str]** | The required fields of the custom object. You can change required fields to optional. However, you can only change optional fields to required on the custom objects with no records. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


