# POSTOrderPreviewRequestTypeSubscriptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | **dict(str, object)** | Container for custom fields of a Subscription object.  | [optional] 
**order_actions** | [**list[PreviewOrderOrderAction]**](PreviewOrderOrderAction.md) | The actions to be applied to the subscription. Order actions will be stored with the sequence when it was provided in the request. | [optional] 
**quote** | [**QuoteObjectFields**](QuoteObjectFields.md) |  | [optional] 
**ramp** | [**RampRequest**](RampRequest.md) |  | [optional] 
**subscription_number** | **str** | Leave this field empty to represent new subscription creation, or specify a subscription number to update an existing subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


