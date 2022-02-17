# ProxyModifyInvoiceItemAdjustmentAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_code** | **str** |  A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **Values**: a valid reason code  | [optional] 
**status** | **str** |  The status of the invoice item adjustment. This field is required in the Query call, but is automatically generated in other calls. **Character limit**: 9 **Values**: Canceled, Processed  | [optional] 
**transferred_to_accounting** | **str** | Indicates the status of the adjustment&#39;s transfer to an external accounting system, such as NetSuite.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


