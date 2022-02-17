# PUTSubscriptionResponseTypeInvoice

Container for invoices.    **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. Also, the response structure is changed and the following invoice related response fields are moved to this **invoice** container:       * amount    * amountWithoutTax    * taxAmount    * invoiceItems    * targetDate 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Invoice amount. | [optional] 
**amount_without_tax** | **float** | Invoice amount minus tax.  | [optional] 
**invoice_items** | [**list[PUTSubscriptionPreviewInvoiceItemsType]**](PUTSubscriptionPreviewInvoiceItemsType.md) | Container for invoice items.  | [optional] 
**target_date** | **date** | Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.  **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**tax_amount** | **float** | The tax amount of the invoice.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


