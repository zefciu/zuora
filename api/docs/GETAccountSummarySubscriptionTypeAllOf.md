# GETAccountSummarySubscriptionTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew** | **bool** | If &#x60;true&#x60;, auto-renew is enabled. If &#x60;false&#x60;, auto-renew is disabled.  | [optional] 
**id** | **str** | Subscription ID.  | [optional] 
**initial_term** | **str** | Duration of the initial subscription term in whole months.   | [optional] 
**rate_plans** | [**list[GETAccountSummarySubscriptionRatePlanType]**](GETAccountSummarySubscriptionRatePlanType.md) | Container for rate plans for this subscription.  | [optional] 
**renewal_term** | **str** | Duration of the renewal term in whole months.  | [optional] 
**status** | **str** | Subscription status; possible values are: &#x60;Draft&#x60;, &#x60;PendingActivation&#x60;, &#x60;PendingAcceptance&#x60;, &#x60;Active&#x60;, &#x60;Cancelled&#x60;, &#x60;Expired&#x60;.  | [optional] 
**subscription_number** | **str** | Subscription Number.  | [optional] 
**subscription_start_date** | **date** | Subscription start date.  | [optional] 
**term_end_date** | **date** | End date of the subscription term. If the subscription is evergreen, this is either null or equal to the cancellation date, as appropriate.  | [optional] 
**term_start_date** | **date** | Start date of the subscription term. If this is a renewal subscription, this date is different than the subscription start date.  | [optional] 
**term_type** | **str** | Possible values are: &#x60;TERMED&#x60;, &#x60;EVERGREEN&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


