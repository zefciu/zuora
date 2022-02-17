# openapi_client.CustomObjectRecordsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_object_record_by_id**](CustomObjectRecordsApi.md#delete_custom_object_record_by_id) | **DELETE** /objects/records/default/{object}/{id} | Delete a custom object record
[**g_et_all_records_for_custom_object_type**](CustomObjectRecordsApi.md#g_et_all_records_for_custom_object_type) | **GET** /objects/records/default/{object} | List records for a custom object
[**g_et_custom_object_record_by_id**](CustomObjectRecordsApi.md#g_et_custom_object_record_by_id) | **GET** /objects/records/default/{object}/{id} | Retrieve a custom object record
[**p_ost_custom_object_records**](CustomObjectRecordsApi.md#p_ost_custom_object_records) | **POST** /objects/records/default/{object} | Create custom object records
[**p_ost_custom_object_records_batch_update_or_delete**](CustomObjectRecordsApi.md#p_ost_custom_object_records_batch_update_or_delete) | **POST** /objects/batch/default/{object} | Update or delete custom object records
[**p_ut_custom_object_record**](CustomObjectRecordsApi.md#p_ut_custom_object_record) | **PUT** /objects/records/default/{object}/{id} | Update a custom object record
[**patch_partial_update_custom_object_record**](CustomObjectRecordsApi.md#patch_partial_update_custom_object_record) | **PATCH** /objects/records/default/{object}/{id} | Partially update a custom object record


# **delete_custom_object_record_by_id**
> str delete_custom_object_record_by_id(authorization, object, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Delete a custom object record

Deletes a custom object record of the given type and ID.  Note that 200 response will be returned under either of the following conditions: * The record is identified and successfully deleted * The record could not be found  Note that the record is deleted immediately and, therefore, will not be retained upon successful deletion. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
id = 'id_example' # str | Id identifier in uuid form
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)

    try:
        # Delete a custom object record
        api_response = api_instance.delete_custom_object_record_by_id(authorization, object, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->delete_custom_object_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **id** | [**str**](.md)| Id identifier in uuid form | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_all_records_for_custom_object_type**
> QueryCustomObjectRecordsResponse g_et_all_records_for_custom_object_type(authorization, object, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version, q=q, ids=ids, page_size=page_size, cursor=cursor)

List records for a custom object

Lists all object records of the given type. You can also use the `q` query parameter to filter the output records.  ## Limitations   This call has the following limitations: * When a record is created, there will be a delay before it is available for search. For example, if you create 5 records and perform a query that these 5 records satisfy the query conditions, there will be a delay between when the 5 records are created, and when all the 5 records can be returned in the query result. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)
q = 'q_example' # str | The query string to filter the records of a custom object. See the [Query syntax of custom object records](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Data_Model/Custom_object_records/Query_syntax_of_custom_object_records) for more information.  Note that the `q` parameter only applies to filterable fields.  (optional)
ids = 'ids_example' # str | UUIDs of the records to be queried. For example:  `GET /objects/records/default/passenger?ids=258d65b2-7bc6-4142-88bc-5184931af493&ids=82ecc9f7-b192-4f88-a4a3-4b2af6c750a1`  (optional)
page_size = 56 # int | Page size. The value must be between 1 and 1000. (optional)
cursor = 'cursor_example' # str | The `cursor` points to the last record of the previous result set. The cursor record is not included in the query result. The call returns the first page if `cursor` is not provided and `pageSize` is valid. (optional)

    try:
        # List records for a custom object
        api_response = api_instance.g_et_all_records_for_custom_object_type(authorization, object, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version, q=q, ids=ids, page_size=page_size, cursor=cursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->g_et_all_records_for_custom_object_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 
 **q** | **str**| The query string to filter the records of a custom object. See the [Query syntax of custom object records](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Data_Model/Custom_object_records/Query_syntax_of_custom_object_records) for more information.  Note that the &#x60;q&#x60; parameter only applies to filterable fields.  | [optional] 
 **ids** | **str**| UUIDs of the records to be queried. For example:  &#x60;GET /objects/records/default/passenger?ids&#x3D;258d65b2-7bc6-4142-88bc-5184931af493&amp;ids&#x3D;82ecc9f7-b192-4f88-a4a3-4b2af6c750a1&#x60;  | [optional] 
 **page_size** | **int**| Page size. The value must be between 1 and 1000. | [optional] 
 **cursor** | **str**| The &#x60;cursor&#x60; points to the last record of the previous result set. The cursor record is not included in the query result. The call returns the first page if &#x60;cursor&#x60; is not provided and &#x60;pageSize&#x60; is valid. | [optional] 

### Return type

[**QueryCustomObjectRecordsResponse**](QueryCustomObjectRecordsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_custom_object_record_by_id**
> CustomObjectRecordWithAllFields g_et_custom_object_record_by_id(authorization, object, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Retrieve a custom object record

Retrieves a record of a given type by ID. 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
id = 'id_example' # str | Id identifier in uuid form
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)

    try:
        # Retrieve a custom object record
        api_response = api_instance.g_et_custom_object_record_by_id(authorization, object, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->g_et_custom_object_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **id** | [**str**](.md)| Id identifier in uuid form | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 

### Return type

[**CustomObjectRecordWithAllFields**](CustomObjectRecordWithAllFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**404** | Not exist |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_custom_object_records**
> PostCustomObjectRecordsResponse p_ost_custom_object_records(authorization, object, custom_objects_records, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Create custom object records

Creates custom object records with the given type.   Upon creating records of a custom object type, the 200 response contains a list of records that have been successfully processed and stored.   ## Limitations   This call has the following limitations: * The maximum number of records that you can create by one call is 1,000. * The storage of empty strings in records is not supported. * Null values must be formatted as the following example:    ```   {     \"records\": [       {         \"fieldName__c\": null       }     ]   }   ``` 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
custom_objects_records = openapi_client.PostCustomObjectRecordsRequest() # PostCustomObjectRecordsRequest | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)

    try:
        # Create custom object records
        api_response = api_instance.p_ost_custom_object_records(authorization, object, custom_objects_records, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->p_ost_custom_object_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **custom_objects_records** | [**PostCustomObjectRecordsRequest**](PostCustomObjectRecordsRequest.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 

### Return type

[**PostCustomObjectRecordsResponse**](PostCustomObjectRecordsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  The 200 response indicates that the records have been partially or completely created.  * If the &#x60;allowPartialSuccess&#x60; flag is set to &#x60;false&#x60;, the 200 response indicates that all object records have been successfully created. * If the &#x60;allowPartialSuccess&#x60; flag is set to &#x60;true&#x60;, the 200 response indicates that some records might not be succesffully created and the error information might be contained in the response body.  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**400** | Failed schema validation |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**401** | Unauthorized |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**500** | Internal error. Retry the returned records. |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_custom_object_records_batch_update_or_delete**
> CustomObjectRecordsBatchUpdatePartialSuccessResponse p_ost_custom_object_records_batch_update_or_delete(authorization, object, custom_object_record_batch_request, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Update or delete custom object records

Makes a batch update or delete of custom object records. ## Limitations   This call has the following limitations: * The maximum number of records that you can update by one call is 1,000. * The maximum number of records that you can delete by one call is 1,000. * The storage of empty strings in records is not supported. * Null values must be formatted as the following example:    ```   {       \"action\": {           \"type\": \"update\",           \"records\": {               \"64edb2a5-2796-4e95-9559-846f8636a01b\": {                   \"fieldName__c\": null             }           }       }   }   ``` 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
custom_object_record_batch_request = openapi_client.CustomObjectRecordBatchRequest() # CustomObjectRecordBatchRequest | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)

    try:
        # Update or delete custom object records
        api_response = api_instance.p_ost_custom_object_records_batch_update_or_delete(authorization, object, custom_object_record_batch_request, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->p_ost_custom_object_records_batch_update_or_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **custom_object_record_batch_request** | [**CustomObjectRecordBatchRequest**](CustomObjectRecordBatchRequest.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 

### Return type

[**CustomObjectRecordsBatchUpdatePartialSuccessResponse**](CustomObjectRecordsBatchUpdatePartialSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  For the bacth &#x60;delete&#x60; action, it indicates the batch records have been successfully deleted.  For the batch &#x60;update&#x60; action, it indicates that the batch records have been partially or completely updated.  * If the &#x60;allowPartialSuccess&#x60; flag is set to &#x60;false&#x60;, the 200 response indicates that all object records have been successfully updated. * If the &#x60;allowPartialSuccess&#x60; flag is set to &#x60;true&#x60;, the 200 response indicates that some records might not be succesffully updated and the error information might be contained in the response body.  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**400** | Failed schema validation  For the batch &#x60;update&#x60; action, the 400 response only returns when the &#x60;allowPartialSuccess&#x60; flag is set to &#x60;false&#x60; and the batch records have failed schema validation.  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**401** | Unauthorized |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**500** | Internal error. Retry the returned records. |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_custom_object_record**
> CustomObjectRecordWithAllFields p_ut_custom_object_record(authorization, object, id, object_record_request, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, if_match=if_match, zuora_version=zuora_version)

Update a custom object record

Updates a record of the given type and ID.  ## Limitations   * The storage of empty strings in records is not supported. * Null values must be formatted as the following example:    ```   {     \"records\": [       {         \"fieldName__c\": null       }     ]   }   ``` 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
id = 'id_example' # str | Id identifier in uuid form
object_record_request = None # dict(str, object) | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
if_match = 'if_match_example' # str | The expected ETag of the resource. You can use this header to perform a conditional request. Zuora responds with 412 Precondition Failed if the ETag of the resource does not match the value of this header.   (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)

    try:
        # Update a custom object record
        api_response = api_instance.p_ut_custom_object_record(authorization, object, id, object_record_request, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, if_match=if_match, zuora_version=zuora_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->p_ut_custom_object_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **id** | [**str**](.md)| Id identifier in uuid form | 
 **object_record_request** | [**dict(str, object)**](object.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **if_match** | **str**| The expected ETag of the resource. You can use this header to perform a conditional request. Zuora responds with 412 Precondition Failed if the ETag of the resource does not match the value of this header.   | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 

### Return type

[**CustomObjectRecordWithAllFields**](CustomObjectRecordWithAllFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**404** | Object record does not exist |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_partial_update_custom_object_record**
> CustomObjectRecordWithAllFields patch_partial_update_custom_object_record(authorization, object, id, object_record_patch_request, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Partially update a custom object record

Updates one or many fields of a custom object record. Patch update uses JSON Merge Patch as specified in [RFC 7386](https://tools.ietf.org/html/rfc7386).  ## Limitations   * The storage of empty strings in records is not supported. * Null values must be formatted as the following example:    ```   {     \"records\": [       {         \"fieldName__c\": null       }     ]   }   ``` 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest.zuora.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rest.zuora.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomObjectRecordsApi(api_client)
    authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
object = 'object_example' # str | Specifies the custom object's API name as object. It is case-sensitive.
id = 'id_example' # str | Id identifier in uuid form
object_record_patch_request = None # dict(str, object) | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = '2013-10-20' # date | API version that determines the response schema. The default version is used if this parameter is not included. Specify `Zuora-Version` in the request header if you expect a specific response schema. (optional)

    try:
        # Partially update a custom object record
        api_response = api_instance.patch_partial_update_custom_object_record(authorization, object, id, object_record_patch_request, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomObjectRecordsApi->patch_partial_update_custom_object_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **object** | **str**| Specifies the custom object&#39;s API name as object. It is case-sensitive. | 
 **id** | [**str**](.md)| Id identifier in uuid form | 
 **object_record_patch_request** | [**dict(str, object)**](object.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **date**| API version that determines the response schema. The default version is used if this parameter is not included. Specify &#x60;Zuora-Version&#x60; in the request header if you expect a specific response schema. | [optional] 

### Return type

[**CustomObjectRecordWithAllFields**](CustomObjectRecordWithAllFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**404** | Object record does not exist |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

