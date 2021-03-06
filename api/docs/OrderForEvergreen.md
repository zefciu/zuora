# OrderForEvergreen

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
**order_date** | **str** | The date when the order is signed. All the order actions under this order will use this order date as the contract effective date if no additinal contractEffectiveDate is provided. | [optional] 
**order_number** | **str** | The order number of the order. | [optional] 
**status** | **str** | The status of the order. | [optional] 
**subscriptions** | [**list[OrderForEvergreenSubscriptions]**](OrderForEvergreenSubscriptions.md) | Represents a processed subscription, including the origin request (order actions) that create this version of subscription and the processing result (order metrics). The reference part in the request will be overridden with the info in the new subscription version. | [optional] 
**updated_by** | **str** | The ID of the user who updated this order. | [optional] 
**updated_date** | **str** | The time that the order gets updated in the system (for example, an order description update), in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


