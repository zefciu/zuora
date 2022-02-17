# SettingItemHttpOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | One of the HTTP methods supported by the setting endpoint, for example, GET,PUT,POST or DELETE. | [optional] 
**parameters** | [**list[SettingItemHttpRequestParameter]**](SettingItemHttpRequestParameter.md) | An array of paramters required by this operation. | [optional] 
**request_type** | [**object**](.md) | JSON Schema for the request body of this operation. | [optional] 
**response_type** | [**object**](.md) | JSON Schema for the response body of this operation. | [optional] 
**url** | **str** | The endpoint url of the operation method. For example, &#x60;/settings/billing-rules&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


