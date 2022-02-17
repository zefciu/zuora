# PostTaxationItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_amount** | [**BigDecimal**](BigDecimal.md) | The calculated tax amount excluded due to the exemption.  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  | [optional] 
**location_code** | **str** | The identifier for the location based on the value of the &#x60;taxCode&#x60; field.  | [optional] 
**name** | **str** | The name of taxation.  | 
**tax_amount** | [**BigDecimal**](BigDecimal.md) | The amount of the taxation item in the invoice item.  | 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific invoice item.  | 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **date** | The date that the tax is applied to the invoice item, in &#x60;yyyy-mm-dd&#x60; format.  | 
**tax_mode** | **str** | The tax mode of the invoice item, indicating whether the amount of the invoice item includes tax.  | 
**tax_rate** | [**BigDecimal**](BigDecimal.md) | The tax rate applied to the invoice item.  | 
**tax_rate_description** | **str** | The description of the tax rate.  | [optional] 
**tax_rate_type** | **str** | The type of the tax rate applied to the invoice item.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


