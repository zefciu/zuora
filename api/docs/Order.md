# Order

Represents the order information that will be returned in the GET call.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The ID of the user who created this order. | [optional] 
**created_date** | **str** | The time that the order gets created in the system, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format. | [optional] 
**currency** | **str** | Currency code. | [optional] 
**custom_fields** | **dict(str, object)** | Container for custom fields of an Order object.  | [optional] 
**description** | **str** | A description of the order. | [optional] 
**existing_account_number** | **str** | The account number that this order has been created under. This is also the invoice owner of the subscriptions included in this order. | [optional] 
**order_date** | **date** | The date when the order is signed. All the order actions under this order will use this order date as the contract effective date if no additinal contractEffectiveDate is provided. | [optional] 
**order_line_items** | [**list[OrderLineItemRetrieveOrder]**](OrderLineItemRetrieveOrder.md) | [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) are non subscription based items created by an Order, representing transactional charges such as one-time fees, physical goods, or professional service charges that are not sold as subscription services.   With the Order Line Items feature enabled, you can now launch non-subscription and unified monetization business models in Zuora, in addition to subscription business models.   **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is now generally available to all Zuora customers. You need to enable the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature to access the [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature. As of Zuora Billing Release 313 (November 2021), new customers who onboard on [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) will have the [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items) feature enabled by default. If you are a new customer who onboard on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) and want to enable the [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items) feature, submit a request at [Zuora Global Support](https://support.zuora.com/). If you are an existing [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) or [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) customer and want to enable the [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items) feature, submit a request at [Zuora Global Support](https://support.zuora.com/).          | [optional] 
**order_number** | **str** | The order number of the order. | [optional] 
**status** | **str** | The status of the order. If the order contains any &#x60;Pending Activation&#x60; or &#x60;Pending Acceptance&#x60; subscription, the order status will be &#x60;Pending&#x60;; otherwise the order status is &#x60;Completed&#x60;. | [optional] 
**subscriptions** | [**list[OrderSubscriptions]**](OrderSubscriptions.md) | Represents a processed subscription, including the origin request (order actions) that create this version of subscription and the processing result (order metrics). The reference part in the request will be overridden with the info in the new subscription version. | [optional] 
**updated_by** | **str** | The ID of the user who updated this order. | [optional] 
**updated_date** | **str** | The time that the order gets updated in the system(for example, an order description update), in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


