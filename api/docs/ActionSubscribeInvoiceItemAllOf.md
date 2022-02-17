# ActionSubscribeInvoiceItemAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** |  The accounting code for the item&#39;s charge. Accounting codes group transactions that contain similar accounting attributes.   **Character limit**: 100   **Values**: inherited from &#x60;RatePlanCharge.AccountingCode&#x60;  | [optional] 
**applied_to_charge_number** | **str** |  The charge number that the discount charge is applied to. This field is only for the invoice items that are discount charges. This field is only returned in subscription previews. This field will be returned in the response if you specify the charge number in the rate plan charges in the request.  **Character limit**: 32  **Values**: inherited from &#x60;RatePlanCharge.ChargeNumber&#x60; for the charge associated with the invoice item that the discount charge is applied to  | [optional] 
**applied_to_invoice_item_id** | **str** |  Associates a discount invoice item to a specific invoice item.  **Character limit**: 32  **Values**: inherited from the ID of the charge that a discount applies to  | [optional] 
**charge_amount** | **float** |  The amount being charged for the invoice item. This amount doesn&#39;t include taxes regardless if the charge&#39;s tax mode is inclusive or exclusive.   **Character limit**:   **Values**: automatically calculated from multiple fields in multiple objects  | [optional] 
**charge_date** | **datetime** |  The date when the Invoice Item is created .   **Character limit**: 29   **Values**: automatically generated  | [optional] 
**charge_description** | **str** |  A description of the invoice item&#39;s charge.   **Character limit**: 500   **Values**: inherited from &#x60;RatePlanCharge.Description&#x60;  | [optional] 
**charge_id** | **str** |  The ID of the rate plan charge that is associated with this invoice item upon object creation.   **Character limit**: 32   **Values**: inherited from &#x60;RatePlanCharge.Id&#x60;  | [optional] 
**charge_name** | **str** |  The name of the invoice item&#39;s charge. **Character limi**t: 50 **Values: **inherited from &#x60;RatePlanCharge.Name&#x60;  | [optional] 
**charge_number** | **str** |  The unique identifier of the invoice item&#39;s charge. **Character limit:** 50 **Values:** inherited from &#x60;RatePlanCharge.ChargeNumber&#x60;  | [optional] 
**charge_type** | **str** |  Specifies the type of charge.   **Character limit**: 9   **Values**: one of the following:  - &#x60;OneTime&#x60; - &#x60;Recurring&#x60; - &#x60;Usage&#x60;  | [optional] 
**created_by_id** | **str** |  The user ID of the person who created the invoice item.   **Character limit**: 32   **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date the invoice item was created. **Character limit:** 29   **Values**: automatically generated  | [optional] 
**invoice_id** | **str** |  The ID of the invoice that&#39;s associated with this invoice item.   **Character limit**: 32   **Values**: inherited from &#x60;Invoice.Id&#x60;  | [optional] 
**processing_type** | **float** |  Identifies the kind of charge where 0 is a charge, 1 is a discount, 2 is a prepayment, and 3 is a tax. The returned value is text not decimal on data sources.   **Character limit**: **Values: **  - 0: charge - 1: discount - 2: prepayment - 3: tax  | [optional] 
**product_description** | **str** |  A description of the product associated with this invoice item.   **Character limit**: 500   **Values**: inherited from &#x60;Product.Description&#x60;  | [optional] 
**product_id** | **str** |  The ID of the product associated with this invoice item.   **Character limit**: 32   **Values**: inherited from &#x60;Product.Id&#x60;  | [optional] 
**product_name** | **str** |  The name of the product associated with this invoice item.   **Character limit**: 255 **Values: **inherited from &#x60;Product.Name&#x60;  | [optional] 
**product_rate_plan_charge_id** | **str** |  The ID of the rate plan charge that&#39;s associated with this invoice item.   **Character limit**: 32   **Values**: inherited from &#x60;ProductRatePlanCharge.Id&#x60; You cannot &#x60;query &#x60; for this field. Only the s&#x60;ubscribe &#x60; preview and the &#x60;amend &#x60; preview calls will return the value of this field in the response. | [optional] 
**quantity** | **float** |  The number of units for this invoice item.    **Values**: inherited from &#x60;RatePlanCharge.Quantity&#x60;  | [optional] 
**rate_plan_charge_id** | **str** |  The ID of the rate plan charge that&#39;s associated with this invoice item.   **Character limit**: 32   **Values**: inherited from &#x60;RatePlanCharge.Id&#x60;  | [optional] 
**rev_rec_code** | **str** |  Associates this invoice item with a specific revenue recognition code.   **Character limit**: 32   **Values**: inherited from &#x60;ProductRatePlanCharge.RevRecCode&#x60;  | [optional] 
**rev_rec_start_date** | **date** |  The date when revenue recognition is triggered.   **Character limit**: 29   **Values**: generated from &#x60;InvoiceItem.RevRecTriggerCondition&#x60;  | [optional] 
**rev_rec_trigger_condition** | **str** |  Specifies when revenue recognition begins based on a triggering event.   **Character limit**:   **Values**: inherited from &#x60;ProductRatePlanCharge&#x60;.&#x60;RevRecTriggerCondition&#x60;  | [optional] 
**sku** | **str** |  The unique SKU for the product associated with this invoice item.   **Character limit**: 255   **Values**: inherited from &#x60;Product.SKU&#x60;  | [optional] 
**service_end_date** | **date** |  The end date of the service period associated with this invoice item. Service ends one second before the date in this value.   **Character limit**: 29   **Values**: automatically generated  | [optional] 
**service_start_date** | **date** |  The start date of the service period associated with this invoice item. If the associated charge is a one-time fee, then this date is the date of that charge. **Character limit:** 29   **Values**: automatically generated  | [optional] 
**subscription_id** | **str** |  The ID of the subscription associated with the invoice item.   **Character limit**: 32   **Values**: inherited from &#x60;Subscription.Id&#x60;  | [optional] 
**subscription_number** | **str** |  The number of the subscription associated with the invoice item.   **Character limit**:   **Values**:  | [optional] 
**tax_amount** | **float** |  The amount of tax applied to the invoice item&#39;s charge.   **Character limit**:   **Values**: calculated from multiple fields in the ProductRatePlanCharge object  | [optional] 
**tax_code** | **str** |  Specifies the tax code for taxation rules.   **Character limit**: 6   **Values**: inherited from &#x60;ProductRatePlanCharge.TaxCode&#x60;  | [optional] 
**tax_exempt_amount** | **float** |  The calculated tax amount excluded due to the exemption.   **Character limit**:   **Values**: calculated from multiple fields in the ProductRatePlanCharge object  | [optional] 
**tax_mode** | **str** |  The tax mode of the invoice item.   **Character limit**: 12   **Values**: &#x60;TaxExclusive&#x60;, &#x60;TaxInclusive&#x60;  | [optional] 
**uom** | **str** |  Specifies the units to measure usage. Units of measure are configured in the web-based UI: **Z-Billing &gt; Settings**  **Character limit**:   **Values**: inherited from &#x60;ProductRatePlanCharge.UOM&#x60;  | [optional] 
**unit_price** | **float** |  The per-unit price of the invoice item.   **Character limit**:   **Values**: calculated from multiple fields in ProductRatePlanCharge and ProductRatePlanChargeTier objets  | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the invoice item.   **Character limit**: 32   **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the invoice item was last updated.   **Character limit**: 29   **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


