# GETCreditMemoItemTypewithSuccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo item. For tax-inclusive credit memo items, the amount indicates the credit memo item amount including tax. For tax-exclusive credit memo items, the amount indicates the credit memo item amount excluding tax.  | [optional] 
**amount_without_tax** | **float** | The credit memo item amount excluding tax.  | [optional] 
**applied_amount** | **float** | The applied amount of the credit memo item.  | [optional] 
**applied_to_item_id** | **str** | The unique ID of the credit memo item that the discount charge is applied to.  | [optional] 
**comment** | **str** | Comments about the credit memo item.  **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the credit memo item.  | [optional] 
**created_date** | **datetime** | The date and time when the credit memo item was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**credit_from_item_id** | **str** | The ID of the credit from item.  | [optional] 
**credit_from_item_source** | **str** | The type of the credit from item.  | [optional] 
**credit_tax_items** | [**list[GETCMTaxItemType]**](GETCMTaxItemType.md) | Container for the taxation items of the credit memo item.   **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;239.0&#x60; or later.  | [optional] 
**description** | **str** | The description of the credit memo item.  **Note**: This field is only available if you set the &#x60;zuora-version&#x60; request header to &#x60;257.0&#x60; or later.  | [optional] 
**finance_information** | [**GETCreditMemoItemTypewithSuccessAllOfFinanceInformation**](GETCreditMemoItemTypewithSuccessAllOfFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the credit memo item.  | [optional] 
**processing_type** | **str** | The kind of the charge for the credit memo item. Its possible values are &#x60;Charge&#x60; and &#x60;Discount&#x60;.   | [optional] 
**quantity** | **float** | The number of units for the credit memo item.  | [optional] 
**refund_amount** | **float** | The amount of the refund on the credit memo item.  | [optional] 
**service_end_date** | **date** | The service end date of the credit memo item.   | [optional] 
**service_start_date** | **date** | The service start date of the credit memo item.  | [optional] 
**sku** | **str** | The SKU for the product associated with the credit memo item.  | [optional] 
**sku_name** | **str** | The name of the SKU.  | [optional] 
**source_item_id** | **str** | The ID of the source item.  - If the value of the &#x60;sourceItemType&#x60; field is &#x60;SubscriptionComponent&#x60; , the value of this field is the ID of the corresponding rate plan charge. - If the value of the &#x60;sourceItemType&#x60; field is &#x60;InvoiceDetail&#x60;, the value of this field is the ID of the corresponding invoice item. - If the value of the &#x60;sourceItemType&#x60; field is &#x60;ProductRatePlanCharge&#x60; , the value of this field is the ID of the corresponding product rate plan charge.  | [optional] 
**source_item_type** | **str** | The type of the source item.  - If a credit memo is not created from an invoice or a product rate plan charge, the value of this field is &#x60;SubscriptionComponent&#x60;.  - If a credit memo is created from an invoice, the value of this field is &#x60;InvoiceDetail&#x60;. - If a credit memo is created from a product rate plan charge, the value of this field is &#x60;ProductRatePlanCharge&#x60;.                | [optional] 
**subscription_id** | **str** | The ID of the subscription associated with the credit memo item.  | [optional] 
**tax_mode** | **str** | The tax mode of the credit memo item, indicating whether the amount of the credit memo item includes tax.  | [optional] 
**taxation_items** | [**GETCreditMemoItemTypeAllOfTaxationItems**](GETCreditMemoItemTypeAllOfTaxationItems.md) |  | [optional] 
**unapplied_amount** | **float** | The unapplied amount of the credit memo item.  | [optional] 
**unit_of_measure** | **str** | The units to measure usage.  | [optional] 
**unit_price** | **float** | The per-unit price of the credit memo item.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the credit memo item.  | [optional] 
**updated_date** | **datetime** | The date and time when the credit memo item was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


