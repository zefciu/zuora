# CustomObjectDefinitionSchema

The schema of the custom object definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_record_migration** | **bool** | Specifies whether Deployment Manager migrates custom object records when migrating the custom object between tenants.  | [optional] 
**filterable** | **list[str]** | The set of fields that are allowed to be queried on. Queries on non-filterable fields will be rejected. You can not change a non-filterable field to filterable. | [optional] 
**label** | **str** | A label for the custom object | [optional] 
**object** | **str** | The API name of the custom object | [optional] 
**properties** | [**CustomObjectAllFieldsDefinition**](CustomObjectAllFieldsDefinition.md) |  | [optional] 
**relationships** | [**list[CustomObjectDefinitionSchemaRelationships]**](CustomObjectDefinitionSchemaRelationships.md) | An array of relationships with Zuora objects or other custom objects | [optional] 
**required** | **list[str]** | The required fields of the custom object definition. You can change required fields to optional. However, you can only change optional fields to required on the custom objects with no records. | [optional] 
**type** | **str** | The custom object definition type. Can only be &#x60;object&#x60; currently. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


