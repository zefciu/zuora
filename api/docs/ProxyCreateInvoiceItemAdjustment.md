# ProxyCreateInvoiceItemAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** |  The accounting code for the invoice item. Accounting codes group transactions that contain similar accounting attributes. **Character limit**: 100 **Values**: inherited from &#x60;InvoiceItem.AccountingCode&#x60;  | [optional] 
**adjustment_date** | **date** |  The date when the invoice item adjustment is applied, in &#x60;yyyy-mm-dd&#x60; format. This date must be the same as the invoice&#39;s date or later. **Character limit**: 29  | 
**adjustment_number** | **str** |  A unique string to identify an individual invoice item adjustment. **Character limit**: 255 **Values**: automatically generated  | [optional] 
**amount** | **float** |  The amount of the invoice item adjustment. The value of Amount must be positive. Use the required parameter Type to either credit or charge (debit) this amount on the invoice. **Character limit**: 16 **Values**: a valid currency amount  | 
**comment** | **str** |  Use this field to record comments about the invoice item adjustment. **Character limit**: 255 **Values**: a string of 255 characters or fewer  | [optional] 
**created_by_id** | **str** |  The user ID of the person who created the invoice item. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**deferred_revenue_account** | **str** |  Records the deferred accounting code in the finance system. This field is in Limited Availability. If you want to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). **Character limit**: 100  **Version notes**: WSDL 63.0+  **Values**: If this field is not passed in, a value from InvoiceItem will be used. | [optional] 
**invoice_id** | **str** |  The ID of the invoice associated with the adjustment. The adjustment invoice item is in this invoice. This field is optional if you specify a value for the &#x60;InvoiceNumber&#x60; field. **Character limit**: 3 **Values**: a valid invoice ID  | 
**invoice_number** | **str** |  The unique identification number for the invoice that contains the invoice item. This field is optional if you specify a value for the &#x60;InvoiceId&#x60; field. **Character limit**: 32 **Values**: a valid invoice number  | 
**reason_code** | **str** |  A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **Values**: a valid reason code  | [optional] 
**recognized_revenue_account** | **str** |  Records the recognized accounting code in the finance system. This field is in Limited Availability. If you want to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). **Character limit**: 100  **Version notes**: WSDL 63.0+  **Values**: If this field is not passed in, a value from InvoiceItem will be used. | [optional] 
**reference_id** | **str** |  A code to reference an object external to Zuora. For example, you can use this field to reference a case number in an external system. **Character limit**: 60 **Values**: a string of 60 characters or fewer  | [optional] 
**source_id** | **str** |  The ID of the item specified in the SourceType field. **Character limit**: 32 **Values**: a valid invoice item ID or taxation item ID  | 
**source_type** | **str** |  The type of adjustment. **Character limit**: 13 **Values**: InvoiceDetail, Tax  | 
**type** | **str** | Indicates whether the adjustment credits or debits the invoice item amount. | 
**invoice_item_adjustment_integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**invoice_item_adjustment_integration_status__ns** | **str** | Status of the invoice item adjustment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**invoice_item_adjustment_sync_date__ns** | **str** | Date when the invoice item adjustment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


