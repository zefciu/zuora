# CreatePaymentMethodCardholderInfo

Container for cardholder information. If provided, Zuora will only use this information for this card. Otherwise, Zuora will use the account''s existing bill-to contact information for this card. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | First address line, 255 characters or less.  | [optional] 
**address_line2** | **str** | Second address line, 255 characters or less.  | [optional] 
**card_holder_name** | **str** | The card holder&#39;s full name as it appears on the card, e.g., \&quot;John J Smith\&quot;, 50 characters or less.  | 
**city** | **str** | City, 40 characters or less.  | [optional] 
**country** | **str** | Country, must be a valid country name or abbreviation.  | [optional] 
**email** | **str** | Card holder&#39;s email address, 80 characters or less.  | [optional] 
**phone** | **str** | Phone number, 40 characters or less.  | [optional] 
**state** | **str** | State; must be a valid state name or 2-character abbreviation.  | [optional] 
**zip_code** | **str** | Zip code, 20 characters or less.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


