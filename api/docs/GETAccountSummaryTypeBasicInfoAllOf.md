# GETAccountSummaryTypeBasicInfoAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Account number.  | [optional] 
**additional_email_addresses** | **list[str]** | A list of additional email addresses to receive email notifications.  | [optional] 
**balance** | **str** | Current outstanding balance.  | [optional] 
**batch** | **str** | The alias name given to a batch. A string of 50 characters or less.  | [optional] 
**bill_cycle_day** | **str** | Billing cycle day (BCD), the day of the month when a bill run generates invoices for the account.  | [optional] 
**currency** | **str** | A currency as defined in Billing Settings in the Zuora UI.  | [optional] 
**default_payment_method** | [**GETAccountSummaryTypeBasicInfoAllOfDefaultPaymentMethod**](GETAccountSummaryTypeBasicInfoAllOfDefaultPaymentMethod.md) |  | [optional] 
**id** | **str** | Account ID.  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Whether the customer wants to receive invoices through email.   | [optional] 
**invoice_delivery_prefs_print** | **bool** | Whether the customer wants to receive printed invoices, such as through postal mail.  | [optional] 
**last_invoice_date** | **date** | Date of the most recent invoice for the account; null if no invoice has ever been generated.  | [optional] 
**last_payment_amount** | **str** | Amount of the most recent payment collected for the account; null if no payment has ever been collected.  | [optional] 
**last_payment_date** | **date** | Date of the most recent payment collected for the account. Null if no payment has ever been collected.  | [optional] 
**name** | **str** | Account name.  | [optional] 
**status** | **str** | Account status; possible values are: &#x60;Active&#x60;, &#x60;Draft&#x60;, &#x60;Canceled&#x60;.  | [optional] 
**tags** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


