# JobResult

**Note:** The schema of the `result` nested field is the same as the response body schema of either the [\"Create an order\"](https://www.zuora.com/developer/api-reference/#operation/POST_Order) or the [\"Preview an order\"](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrder) operation, depending on the purpose of the job.  The following schema for the nested `result` field is defined as the response body schema of \"Create an order\". See [Preview an Order](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrder) for the response body schema of \"Preview an order\".  
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_id** | **str** | The Id of the process that handle the operation.  | [optional] 
**reasons** | [**list[CommonResponseTypeReasons]**](CommonResponseTypeReasons.md) |  | [optional] 
**success** | **bool** | Indicates whether the call succeeded.  | [optional] 
**account_id** | **str** | The account ID for the order. This field is returned only when the &#x60;returnIds&#x60; query parameter in the \&quot;Create an order asynchronously\&quot; operation is set to &#x60;true&#x60;. | [optional] 
**account_number** | **str** | The account number for the order. | [optional] 
**credit_memo_ids** | **list[str]** | An array of the credit memo IDs that are generated in the \&quot;Create an order asynchronously\&quot; operation. This field is returned only when the &#x60;returnIds&#x60; query parameter in the \&quot;Create an order asynchronously\&quot; operation is set to &#x60;true&#x60;. | [optional] 
**credit_memo_numbers** | **list[str]** | An array of the credit memo numbers generated in this order request. The credit memo is only available if you have the Invoice Settlement feature enabled. | [optional] 
**invoice_id** | **str** | An array of the invoice IDs that are generated in the \&quot;Create an order asynchronously\&quot; operation. This field is returned only when the &#x60;returnIds&#x60; query parameter in the \&quot;Create an order asynchronously\&quot; operation is set to &#x60;true&#x60;. | [optional] 
**invoice_numbers** | **list[str]** | An array of the invoice numbers generated in this order request. Normally it includes one invoice number only, but can include multiple items when a subscription was tagged as invoice separately. | [optional] 
**order_id** | **str** | The ID of the order created. This field is returned only when the &#x60;returnIds&#x60; query parameter in the \&quot;Create an order asynchronously\&quot; operation is set to &#x60;true&#x60;. | [optional] 
**order_line_items** | [**list[JobResultAllOfOrderLineItems]**](JobResultAllOfOrderLineItems.md) |  | [optional] 
**order_number** | **str** | The order number of the order created. | [optional] 
**paid_amount** | **str** | The total amount collected in this order request. | [optional] 
**payment_id** | **str** | The ID of the payment that is collected in the \&quot;Create an order asynchronously\&quot; operation. This field is returned only when the &#x60;returnIds&#x60; query parameter in the \&quot;Create an order asynchronously\&quot; operation is set to &#x60;true&#x60;. | [optional] 
**payment_number** | **str** | The payment number that collected in this order request. | [optional] 
**ramps** | [**list[JobResultAllOfRamps]**](JobResultAllOfRamps.md) | **Note**: This field is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  The ramp definitions created by this order request.  | [optional] 
**status** | **str** | Status of the order. &#x60;Pending&#x60; is only applicable for an order that contains a &#x60;CreateSubscription&#x60; order action. | [optional] 
**subscription_ids** | **list[str]** | Container for the IDs of the subscriptions in the order. This field is returned only when the &#x60;returnIds&#x60; query parameter in the \&quot;Create an order asynchronously\&quot; operation is set to &#x60;true&#x60;. | [optional] 
**subscription_numbers** | **list[str]** | **Note:** This field is in Zuora REST API version control. Supported minor versions are 222.4 or earlier. To use this field in the method, you must set the &#x60;zuora-version&#x60; parameter to the minor version number in the request header.  Container for the subscription numbers of the subscriptions in an order.  | [optional] 
**subscriptions** | [**list[JobResultAllOfSubscriptions]**](JobResultAllOfSubscriptions.md) | **Note:** This field is in Zuora REST API version control. Supported minor versions are 223.0 or later. To use this field in the method, you must set the &#x60;zuora-version&#x60; parameter to the minor version number in the request header.  Container for the subscription numbers and statuses in an order.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


