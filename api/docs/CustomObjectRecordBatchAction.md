# CustomObjectRecordBatchAction

The batch action on custom object records
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_partial_success** | **bool** | Indicates whether the records that pass the schema validation should be updated when not all records in the request pass the schema validation.  This field is applicable only to the batch update actions.  | [optional] [default to False]
**ids** | **list[str]** | Ids of the custom object records that you want to delete. Only applicable when &#x60;type&#x60; is &#x60;delete&#x60;. | [optional] 
**records** | **dict(str, object)** | Object records that you want to update. Only applicable when &#x60;type&#x60; is &#x60;update&#x60;. | [optional] 
**type** | **str** | The type of the batch action | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


