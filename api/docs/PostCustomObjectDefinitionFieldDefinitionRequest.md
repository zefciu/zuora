# PostCustomObjectDefinitionFieldDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The data format of the custom field | [optional] 
**label** | **str** | The UI label of the custom field | 
**max_length** | **int** | The maximum length of string that can be stored in the custom field. Only applicable if:  - The custom field &#x60;type&#x60; is &#x60;string&#x60;; and - The custom field &#x60;format&#x60; is not specified  If the custom field is filterable, the value of &#x60;maxLength&#x60; must be 512 or less.  | [optional] 
**type** | **str** | The data type of the custom field | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


