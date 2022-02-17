# Task

A task. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | The type of the task.  | [optional] 
**call_type** | **str** | The type of API used.  | [optional] 
**concurrent_limit** | **int** | the number of concurrent tasks that are allowed to run simultaneously | [optional] 
**data** | [**object**](.md) | The data payload for the task.  | [optional] 
**end_time** | **str** | If **Instance** is **true**, the end time of the task instance.  | [optional] 
**error** | **str** | If **Instance** is **true** and **status** is **Error**, the error reason of the task instance failure.  | [optional] 
**error_class** | **str** | If **Instance** is **true** and **status** is **Error**, the error class of the task instance failure.  | [optional] 
**error_details** | **str** | If **Instance** is **true** and **status** is **Error**, the error details of the task instance failure.  | [optional] 
**id** | **int** | The unique ID of the task.  | [optional] 
**instance** | **bool** | Indicates whether this task belongs to an instance of a workflow.  | [optional] 
**name** | **str** | The name of the task.  | [optional] 
**object** | **str** | The selected object for the task.  | [optional] 
**object_id** | **str** | The id of the selected object of the task.  | [optional] 
**original_task_id** | **int** | If **Instance** is **true**, the ID of the original task in the original workflow.  | [optional] 
**original_workflow_id** | **int** | If **Instance** is **true**, the ID of the original workflow.  | [optional] 
**parameters** | [**object**](.md) | The configuration of the task.  | [optional] 
**start_time** | **str** | If **Instance** is **true**, the start time of the task instance.  | [optional] 
**status** | **str** | If **Instance** is **true**, the status of the task instance.  | [optional] 
**tags** | **list[str]** | The array of filter tags.  | [optional] 
**task_id** | **int** | the id of this task&#39;s parent task. Will be null if this is the first task of the workflow | [optional] 
**workflow_id** | **int** | The ID of the workflow that the task belongs to.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


