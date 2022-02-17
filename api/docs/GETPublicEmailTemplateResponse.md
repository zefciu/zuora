# GETPublicEmailTemplateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the email template. | [optional] 
**bcc_email_address** | **str** | Email BCC address. | [optional] 
**cc_email_address** | **str** | Email CC address. | [optional] 
**cc_email_type** | **str** | Email cc type. | [optional] [default to 'SpecificEmails']
**created_by** | **str** | The ID of the user who created the email template. | [optional] 
**created_on** | **datetime** | The time when the email template was created. Specified in the UTC timezone in the ISO860 format (YYYY-MM-DDThh:mm:ss.sTZD). E.g. 1997-07-16T19:20:30.45+00:00 | [optional] 
**description** | **str** | The description of the email template. | [optional] 
**email_body** | **str** | The email body. You can add merge fields in the email object using angle brackets.  User can also embed html tags if &#x60;isHtml&#x60; is &#x60;true&#x60;. | [optional] 
**email_subject** | **str** | The email subject. You can add merge fields in the email subject using angle brackets. | [optional] 
**encoding_type** | **str** | The endcode type of the email body. | [optional] 
**event_category** | **float** | The event category code for a standard event. See [Standard Event Categories](https://knowledgecenter.zuora.com/Central_Platform/Notifications/A_Standard_Events/Standard_Event_Category_Code_for_Notification_Histories_API) for all event category codes. | [optional] 
**event_type_name** | **str** | The name of the custom event type. | [optional] 
**event_type_namespace** | **str** | The namespace of the &#x60;eventTypeName&#x60; field for custom events.   | [optional] 
**from_email_address** | **str** | If formEmailType is SpecificEmail, this field is required. | [optional] 
**from_email_type** | **str** | The from email type. | [optional] 
**from_name** | **str** | The name of email sender. | [optional] 
**id** | **str** | The email template ID. | [optional] 
**is_html** | **bool** | Indicates whether the style of email body is HTML. | [optional] 
**name** | **str** | The name of the email template. | [optional] 
**reply_to_email_address** | **str** | If replyToEmailType is SpecificEmail, this field is required | [optional] 
**reply_to_email_type** | **str** | The reply email type. | [optional] 
**to_email_address** | **str** | If &#x60;toEmailType&#x60; is &#x60;SpecificEmail&#x60;, this field is required. | [optional] 
**to_email_type** | **str** | Email receive type. | [optional] 
**updated_by** | **str** | The ID of the user who updated the email template. | [optional] 
**updated_on** | **datetime** | The time when the email template was updated. Specified in the UTC timezone in the ISO860 format (YYYY-MM-DDThh:mm:ss.sTZD). E.g. 1997-07-16T19:20:30.45+00:00 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


