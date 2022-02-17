# RampIntervalChargeDeltaMetrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_number** | **str** | The number of the rate plan charge. | [optional] 
**delta_discount_tcb** | **float** | The discount delta amount for the TCB. | [optional] 
**delta_discount_tcv** | **float** | The discount delta amount for the TCV. | [optional] 
**delta_gross_tcb** | **float** | The TCB delta value before discount charges are applied. | [optional] 
**delta_gross_tcv** | **float** | The TCV delta value before discount charges are applied. | [optional] 
**delta_mrr** | [**list[RampIntervalChargeDeltaMetricsDeltaMrr]**](RampIntervalChargeDeltaMetricsDeltaMrr.md) | The MRR changing history of the current rate plan charge in the current ramp interval. | [optional] 
**delta_net_tcb** | **float** | The TCB delta value after discount charges are applied. | [optional] 
**delta_net_tcv** | **float** | The TCV delta value after discount charges are applied. | [optional] 
**delta_quantity** | [**list[RampIntervalChargeDeltaMetricsDeltaQuantity]**](RampIntervalChargeDeltaMetricsDeltaQuantity.md) | The charge quantity changing history of the current rate plan charge in the current ramp interval. | [optional] 
**product_rate_plan_charge_id** | **str** | The ID of the corresponding product rate plan charge. | [optional] 
**subscription_number** | **str** | The number of the subscription that the current rate plan charge belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


