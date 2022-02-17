# POSTCreateOpenPaymentMethodTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | If this custom payment method type is specific to one entity only, provide the entity UUID in this field. If no entity UUID is provided, the custom payment method type is available to the global entity and all the sub entities in the tenant.  Note: After the custom payment method type is created, you can only update this field to be empty.  | [optional] 
**fields** | [**list[OpenPaymentMethodTypeRequestFields]**](OpenPaymentMethodTypeRequestFields.md) | An array containing field metadata of the custom payment method type.  Notes:   - All the following nested metadata must be provided in the request to define a field.    - At least one field must be defined in the fields array for a custom payment method type.    - Up to 20 fields can be defined in the fields array for a custom payment method type.  | 
**internal_name** | **str** | A string to identify the custom payment method type in the API name of the payment method type.  This field must be alphanumeric, starting with a capital letter, excluding JSON preserved characters such as  * \\ ’ ”. Additionally, &#39;_&#39; or &#39;-&#39; is not allowed.  This field must be unique in a tenant.  This field is used along with the &#x60;tenantId&#x60; field by the system to construct and generate the API name of the custom payment method type in the following way:  &#x60;&lt;internalName&gt;__c_&lt;tenantId&gt;&#x60;  For example, if &#x60;internalName&#x60; is &#x60;AmazonPay&#x60;, and &#x60;tenantId&#x60; is &#x60;12368&#x60;, the API name of the custom payment method type will be &#x60;AmazonPay__c_12368&#x60;.  This field cannot be updated after the creation of the custom payment method type.  | 
**label** | **str** | The label that is used to refer to this type in the Zuora UI.  This value must be alphanumeric, excluding JSON preserved characters such as  * \\ ’ ”   | 
**method_reference_id_field** | **str** | A field available in the Payment Method data source export and Data Query for filtering data. Specify the name of a field that is in the &#x60;fields&#x60; array .  This field cannot be updated after the creation of the custom payment method type.  | 
**sub_type_field** | **str** | A field available in the Payment Method data source export and Data Query for filtering data. Specify the name of a field that is in the &#x60;fields&#x60; array.  This field cannot be updated after the creation of the custom payment method type.  | [optional] 
**tenant_id** | **str** | Zuora tenant ID. If multi-entity is enabled in your tenant, this is the ID of the parent tenant of all the sub entities.  This field cannot be updated after the creation of the custom payment method type.  | 
**user_reference_id_field** | **str** | A field available in the Payment Method data source export and Data Query for filtering data. Specify the name of a field that is in the &#x60;fields&#x60; array.  This field cannot be updated after the creation of the custom payment method type.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


