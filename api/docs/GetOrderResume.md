# GetOrderResume

Information about an order action of type `Resume`. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extends_term** | **bool** | Specifies whether to extend the subscription term by the length of time the suspension is in effect. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  | [optional] 
**resume_date** | **date** | The resume date when the resumption takes effect.  | [optional] 
**resume_periods** | **int** | This field is applicable only when the &#x60;resumePolicy&#x60; field is set to &#x60;FixedPeriodsFromToday&#x60; or &#x60;FixedPeriodsFromSuspendDate&#x60;. It must be used together with the &#x60;resumePeriodsType&#x60; field. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  The total number of the periods used to specify when a subscription resumption takes effect. The subscription resumption will take place after the specified time frame (&#x60;suspendPeriods&#x60; multiplied by &#x60;suspendPeriodsType&#x60;) from today&#39;s date.   | [optional] 
**resume_periods_type** | **str** | This field is applicable only when the &#x60;resumePolicy&#x60; field is set to &#x60;FixedPeriodsFromToday&#x60; or &#x60;FixedPeriodsFromSuspendDate&#x60;. It must be used together with the &#x60;resumePeriods&#x60; field. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  The period type used to specify when a subscription resumption takes effect. The subscription suspension will take place after the specified time frame (&#x60;suspendPeriods&#x60; multiplied by &#x60;suspendPeriodsType&#x60;) from today&#39;s date.   | [optional] 
**resume_policy** | **str** | Resume methods. Specify a way to resume a subscription. See [Resume Date](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/Resume_a_Subscription#Resume_Date) for more information. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  If &#x60;SuspendDate&#x60; is specfied, the resumption will take place on the same day as the suspension.   | [optional] 
**resume_specific_date** | **date** | This field is applicable only when the &#x60;resumePolicy&#x60; field is set to &#x60;SpecificDate&#x60;. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  A specific date when the subscription resumption takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription suspension date.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


