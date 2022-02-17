# CustomObjectCustomFieldDefinitionUpdate

The custom field definition in the custom object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Applicable if the &#x60;type&#x60; of the action is  &#x60;updateField&#x60; | [optional] 
**description** | **str** | Applicable if the &#x60;type&#x60; of the action is  &#x60;updateField&#x60; | [optional] 
**format** | **str** | The data format of the custom field | [optional] 
**label** | **str** | The UI label of the custom field | [optional] 
**max_length** | **int** | The maximum length of string that can be stored in the custom field. Only applicable if:  - The custom field &#x60;type&#x60; is &#x60;string&#x60;; - The custom field &#x60;format&#x60; is not specified; and - The action &#x60;type&#x60; is &#x60;updateField&#x60;  If the custom field is filterable, the value of &#x60;maxLength&#x60; must be 512 or less.  | [optional] 
**origin** | **str** | Specifies that this is a custom field | [optional] 
**type** | **str** | The data type of the custom field | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


