# GetWorkflowResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_time** | **str** | The overall CPU time for the execution of the workflow.  | [optional] 
**created_at** | **str** | The date and time when the workflow is created, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format..  | [optional] 
**finished_at** | **str** | The date and time when the execution of the workflow completes, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format.  | [optional] 
**id** | **int** | The unique ID of the workflow.  | [optional] 
**messages** | [**object**](.md) | Messages from tasks.  | [optional] 
**name** | **str** | The unique run number of the workflow.  | [optional] 
**original_workflow_id** | **str** | The ID of the workflow setup.  | [optional] 
**run_time** | **float** | The execution time of the workflow including the waiting time, in seconds.  | [optional] 
**status** | **str** | The status of the workflow:   - Queued: The workflow is in queue for being processed.   - Processing: The workflow is in process.   - Stopping: The workflow is being stopped through Zuora UI.   - Stopped: The workflow is stopped through Zuora UI.   - Finished: The workflow is finished. When a workflow is finished, it might have tasks pending for retry or delay. Pending tasks do not block the onfinish branch of the workflow, but they block the oncomplete branch of the iterate.   | [optional] 
**tasks** | [**GetWorkflowResponseTasks**](GetWorkflowResponseTasks.md) |  | [optional] 
**type** | **str** | The type of the current workflow. Possible values:   - &#x60;Workflow::Setup&#x60;: The workflow is a setup and is used for creating workflow instances.   - &#x60;Workflow::Instance&#x60;: The workflow is an execution that has data.  | [optional] 
**updated_at** | **str** | The date and time when the workflow is updated the last time, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


