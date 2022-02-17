# OrderLineItemCommonPostOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uom** | **str** | Specifies the units to measure usage.  | [optional] 
**accounting_code** | **str** | The accounting code for the Order Line Item.  | [optional] 
**adjustment_liability_accounting_code** | **str** | The accounting code on the Order Line Item object for customers using [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration).  | [optional] 
**adjustment_revenue_accounting_code** | **str** | The accounting code on the Order Line Item object for customers using [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration).  | [optional] 
**amount_per_unit** | **float** | The actual charged amount per unit for the Order Line Item.  | [optional] 
**bill_target_date** | **date** | The target date for the Order Line Item to be picked up by bill run for billing.  | [optional] 
**contract_asset_accounting_code** | **str** | The accounting code on the Order Line Item object for customers using [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration).  | [optional] 
**contract_liability_accounting_code** | **str** | The accounting code on the Order Line Item object for customers using [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration).  | [optional] 
**contract_recognized_revenue_accounting_code** | **str** | The accounting code on the Order Line Item object for customers using [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration).  | [optional] 
**custom_fields** | **dict(str, object)** | Container for custom fields of an Order Line Item object.  | [optional] 
**deferred_revenue_accounting_code** | **str** | The deferred revenue accounting code for the Order Line Item.  | [optional] 
**description** | **str** | The description of the Order Line Item.  | [optional] 
**item_name** | **str** | The name of the Order Line Item.  | [optional] 
**item_number** | **str** | The number of the Order Line Item. Use this field to specify a custom item number for your Order Line Item. If you are to use this field,  you must set all the item numbers in an order when there are several order line items in the order.  | [optional] 
**item_state** | **str** | The state of an Order Line Item. If you want to generate invoice for order line items, you must set this field to &#x60;SentToBilling&#x60;. For invoice preview, you do not need to set this field.  See [Order Line Item states, Order states, and state transitions](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AB_Order_Line_Item_States_and_Order_States) for more information.  | [optional] 
**item_type** | **str** | The type of the Order Line Item.   | [optional] 
**list_price_per_unit** | **float** | The list price per unit for the Order Line Item.  | [optional] 
**product_code** | **str** | The product code for the Order Line Item.  | [optional] 
**product_rate_plan_charge_id** | **date** | Id of a Product Rate Plan Charge. Only one-time charges are supported.  | [optional] 
**purchase_order_number** | **str** | Used by customers to specify the Purchase Order Number provided by the buyer.  | [optional] 
**quantity** | **float** | The quantity of units, such as the number of authors in a hosted wiki service.  | [optional] 
**recognized_revenue_accounting_code** | **str** | The recognized revenue accounting code for the Order Line Item.  | [optional] 
**related_subscription_number** | **str** | Use this field to relate an order line item to a subscription when you create the order line item.  * To relate an order line item to a new subscription which is yet to create in the same \&quot;Create an order\&quot; call, use this field in combination with the &#x60;subscriptions&#x60; &gt; &#x60;subscriptionNumber&#x60; field in the \&quot;Create an order\&quot; operation. Specify this field to the same value as that of the &#x60;subscriptions&#x60; &gt; &#x60;subscriptionNumber&#x60; field when you make the \&quot;Create an order\&quot; call. * To relate an order line item to an existing subscription, specify this field to the subscription number of the existing subscription.  | [optional] 
**revenue_recognition_rule** | **str** | The Revenue Recognition rule for the Order Line Item.  | [optional] 
**tax_code** | **str** | The tax code for the Order Line Item.  | [optional] 
**tax_mode** | **str** | The tax mode for the Order Line Item.  | [optional] 
**transaction_end_date** | **date** | The date a transaction is completed. The default value of this field is the transaction start date. Also, the value of this field should always equal or be later than the value of the &#x60;transactionStartDate&#x60; field.  | [optional] 
**transaction_start_date** | **date** | The date a transaction starts. The default value of this field is the order date.  | [optional] 
**unbilled_receivables_accounting_code** | **str** | The accounting code on the Order Line Item object for customers using [Zuora Billing - Revenue Integration](https://knowledgecenter.zuora.com/Zuora_Revenue/Zuora_Billing_-_Revenue_Integration).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


