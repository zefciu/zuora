# GETAccountTypeBasicInfoAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Account number.  | [optional] 
**batch** | **str** | The alias name given to a batch. A string of 50 characters or less.  | [optional] 
**communication_profile_id** | **str** | ID of a communication profile.  | [optional] 
**credit_memo_template_id** | **str** | **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the credit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.  | [optional] 
**crm_id** | **str** | CRM account ID for the account, up to 100 characters.  | [optional] 
**currency** | **str** | A currency as defined in Billing Settings in the Zuora UI.  | [optional] 
**debit_memo_template_id** | **str** | **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the debit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.  | [optional] 
**id** | **str** | Account ID.  | [optional] 
**invoice_template_id** | **str** | Invoice template ID, configured in Billing Settings in the Zuora UI.  | [optional] 
**name** | **str** | Account name.  | [optional] 
**notes** | **str** | Notes associated with the account, up to 65,535 characters.  | [optional] 
**parent_id** | **str** | Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled. | [optional] 
**sales_rep** | **str** | The name of the sales representative associated with this account, if applicable. Maximum of 50 characters. | [optional] 
**sequence_set_id** | **str** | The ID of the billing document sequence set that is assigned to the customer account.   | [optional] 
**status** | **str** | Account status; possible values are: &#x60;Active&#x60;, &#x60;Draft&#x60;, &#x60;Canceled&#x60;.  | [optional] 
**tags** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


