# GETPublicNotificationDefinitionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the notification definition. The default value is &#x60;true&#x60;. | [optional] 
**callout** | [**GETPublicNotificationDefinitionResponseCallout**](GETPublicNotificationDefinitionResponseCallout.md) |  | [optional] 
**callout_active** | **bool** | The status of the callout action. The default value is &#x60;false&#x60;. | [optional] 
**communication_profile_id** | **str** | The profile that the notification definition belongs to. | [optional] 
**created_by** | **str** | The ID of the user who created the notification definition. | [optional] 
**created_on** | **datetime** | The time when the notification definition was created. Specified in the UTC timezone in the ISO860 format (YYYY-MM-DDThh:mm:ss.sTZD). E.g. 1997-07-16T19:20:30.45+00:00 | [optional] 
**description** | **str** | Description of the notification definition | [optional] 
**email_active** | **bool** | The status of the email action. The default value is &#x60;false&#x60;. | [optional] 
**email_template_id** | **str** | The ID of the email template. In the request, there should be at least one email template or callout. | [optional] 
**event_type_name** | **str** | The name of the event type. | [optional] 
**event_type_namespace** | **str** | The namespace of the &#x60;eventTypeName&#x60; field.   | [optional] 
**filter_rule** | [**GETPublicNotificationDefinitionResponseFilterRule**](GETPublicNotificationDefinitionResponseFilterRule.md) |  | [optional] 
**filter_rule_params** | **dict(str, str)** | The parameter values used to configure the filter rule.  | [optional] 
**id** | **str** | The ID associated with this notification definition. | [optional] 
**name** | **str** | The name of the notification definition. | [optional] 
**updated_by** | **str** | The ID of the user who updated the notification definition. | [optional] 
**updated_on** | **datetime** | The time when the notification was updated. Specified in the UTC timezone in the ISO860 format (YYYY-MM-DDThh:mm:ss.sTZD). E.g. 1997-07-16T19:20:30.45+00:00 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


