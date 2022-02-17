# POSTDelayAuthorizeCapture

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account. Either &#x60;accountId&#x60; or &#x60;accountNumber&#x60; is required. | [optional] 
**account_number** | **str** | The number of the customer account. Either &#x60;accountNumber&#x60; or &#x60;accountId&#x60; is required. | [optional] 
**amount** | **float** | The amount of the trasaction. | 
**gateway_order_id** | **str** | The order ID for the specific gateway. | 
**mit_transaction_source** | **str** | Payment transaction source used to differentiate the transaction source in Stored Credential Transaction framework.   - &#x60;C_Unscheduled&#x60;: Cardholder-initiated transaction (CIT) that does not occur on scheduled or regularly occurring dates.   - &#x60;M_Recurring&#x60;: Merchant-initiated transaction (MIT) that occurs at regular intervals.   - &#x60;M_Unscheduled&#x60;: Merchant-initiated transaction (MIT) that does not occur on scheduled or regularly occurring dates.  | [optional] 
**soft_descriptor** | **str** | A text, rendered on a cardholder’s statement, describing a particular product or service purchased by the cardholder. | [optional] 
**soft_descriptor_phone** | **str** | The phone number that relates to the soft descriptor, usually the phone number of customer service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


