# InvoiceItemPreviewResultTaxationItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_amount** | **float** | The calculated tax amount excluded due to the exemption.  | [optional] 
**id** | **str** | The ID of the taxation item.  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  | [optional] 
**location_code** | **str** | The identifier for the location based on the value of the taxCode field.  | [optional] 
**name** | **str** | The name of the taxation item.  | [optional] 
**tax_amount** | **float** | The amount of the tax applied to the invoice.  | [optional] 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific invoice.  | [optional] 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **str** | The date when the tax is applied to the invoice.  | [optional] 
**tax_rate** | **float** | The tax rate applied to the invoice.  | [optional] 
**tax_rate_description** | **str** | The description of the tax rate.  | [optional] 
**tax_rate_type** | **str** | Enum:\&quot;Percentage\&quot; \&quot;FlatFee\&quot;. The type of the tax rate applied to the invoice.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


