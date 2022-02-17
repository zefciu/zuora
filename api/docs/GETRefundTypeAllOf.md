# GETRefundTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account associated with this refund. Zuora associates the refund automatically with the account from the associated payment or credit memo.  | [optional] 
**amount** | **float** | The total amount of the refund.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the refund was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the refund.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the refund.  | [optional] 
**created_date** | **datetime** | The date and time when the refund was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**credit_memo_id** | **str** | The ID of the credit memo that is refunded.  | [optional] 
**finance_information** | [**GETRefundCreditMemoTypeAllOfFinanceInformation**](GETRefundCreditMemoTypeAllOfFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the refund.  | [optional] 
**gateway_reconciliation_reason** | **str** | The reason of gateway reconciliation.  | [optional] 
**gateway_reconciliation_status** | **str** | The status of gateway reconciliation.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the refund. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the refund. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the refund in the gateway.  | [optional] 
**id** | **str** | The ID of the refund.  | [optional] 
**marked_for_submission_on** | **datetime** | The date and time when a refund was marked and waiting for batch submission to the payment process, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.   | [optional] 
**method_type** | **str** | How an external refund was issued to a customer.   | [optional] 
**number** | **str** | The unique identification number of the refund.  | [optional] 
**payment_id** | **str** | The ID of the payment that is refunded.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the refund.  | [optional] 
**payment_method_snapshot_id** | **str** | The unique ID of the payment method snapshot, which is a copy of the particular payment method used in a transaction.  | [optional] 
**payout_id** | **str** | The payout ID of the refund from the gateway side.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.  | [optional] 
**refund_date** | **date** | The date when the refund takes effect, in &#x60;yyyy-mm-dd&#x60; format. For example, 2017-03-01.  | [optional] 
**refund_transaction_time** | **datetime** | The date and time when the refund was issued, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**second_refund_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional transaction for the refund. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**settled_on** | **datetime** | The date and time when the refund was settled in the payment processor, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. This field is used by the Spectrum gateway only and not applicable to other gateways.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps Zuora to other gateways.  | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps Zuora to other gateways.  | [optional] 
**status** | **str** | The status of the refund.   | [optional] 
**submitted_on** | **datetime** | The date and time when the refund was submitted, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully. | [optional] 
**type** | **str** | The type of the refund.   | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the refund.  | [optional] 
**updated_date** | **datetime** | The date and time when the refund was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


