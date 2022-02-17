# SettingValueRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**object**](.md) | Request payload if any | [optional] 
**children** | [**list[ChildrenSettingValueRequest]**](ChildrenSettingValueRequest.md) | An array of requests that can only be executed after its parent request has been executed successfully.  | [optional] 
**id** | **str** | The id of the request. You can set it to any string. It must be unique within the whole batch.  | [optional] 
**method** | **str** | One of the HTTP methods supported by the setting endpoint, for example, GET,PUT,POST or DELETE.  | [optional] 
**url** | **str** | The relative URL of the setting. It is the same as in the &#x60;pathPattern&#x60; field in the response body of [Listing all Settings](https://www.zuora.com/developer/api-reference/#operation/GET_ListAllSettings). For example, &#x60;/billing-rules&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


