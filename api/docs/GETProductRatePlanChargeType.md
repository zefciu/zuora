# GETProductRatePlanChargeType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_discount_to** | **str** | Specifies where (to what charge type) the discount will be applied. These field values are case-sensitive.  Permissible values: - RECURRING - USAGE - ONETIMERECURRING - ONETIMEUSAGE - RECURRINGUSAGE - ONETIMERECURRINGUSAGE  | [optional] 
**billing_day** | **str** | The bill cycle day (BCD) for the charge. The BCD determines which day of the month or week the customer is billed. The BCD value in the account can override the BCD in this object.  | [optional] 
**billing_period** | **str** | The billing period for the charge. The start day of the billing period is also called the bill cycle day (BCD).  Values: - Month - Quarter - Annual - Semi-Annual - Specific Months - Week - Specific_Weeks  | [optional] 
**billing_period_alignment** | **str** | Aligns charges within the same subscription if multiple charges begin on different dates.  Possible values: - AlignToCharge - AlignToSubscriptionStart - AlignToTermStart  | [optional] 
**billing_timing** | **str** | The billing timing for the charge. You can choose to bill for charges in advance or in arrears.  Values: - In Advance - In Arrears  **Note:** This feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).   | [optional] 
**charge_model_configurations** | [**object**](.md) | This field is for Zuora Internal Use only. See the **pricing** field for the same information as this field. | [optional] 
**default_quantity** | **str** | The default quantity of units.  This field is required if you use a per-unit charge model.  | [optional] 
**description** | **str** | Usually a brief line item summary of the Rate Plan Charge.  | [optional] 
**discount_class** | **str** | The class that the discount belongs to. The discount class defines the order in which discount product rate plan charges are applied.  For more information, see [Manage Discount Classes](https://knowledgecenter.zuora.com/BC_Subscription_Management/Product_Catalog/B_Charge_Models/Manage_Discount_Classes).  | [optional] 
**discount_level** | **str** | The level of the discount.   Values: - RatePlan - Subscription - Account  | [optional] 
**end_date_condition** | **str** | Defines when the charge ends after the charge trigger date. If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.  Values: - Subscription_End - Fixed_Period  | [optional] 
**finance_information** | [**FinanceInformation**](FinanceInformation.md) |  | [optional] 
**formula** | **str** | The pricing formula to calculate the actual rating amount for each usage record.  This field is only available for the usage-based charges that use the Multi-Attribute Pricing charge model. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.  | [optional] 
**id** | **str** | Unique product rate-plan charge ID.  | [optional] 
**included_units** | **str** | Specifies the number of units in the base set of units when the charge model is Overage.  | [optional] 
**list_price_base** | **str** | The list price base for the product rate plan charge.  Values: - Month - Billing Period - Per_Week  | [optional] 
**max_quantity** | **str** | Specifies the maximum number of units for this charge. Use this field and the &#x60;minQuantity&#x60; field to create a range of units allowed in a product rate plan charge.  | [optional] 
**min_quantity** | **str** | Specifies the minimum number of units for this charge. Use this field and the &#x60;maxQuantity&#x60; field to create a range of units allowed in a product rate plan charge.  | [optional] 
**model** | **str** | Charge model which determines how charges are calculated. Charge models must be individually activated in Zuora Billing administration.   Possible values are: - &#x60;FlatFee&#x60; - &#x60;PerUnit&#x60; - &#x60;Overage&#x60; - &#x60;Volume&#x60; - &#x60;Tiered&#x60; - &#x60;TieredWithOverage&#x60; - &#x60;DiscountFixedAmount&#x60; - &#x60;DiscountPercentage&#x60; - &#x60;MultiAttributePricing&#x60; (available only if you have the Multi-Attribute Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.) - &#x60;PreratedPerUnit&#x60; (available only if you have the Pre-rated Per Unit Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.) - &#x60;PreratedPricing&#x60; (available only if you have the Pre-rated Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.) - &#x60;HighWatermarkVolumePricing&#x60; (available only if you have the High Water Mark Volume Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.) - &#x60;HighWatermarkTieredPricing&#x60; (available only if you have the High Water Mark Tiered Pricing charge model enabled. The charge model is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.)  The value of the &#x60;pricing&#x60; field contains details about these charge models and the value of &#x60;pricingSummary&#x60; field contains their associated pricing summary values.  | [optional] 
**name** | **str** | Name of the product rate-plan charge. (Not required to be unique.)  | [optional] 
**number_of_periods** | **int** | Value specifies the number of periods used in the smoothing model calculations Used when overage smoothing model is &#x60;RollingWindow&#x60; or &#x60;Rollover&#x60;.  | [optional] 
**overage_calculation_option** | **str** | Value specifies when to calculate overage charges.  Values: - EndOfSmoothingPeriod - PerBillingPeriod  | [optional] 
**overage_unused_units_credit_option** | **str** | Determines whether to credit the customer with unused units of usage.  Values: - NoCredit - CreditBySpecificRate  | [optional] 
**prepay_periods** | **int** | The number of periods to which prepayment is set.   **Note:** This field is only available if you already have the prepayment feature enabled. The prepayment feature is deprecated and available only for backward compatibility. Zuora does not support enabling this feature anymore.  | [optional] 
**price_change_option** | **str** | Applies an automatic price change when a termed subscription is renewed and the following applies:  1. AutomatedPriceChange setting is on 2. Charge type is not one-time 3. Charge model is not discount fixed amount  Values: - NoChange (default) - SpecificPercentageValue - UseLatestProductCatalogPricing  | [optional] 
**price_increase_percentage** | **str** | Specifies the percentage to increase or decrease the price of a termed subscription&#39;s renewal. Use this field if you set the &#x60;PriceChangeOption&#x60; value to &#x60;SpecificPercentageValue&#x60;.  1. AutomatedPriceChange setting is on 2. Charge type is not one-time 3. Charge model is not discount fixed amount  Values: a decimal between -100 and 100  | [optional] 
**pricing** | [**list[GETProductRatePlanChargePricingType]**](GETProductRatePlanChargePricingType.md) | One or more price charge models with attributes that further describe the model.  Some attributes show as null values when not applicable.  | [optional] 
**pricing_summary** | **list[str]** | A concise description of the charge model and pricing that is suitable to show to your customers. When the rate plan charge model is &#x60;Tiered&#x60; and multi-currency is enabled, this field includes an array of string of each currency, and each string of currency includes tier price description separated by comma.  For the following charge models, the value of this field is an empty string: - Multi-Attribute Pricing - High Water Mark Tiered Pricing - High Water Mark Volume Pricing - Pre-Rated Per Unit Pricing - Pre-Rated Pricing  The charge models are available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information.  | [optional] 
**product_discount_apply_details** | [**list[GETProductDiscountApplyDetailsType]**](GETProductDiscountApplyDetailsType.md) | Container for the application details about a discount product rate plan charge.   Only discount product rate plan charges have values in this field.  | [optional] 
**rating_group** | **str** | Specifies a rating group based on which usage records are rated.  Possible values:  - &#x60;ByBillingPeriod&#x60; (default): The rating is based on all the usages in a billing period. - &#x60;ByUsageStartDate&#x60;: The rating is based on all the usages on the same usage start date.  - &#x60;ByUsageRecord&#x60;: The rating is based on each usage record. - &#x60;ByUsageUpload&#x60;: The rating is based on all the  usages in a uploaded usage file (&#x60;.xls&#x60; or &#x60;.csv&#x60;). - &#x60;ByGroupId&#x60;: The rating is based on all the usages in a custom group.  **Note:**  - The &#x60;ByBillingPeriod&#x60; value can be applied for all charge models.  - The &#x60;ByUsageStartDate&#x60;, &#x60;ByUsageRecord&#x60;, and &#x60;ByUsageUpload&#x60; values can only be applied for per unit, volume pricing, and tiered pricing charge models.  - The &#x60;ByGroupId&#x60; value is only available if you have the Active Rating feature enabled. - Use this field only for Usage charges. One-Time Charges and Recurring Charges return &#x60;NULL&#x60;.  | [optional] 
**rev_rec_code** | **str** | Associates this product rate plan charge with a specific revenue recognition code. The value is a valid revenue recognition code.  | [optional] 
**rev_rec_trigger_condition** | **str** | Specifies when revenue recognition begins.  | [optional] 
**revenue_recognition_rule_name** | **str** | The name of the revenue recognition rule governing the revenue schedule.  | [optional] 
**smoothing_model** | **str** | Specifies the smoothing model for an overage smoothing charge model or an tiered with overage model, which is an advanced type of a usage model that avoids spikes in usage charges. If a customer&#39;s usage spikes in a single period, then an overage smoothing model eases overage charges by considering usage and multiple periods.  One of the following values shows which smoothing model will be applied to the charge when &#x60;Overage&#x60; or &#x60;Tiered with Overage&#x60; is used:  - &#x60;RollingWindow&#x60; considers a number of periods to smooth usage. The rolling window starts and increments forward based on billing frequency. When allowed usage is met, then period resets and a new window begins. - &#x60;Rollover&#x60; considers a fixed number of periods before calculating usage. The net balance at the end of a period is unused usage, which is carried over to the next period&#39;s balance.  | [optional] 
**specific_billing_period** | **int** | When the billing period is set to &#x60;Specific&#x60; Months then this positive integer reflects the number of months for billing period charges.  | [optional] 
**tax_code** | **str** | Specifies the tax code for taxation rules; used by Zuora Tax.  | [optional] 
**tax_mode** | **str** | Specifies how to define taxation for the charge; used by Zuora Tax. Possible values are: &#x60;TaxExclusive&#x60;, &#x60;TaxInclusive&#x60;.  | [optional] 
**taxable** | **bool** | Specifies whether the charge is taxable; used by Zuora Tax. Possible values are:&#x60;true&#x60;, &#x60;false&#x60;.  | [optional] 
**trigger_event** | **str** | Specifies when to start billing the customer for the charge.  Values: one of the following: - &#x60;ContractEffective&#x60; is the date when the subscription&#39;s contract goes into effect and the charge is ready to be billed. - &#x60;ServiceActivation&#x60; is the date when the services or products for a subscription have been activated and the customers have access. - &#x60;CustomerAcceptance&#x60; is when the customer accepts the services or products for a subscription.  - &#x60;SpecificDate&#x60; is the date specified.  | [optional] 
**type** | **str** | The type of charge. Possible values are: &#x60;OneTime&#x60;, &#x60;Recurring&#x60;, &#x60;Usage&#x60;.  | [optional] 
**uom** | **str** | Describes the Units of Measure (uom) configured in **Settings &gt; Billing** for the productRatePlanCharges.  Values: &#x60;Each&#x60;, &#x60;License&#x60;, &#x60;Seat&#x60;, or &#x60;null&#x60;  | [optional] 
**up_to_periods** | **int** | Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends. If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.  | [optional] 
**up_to_periods_type** | **str** | The period type used to define when the charge ends.  Values: - Billing_Periods - Days - Weeks - Months - Years     | [optional] 
**usage_record_rating_option** | **str** | Determines how Zuora processes usage records for per-unit usage charges.   | [optional] 
**use_discount_specific_accounting_code** | **bool** | Determines whether to define a new accounting code for the new discount charge. Values: &#x60;true&#x60;, &#x60;false&#x60;  | [optional] 
**use_tenant_default_for_price_change** | **bool** | Shows the tenant-level percentage uplift value for an automatic price change to a termed subscription&#39;s renewal. You set the tenant uplift value in the web-based UI: **Settings &gt; Billing &gt; Define Default Subscription Settings**.  Values: &#x60;true&#x60;, &#x60;false&#x60;  | [optional] 
**class__ns** | **str** | Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**deferred_rev_account__ns** | **str** | Deferrred revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**department__ns** | **str** | Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**include_children__ns** | **str** | Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the product rate plan charge&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**item_type__ns** | **str** | Type of item that is created in NetSuite for the product rate plan charge. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**location__ns** | **str** | Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**recognized_rev_account__ns** | **str** | Recognized revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**rev_rec_end__ns** | **str** | End date condition of the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**rev_rec_start__ns** | **str** | Start date condition of the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**rev_rec_template_type__ns** | **str** | Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**subsidiary__ns** | **str** | Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the product rate plan charge was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

