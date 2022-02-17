# DebitMemoItemFromInvoiceItemTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the debit memo item.  | 
**comment** | **str** | Comments about the debit memo item.  **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | [optional] 
**description** | **str** | The description of the debit memo item.  **Note**: This field is only available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | [optional] 
**finance_information** | [**DebitMemoItemFromInvoiceItemTypeAllOfFinanceInformation**](DebitMemoItemFromInvoiceItemTypeAllOfFinanceInformation.md) |  | [optional] 
**invoice_item_id** | **str** | The ID of the invoice item.  | [optional] 
**quantity** | **float** | The number of units for the debit memo item.  | [optional] 
**service_end_date** | **date** | The service end date of the debit memo item.  | [optional] 
**service_start_date** | **date** | The service start date of the debit memo item.   | [optional] 
**sku_name** | **str** | TThe name of the charge associated with the invoice.  | 
**tax_items** | [**list[DebitMemoTaxItemFromInvoiceTaxItemType]**](DebitMemoTaxItemFromInvoiceTaxItemType.md) | Container for taxation items.  | [optional] 
**tax_mode** | **str** | The tax mode of the debit memo item, indicating whether the amount of the debit memo item includes tax.  **Note**: You can set this field to &#x60;TaxInclusive&#x60; only if the &#x60;taxAutoCalculation&#x60; field is set to &#x60;true&#x60;.  If you set &#x60;taxMode&#x60; to &#x60;TaxInclusive&#x60;, you cannot input tax amounts for debit memo items. The corresponding invoice item must use the same tax engine as the debit memo item to calculate tax amounts.  | [optional] [default to 'TaxExclusive']
**unit_of_measure** | **str** | The definable unit that you measure when determining charges.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


