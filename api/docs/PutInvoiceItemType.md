# PutInvoiceItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** | The accounting code associated with the invoice item.  | [optional] 
**adjustment_liability_accounting_code** | **str** | The accounting code for adjustment liability.         **Note**: This field is only available if you have the RevPro Integration feature enabled.   | [optional] 
**adjustment_revenue_accounting_code** | **str** | The accounting code for adjustment revenue.         **Note**: This field is only available if you have the RevPro Integration feature enabled.   | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The amount of the invoice item.   - For tax-inclusive invoice items, the amount indicates the invoice item amount including tax.  - For tax-exclusive invoice items, the amount indicates the invoice item amount excluding tax.  | [optional] 
**charge_date** | **datetime** | The date when the invoice item is charged.  | [optional] 
**charge_name** | **str** | The name of the charge associated with the invoice item.   This field is required if the &#x60;productRatePlanChargeId&#x60; field is not specified in the request.  | [optional] 
**contract_asset_accounting_code** | **str** | The accounting code for contract asset.         **Note**: This field is only available if you have the RevPro Integration feature enabled.   | [optional] 
**contract_liability_accounting_code** | **str** | The accounting code for contract liability.         **Note**: This field is only available if you have the RevPro Integration feature enabled.   | [optional] 
**contract_recognized_revenue_accounting_code** | **str** | The accounting code for contract recognized revenue.         **Note**: This field is only available if you have the RevPro Integration feature enabled.   | [optional] 
**deferred_revenue_accounting_code** | **str** | The accounting code for the deferred revenue, such as Monthly Recurring Liability.  **Note:** This field is only available if you have Zuora Finance enabled.  | [optional] 
**description** | **str** | The description of the invoice item.  | [optional] 
**id** | **str** | The unique ID of the invoice item.  | [optional] 
**item_type** | **str** | The type of the invoice item.  | [optional] 
**purchase_order_number** | **str** | The purchase order number associated the invoice item.  | [optional] 
**quantity** | [**BigDecimal**](BigDecimal.md) | The number of units for the invoice item.  | [optional] 
**recognized_revenue_accounting_code** | **str** | The accounting code for the recognized revenue, such as Monthly Recurring Charges or Overage Charges.  **Note:** This field is only available if you have Zuora Finance enabled.  | [optional] 
**rev_rec_code** | **str** | The revenue recognition code.  | [optional] 
**rev_rec_trigger_condition** | **str** | The date when revenue recognition is triggered.  | [optional] 
**revenue_recognition_rule_name** | **str** | The name of the revenue recognition rule governing the revenue schedule.  **Note:** This field is only available if you have Zuora Finance enabled.  | [optional] 
**service_end_date** | **date** | The service end date of the invoice item.  | [optional] 
**service_start_date** | **date** | The service start date of the invoice item.  | [optional] 
**sku** | **str** | The SKU of the invoice item. The SKU of the invoice item must be different from the SKU of any existing product.  | [optional] 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to the invoice item.  **Note:**  - This field is only available if you have Taxation enabled. - If the values of both &#x60;taxCode&#x60; and &#x60;taxMode&#x60; fields are changed to &#x60;null&#x60; when updating a standalone invoice, the corresponding &#x60;invoiceItems&#x60; &gt; &#x60;taxItems&#x60; field and its nested fields specified in the creation request will be removed.  | [optional] 
**tax_mode** | **str** | The tax mode of the invoice item, indicating whether the amount of the invoice item includes tax.  **Note:**  - This field is only available if you have Taxation enabled. - If the values of both &#x60;taxCode&#x60; and &#x60;taxMode&#x60; fields are changed to &#x60;null&#x60; when updating a standalone invoice, the corresponding &#x60;invoiceItems&#x60; &gt; &#x60;taxItems&#x60; field and its nested fields specified in the creation request will be removed.  | [optional] 
**unbilled_receivables_accounting_code** | **str** | The accounting code for unbilled receivables.         **Note**: This field is only available if you have the RevPro Integration feature enabled.   | [optional] 
**unit_price** | [**BigDecimal**](BigDecimal.md) | The per-unit price of the invoice item.  | [optional] 
**uom** | **str** | The unit of measure.  | [optional] 
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice item&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


