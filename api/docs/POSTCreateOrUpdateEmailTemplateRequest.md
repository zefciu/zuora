# POSTCreateOrUpdateEmailTemplateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_partial_success** | **bool** | When set to &#x60;false&#x60;, the call will fail if one or multiple instances fail to import, and a &#x60;200&#x60; response is returned if all email templates have been successfully updated. When set to &#x60;true&#x60;, a success (&#x60;200&#x60;) response is returned if one or more instances have imported successfully. All failed instances are also returned in the response.  | [optional] 
**email_templates** | [**list[POSTCreateOrUpdateEmailTemplateRequestFormat]**](POSTCreateOrUpdateEmailTemplateRequestFormat.md) | A container for email templates.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


