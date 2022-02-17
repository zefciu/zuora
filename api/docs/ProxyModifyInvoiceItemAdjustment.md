# ProxyModifyInvoiceItemAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_code** | **str** |  A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **Values**: a valid reason code  | [optional] 
**status** | **str** |  The status of the invoice item adjustment. This field is required in the Query call, but is automatically generated in other calls. **Character limit**: 9 **Values**: Canceled, Processed  | [optional] 
**transferred_to_accounting** | **str** | Indicates the status of the adjustment&#39;s transfer to an external accounting system, such as NetSuite.  | [optional] 
**invoice_item_adjustment_integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**invoice_item_adjustment_integration_status__ns** | **str** | Status of the invoice item adjustment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**invoice_item_adjustment_sync_date__ns** | **str** | Date when the invoice item adjustment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


