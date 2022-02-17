# PUTPublicNotificationDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the notification definition. The default value is &#x60;true&#x60;. | [optional] [default to True]
**callout** | [**PUTPublicNotificationDefinitionRequestCallout**](PUTPublicNotificationDefinitionRequestCallout.md) |  | [optional] 
**callout_active** | **bool** | The status of the callout action. The default value is &#x60;false&#x60;. | [optional] [default to False]
**communication_profile_id** | **str** | The profile that notification definition belongs to. If you want to update the notification to a system notification, you should pass &#39;SystemNotification&#39;. &#39;  | [optional] 
**description** | **str** | The description of the notification definition. | [optional] 
**email_active** | **bool** | The status of the email action. The default value is &#x60;false&#x60;. | [optional] [default to False]
**email_template_id** | **str** | The ID of the email template. If emailActive is updated from false to true, an email template is required, and the EventType of the email template MUST be the same as the EventType of the notification definition.  | [optional] 
**filter_rule** | [**PUTPublicNotificationDefinitionRequestFilterRule**](PUTPublicNotificationDefinitionRequestFilterRule.md) |  | [optional] 
**filter_rule_params** | **dict(str, str)** | The parameter values used to configure the filter rule.  | [optional] 
**name** | **str** | The name of the notification definition, which is unique in the profile. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


