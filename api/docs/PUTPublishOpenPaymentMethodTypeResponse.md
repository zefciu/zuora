# PUTPublishOpenPaymentMethodTypeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | If an entity UUID is provided, this custom payment method type is specific to this entity only. If no entity UUID is provided, the custom payment method type is available to the global entity and all the sub entities in the tenant.  | [optional] 
**fields** | [**list[OpenPaymentMethodTypeResponseFields]**](OpenPaymentMethodTypeResponseFields.md) | An array containing field metadata of the custom payment method type.  | [optional] 
**internal_name** | **str** | A string to identify the custom payment method type in the API name of the payment method type.  This field is used along with the &#x60;tenantId&#x60; field by the system to construct and generate the API name of the custom payment method type in the following way:  &#x60;&lt;internalName&gt;__c_&lt;tenantId&gt;&#x60;  For example, if &#x60;internalName&#x60; is &#x60;AmazonPay&#x60;, and &#x60;tenantId&#x60; is &#x60;12368&#x60;, the API name of the custom payment method type will be &#x60;AmazonPay__c_12368&#x60;.  | [optional] 
**label** | **str** | The label that is used to refer to this type in the Zuora UI.  | [optional] 
**method_reference_id_field** | **str** | A field available in the Payment Method data source export and Data Query for filtering data.  | [optional] 
**revision** | **int** | The revision number of the custom payment method type, which starts from 1 and increases by 1 when you update a published revision for the first time.  | [optional] 
**status** | **str** | The status of the custom payment method type.  | [optional] 
**sub_type_field** | **str** | A field available in the Payment Method data source export and Data Query for filtering data.  | [optional] 
**tenant_id** | **str** | Zuora tenant ID. If multi-entity is enabled in your tenant, this is the ID of the parent tenant of all the sub entities.  | [optional] 
**user_reference_id_field** | **str** | A field available in the Payment Method data source export and Data Query for filtering data.  | [optional] 
**version** | **str** | The time when the custom payment method type was first published.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


