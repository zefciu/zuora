# DetailedWorkflow

A workflow. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_type** | **str** | The call type of the active workflow version.  | [optional] 
**callout_trigger** | **bool** | Indicates whether the callout trigger is enabled for the retrieved workflow.  | [optional] 
**created_at** | **str** | The date and time when the workflow is created, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format.  | [optional] 
**description** | **str** | The description of the workflow.  | [optional] 
**finished_at** | **str** | The date and time when the instance of the workflow version finished at.  | [optional] 
**id** | **int** | The unique ID of the workflow.  | [optional] 
**interval** | **str** | The schedule of the workflow, in a CRON expression. Returns null if the schedued trigger is disabled.  | [optional] 
**name** | **str** | The name of the workflow.  | [optional] 
**ondemand_trigger** | **bool** | Indicates whether the ondemand trigger is enabled for the workflow.  | [optional] 
**original_workflow_id** | **int** | The unique ID of the original workflow version.  | [optional] 
**priority** | **str** | The priority of the active workflow version.   | [optional] 
**scheduled_trigger** | **bool** | Indicates whether the scheduled trigger is enabled for the workflow.  | [optional] 
**started_at** | **str** | The date and time when the instance of the workflow version started at.  | [optional] 
**status** | **int** | The status of the active workflow version.  | [optional] 
**sync_trigger** | **bool** | Indicates whether the workflow version is enabled for the sync mode.  | [optional] 
**timezone** | **str** | The timezone that is configured for the scheduler of the workflow. Returns null if the scheduled trigger is disabled.  | [optional] 
**type** | **str** | The type of the workflow. Currently the only valid value is &#39;Workflow::Setup&#39;.  | [optional] 
**updated_at** | **str** | The date and time when the workflow is updated the last time, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format.  | [optional] 
**version** | **str** | The version number of the active workflow version.              | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


