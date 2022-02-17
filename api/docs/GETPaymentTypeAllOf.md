# GETPaymentTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Customer account ID.  | [optional] 
**account_name** | **str** | Customer account name.  | [optional] 
**account_number** | **str** | Customer account number.  | [optional] 
**amount** | **str** | Payment amount.  | [optional] 
**effective_date** | **date** | Effective payment date as _yyyy-mm-dd_.  | [optional] 
**gateway_transaction_number** | **str** | Transaction ID from payment gateway.  | [optional] 
**id** | **str** | PaymentID.  | [optional] 
**paid_invoices** | [**list[GETPaidInvoicesType]**](GETPaidInvoicesType.md) | Information about one or more invoices to which this payment was applied:  | [optional] 
**payment_method_id** | **str** | Payment method.  | [optional] 
**payment_number** | **str** | Unique payment number.  | [optional] 
**status** | **str** | Possible values are: &#x60;Draft&#x60;, &#x60;Processing&#x60;, &#x60;Processed&#x60;, &#x60;Error&#x60;, &#x60;Voided&#x60;, &#x60;Canceled&#x60;, &#x60;Posted.  | [optional] 
**type** | **str** | Possible values are: &#x60;External&#x60;, &#x60;Electronic&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


