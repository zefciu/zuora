# CreatePaymentMethodBankTransfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **str** | The International Bank Account Number. This field is used to create the SEPA payment method.  | [optional] 
**account_holder_info** | [**CreatePaymentMethodBankTransferAccountHolderInfo**](CreatePaymentMethodBankTransferAccountHolderInfo.md) |  | [optional] 
**account_number** | **str** | The number of the customer&#39;s bank account. Use this field for direct debit payment methods.  | [optional] 
**bank_code** | **str** | The sort code or number that identifies the bank. This is also known as the sort code.   | [optional] 
**branch_code** | **str** | The branch code of the bank used for direct debit.    | [optional] 
**business_identification_code** | **str** | The BIC code used for SEPA.  | [optional] 
**currency_code** | **str** | The currency used for payment method authorization.  If this field is not specified, &#x60;currency&#x60; specified for the account is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.  | [optional] 
**identity_number** | **str** | The identity number used for Bank Transfer.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


