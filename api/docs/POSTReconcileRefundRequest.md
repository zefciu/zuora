# POSTReconcileRefundRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action of the refund reconciliation.   - &#x60;settle&#x60;: Sets the gatewayState to \&quot;Settled\&quot; and returns the refund object as response.   - &#x60;reject&#x60;: Sets the gatewayState to \&quot;FailedToSettle\&quot; and handle the event according to the settings configured in the Gateway Reconciliation Configuration in Payments Settings through Zuora UI. See [Configure how to handle refund rejected events](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/M_Payment_Gateways/Gateway_Reconciliation#Configure_how_to_handle_refund_rejected_events) for details.  | [optional] 
**action_date** | **str** | The date and time of the refund reconciliation action, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**gateway_reconciliation_reason** | **str** | The reason of gateway reconciliation.  | [optional] 
**gateway_reconciliation_status** | **str** | The status of gateway reconciliation.  | [optional] 
**payout_id** | **str** | The payout ID of the refund from the gateway side.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


