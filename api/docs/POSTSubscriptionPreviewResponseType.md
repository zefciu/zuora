# POSTSubscriptionPreviewResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Invoice amount.  | [optional] 
**amount_without_tax** | **float** | Invoice amount minus tax.  | [optional] 
**charge_metrics** | [**POSTSubscriptionPreviewResponseTypeChargeMetrics**](POSTSubscriptionPreviewResponseTypeChargeMetrics.md) |  | [optional] 
**contracted_mrr** | **float** | Monthly recurring revenue of the subscription.  | [optional] 
**credit_memo** | [**POSTSubscriptionPreviewResponseTypeCreditMemo**](POSTSubscriptionPreviewResponseTypeCreditMemo.md) |  | [optional] 
**invoice** | [**POSTSubscriptionPreviewResponseTypeInvoice**](POSTSubscriptionPreviewResponseTypeInvoice.md) |  | [optional] 
**invoice_items** | [**list[POSTSubscriptionPreviewInvoiceItemsType]**](POSTSubscriptionPreviewInvoiceItemsType.md) | Container for invoice items.  | [optional] 
**invoice_target_date** | **date** | Date through which charges are calculated on the invoice, as yyyy-mm-dd.  **Note:** This field is only available if you do not specify the Zuora REST API minor version or specify the minor version to 186.0, 187.0, 188.0, 189.0, and 196.0. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**target_date** | **date** | Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.  **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**tax_amount** | **float** | Tax amount on the invoice.  | [optional] 
**total_contracted_value** | **float** | Total contracted value of the subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


