# DataQueryJob

A data query job. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The query job creator&#39;s Id.  | [optional] 
**id** | **str** | Internal identifier of the query job.  | [optional] 
**query** | **str** | The query that was submitted.  | [optional] 
**remaining_retries** | **int** | The number of times that Zuora will retry the query if Zuora is unable to perform the query.  | [optional] 
**updated_on** | **datetime** | Date and time when the query job was last updated, in ISO 8601 format.  | [optional] 
**data_file** | **str** | The URL of the query results. Only applicable if the value of the &#x60;queryStatus&#x60; field is &#x60;completed&#x60;.  | [optional] 
**output_rows** | **int** | The number of rows the query results. Only applicable if the value of the &#x60;queryStatus&#x60; field is &#x60;completed&#x60;.  | [optional] 
**processing_time** | **int** | Processing time of the query job, in milliseconds. Only applicable if the value of the &#x60;queryStatus&#x60; field is &#x60;completed&#x60;.  | [optional] 
**query_status** | **str** | Status of the query job.  * &#x60;submitted&#x60; - query submitted to query service for processing * &#x60;accepted&#x60; - query accepted by the query service * &#x60;in_progress&#x60; - query executed by the query service * &#x60;completed&#x60; - query execution completed by the query service * &#x60;failed&#x60; - query unable to be processed by the query service * &#x60;cancelled&#x60; - query cancelled by the user  If the value of this field is &#x60;completed&#x60;, the &#x60;dataFile&#x60; field contains the location of the query results.  If the value of this field is &#x60;accepted&#x60; or &#x60;in_progress&#x60;, you can use [Cancel a data query job](#operation/DELETE_DataQueryJob) to prevent Zuora from performing the query. Zuora then sets the status of the query job to &#x60;cancelled&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


