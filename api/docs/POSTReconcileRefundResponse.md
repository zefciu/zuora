# POSTReconcileRefundResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account that the refund is for.  | [optional] 
**amount** | **float** | The total amount of the refund.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the transaction was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the refund.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the refund.  | [optional] 
**created_date** | **datetime** | The date and time when the refund is created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**credit_memo_id** | **str** | The ID of the credit memo that is refunded.  | [optional] 
**finance_information** | [**POSTReconcileRefundResponseFinanceInformation**](POSTReconcileRefundResponseFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the refund.  | [optional] 
**gateway_reconciliation_reason** | **str** | The reason of gateway reconciliation.  | [optional] 
**gateway_reconciliation_status** | **str** | The status of gateway reconciliation.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the refund. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the refund. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the refund in the gateway; used for reconciliation.  | [optional] 
**id** | **str** | The ID of the refund.  | [optional] 
**marked_for_submission_on** | **datetime** | The date and time when a refund was marked and waiting for batch submission to the payment process, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**method_type** | **str** | How an external refund was issued to a customer.   | [optional] 
**number** | **str** | The unique identification number of the refund. For example, R-00000001.  | [optional] 
**payment_id** | **str** | The ID of the payment that is refunded.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the refund.  | [optional] 
**payment_method_snapshot_id** | **str** | The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.  | [optional] 
**payout_id** | **str** | The payout ID of the refund from the gateway side.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction.        | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.  | [optional] 
**refund_date** | **date** | The date when the refund takes effect, in &#x60;yyyy-mm-dd&#x60; format. For example, 2020-03-01.         | [optional] 
**refund_transaction_time** | **datetime** | The date and time when the refund was issued, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**second_refund_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional refund.   | [optional] 
**settled_on** | **datetime** | The date and time when the transaction is settled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps Zuora to other gateways.  | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps Zuora to other gateways.            | [optional] 
**status** | **str** | The status of the refund.  | [optional] 
**submitted_on** | **datetime** | The date and time when the refund was submitted, in yyyy-mm-dd hh:mm:ss format.  | [optional] 
**success** | **bool** | Indicates if the request is processed successfully. | [optional] 
**type** | **str** | The type of the refund.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the refund.  | [optional] 
**updated_date** | **datetime** | The date and time when the refund was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


