# GETSubscriptionTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**auto_renew** | **bool** | If &#x60;true&#x60;, the subscription automatically renews at the end of the term. Default is &#x60;false&#x60;.  | [optional] 
**contract_effective_date** | **date** | Effective contract date for this subscription, as yyyy-mm-dd.  | [optional] 
**contracted_mrr** | **float** | Monthly recurring revenue of the subscription.  | [optional] 
**current_term** | **int** | The length of the period for the current subscription term.  | [optional] 
**current_term_period_type** | **str** | The period type for the current subscription term.  Values are:  * &#x60;Month&#x60; (default) * &#x60;Year&#x60; * &#x60;Day&#x60; * &#x60;Week&#x60;  | [optional] 
**customer_acceptance_date** | **date** | The date on which the services or products within a subscription have been accepted by the customer, as yyyy-mm-dd.  | [optional] 
**externally_managed_by** | **str** | An enum field on the Subscription object to indicate the name of a third-party store. This field is used to represent subscriptions created through third-party stores.  | [optional] 
**id** | **str** | Subscription ID.  | [optional] 
**initial_term** | **int** | The length of the period for the first subscription term.  | [optional] 
**initial_term_period_type** | **str** | The period type for the first subscription term.  Values are:  * &#x60;Month&#x60; (default) * &#x60;Year&#x60; * &#x60;Day&#x60; * &#x60;Week&#x60;  | [optional] 
**invoice_owner_account_id** | **str** |  | [optional] 
**invoice_owner_account_name** | **str** |  | [optional] 
**invoice_owner_account_number** | **str** |  | [optional] 
**invoice_separately** | **str** | Separates a single subscription from other subscriptions and creates an invoice for the subscription.   If the value is &#x60;true&#x60;, the subscription is billed separately from other subscriptions. If the value is &#x60;false&#x60;, the subscription is included with other subscriptions in the account invoice.  | [optional] 
**notes** | **str** | A string of up to 65,535 characters.  | [optional] 
**order_number** | **str** | The order number of the order in which the changes on the subscription are made.   **Note:** This field is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). We will investigate your use cases and data before enabling this feature for you.  | [optional] 
**rate_plans** | [**list[GETSubscriptionRatePlanType]**](GETSubscriptionRatePlanType.md) | Container for rate plans.  | [optional] 
**renewal_setting** | **str** | Specifies whether a termed subscription will remain &#x60;TERMED&#x60; or change to &#x60;EVERGREEN&#x60; when it is renewed.   Values are:  * &#x60;RENEW_WITH_SPECIFIC_TERM&#x60; (default) * &#x60;RENEW_TO_EVERGREEN&#x60;  | [optional] 
**renewal_term** | **int** | The length of the period for the subscription renewal term.  | [optional] 
**renewal_term_period_type** | **str** | The period type for the subscription renewal term.  Values are:  * &#x60;Month&#x60; (default) * &#x60;Year&#x60; * &#x60;Day&#x60; * &#x60;Week&#x60;  | [optional] 
**revision** | **str** | An auto-generated decimal value uniquely tagged with a subscription. The value always contains one decimal place, for example, the revision of a new subscription is 1.0. If a further version of the subscription is created, the revision value will be increased by 1. Also, the revision value is always incremental regardless of deletion of subscription versions.  | [optional] 
**service_activation_date** | **date** | The date on which the services or products within a subscription have been activated and access has been provided to the customer, as yyyy-mm-dd  | [optional] 
**status** | **str** | Subscription status; possible values are:  * &#x60;Draft&#x60; * &#x60;Pending Activation&#x60; * &#x60;Pending Acceptance&#x60; * &#x60;Active&#x60; * &#x60;Cancelled&#x60; * &#x60;Suspended&#x60;  | [optional] 
**subscription_end_date** | **date** | The date when the subscription term ends, where the subscription ends at midnight the day before. For example, if the &#x60;subscriptionEndDate&#x60; is 12/31/2016, the subscriptions ends at midnight (00:00:00 hours) on 12/30/2016. This date is the same as the term end date or the cancelation date, as appropriate.  | [optional] 
**subscription_number** | **str** |  | [optional] 
**subscription_start_date** | **date** | Date the subscription becomes effective.  | [optional] 
**term_end_date** | **date** | Date the subscription term ends. If the subscription is evergreen, this is null or is the cancellation date (if one has been set).  | [optional] 
**term_start_date** | **date** | Date the subscription term begins. If this is a renewal subscription, this date is different from the subscription start date.  | [optional] 
**term_type** | **str** | Possible values are: &#x60;TERMED&#x60;, &#x60;EVERGREEN&#x60;.  | [optional] 
**total_contracted_value** | **float** | Total contracted value of the subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


