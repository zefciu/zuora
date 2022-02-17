# PUTAccountTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_email_addresses** | **list[str]** | A list of additional email addresses to receive email notifications. Use commas to separate email addresses.  | [optional] 
**auto_pay** | **bool** | Whether future payments are to be automatically billed when they are due.   | [optional] 
**batch** | **str** | The alias name given to a batch. A string of 50 characters or less.  | [optional] 
**bill_cycle_day** | **int** | Sets the bill cycle day (BCD) for the charge. The BCD determines which day of the month the customer is billed. Values: Any activated system-defined bill cycle day （&#x60;1&#x60;-&#x60;31&#x60;）  | [optional] 
**bill_to_contact** | [**PUTAccountTypeBillToContact**](PUTAccountTypeBillToContact.md) |  | [optional] 
**communication_profile_id** | **str** | The ID of a communication profile.  | [optional] 
**credit_memo_template_id** | **str** | **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the credit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.  | [optional] 
**crm_id** | **str** | CRM account ID for the account, up to 100 characters.  | [optional] 
**debit_memo_template_id** | **str** | **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the debit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.  | [optional] 
**default_payment_method_id** | **str** | ID of the default payment method for the account.  Values: a valid ID for an existing payment method.  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Whether the customer wants to receive invoices through email.   The default value is &#x60;false&#x60;.  | [optional] 
**invoice_delivery_prefs_print** | **bool** | Whether the customer wants to receive printed invoices, such as through postal mail.  The default value is &#x60;false&#x60;.  | [optional] 
**invoice_template_id** | **str** | Invoice template ID, configured in Billing Settings in the Zuora UI.  | [optional] 
**name** | **str** | Account name, up to 255 characters.  | [optional] 
**notes** | **str** | A string of up to 65,535 characters.  | [optional] 
**parent_id** | **str** | Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled. | [optional] 
**payment_gateway** | **str** | The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.  | [optional] 
**payment_term** | **str** | Payment terms for this account. Possible values are &#x60;Due Upon Receipt&#x60;, &#x60;Net 30&#x60;, &#x60;Net 60&#x60;, &#x60;Net 90&#x60;. | [optional] 
**sales_rep** | **str** | The name of the sales representative associated with this account, if applicable. Maximum of 50 characters. | [optional] 
**sequence_set_id** | **str** | The ID of the billing document sequence set to assign to the customer account.   The billing documents to generate for this account will adopt the prefix and starting document number configured in the sequence set.  If a customer account has no assigned billing document sequence set, billing documents generated for this account adopt the prefix and starting document number from the default sequence set.  | [optional] 
**sold_to_contact** | [**PUTAccountTypeSoldToContact**](PUTAccountTypeSoldToContact.md) |  | [optional] 
**tagging** | **str** |  | [optional] 
**tax_info** | [**POSTAccountTypeAllOfTaxInfo**](POSTAccountTypeAllOfTaxInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


