# POSTPMMandateInfo

The mandate information for the Credit Card, Credit Card Reference Transaction, ACH, or Bank Transfer payment method.  The following mandate fields are common to all supported payment methods: * `mandateId` * `mandateReason` * `mandateStatus`  The following mandate fields are specific to the ACH and Bank Transfer payment methods: * `mandateReceivedStatus` * `existingMandateStatus` * `mandateCreationDate` * `mandateUpdateDate`  The following mandate fields are specific to the Credit Card payment method: * `mitTransactionId` * `mitProfileAgreedOn` * `mitConsentAgreementRef` * `mitConsentAgreementSrc` * `mitProfileType` * `mitProfileAction` 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existing_mandate_status** | **str** | Indicates whether the mandate is an existing mandate.  | [optional] 
**mandate_creation_date** | **date** | The date on which the mandate was created.  | [optional] 
**mandate_id** | **str** | The mandate ID.  | [optional] 
**mandate_reason** | **str** | The reason of the mandate from the gateway side.  | [optional] 
**mandate_received_status** | **str** | Indicates whether the mandate is received from the gateway  | [optional] 
**mandate_status** | **str** | The status of the mandate from the gateway side.  | [optional] 
**mandate_update_date** | **date** | The date on which the mandate was updated.  | [optional] 
**mit_consent_agreement_ref** | **str** | Reference for the consent agreement that you have established with the customer.    | [optional] 
**mit_consent_agreement_src** | **str** |  | [optional] 
**mit_profile_action** | **str** | Specifies how Zuora activates the stored credential profile. Only applicable if you set the &#x60;status&#x60; field to &#x60;Active&#x60;.  * &#x60;Activate&#x60; (default) - Use this value if you are creating the stored credential profile after receiving the customer&#39;s consent.    Zuora will create the stored credential profile then send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile. If the CIT succeeds, the status of the stored credential profile will be &#x60;Active&#x60;. If the CIT does not succeed, Zuora will not create a stored credential profile.      If the payment gateway does not support the stored credential transaction framework, the status of the stored credential profile will be &#x60;Agreed&#x60;.   * &#x60;Persist&#x60; - Use this value if the stored credential profile represents a stored credential profile in an external system. The status of the payment method&#39;s stored credential profile will be &#x60;Active&#x60;.  | [optional] 
**mit_profile_agreed_on** | **date** | The date on which the stored credential profile is agreed. The date format is &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**mit_profile_type** | **str** | Indicates the type of the stored credential profile.  | [optional] 
**mit_transaction_id** | **str** | Specifies the ID of the transaction. Only applicable if you set the &#x60;mitProfileAction&#x60; field to &#x60;Persist&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


