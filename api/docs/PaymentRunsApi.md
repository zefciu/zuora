# openapi_client.PaymentRunsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_payment_run**](PaymentRunsApi.md#d_elete_payment_run) | **DELETE** /v1/payment-runs/{paymentRunId} | Delete a payment run
[**g_et_payment_run**](PaymentRunsApi.md#g_et_payment_run) | **GET** /v1/payment-runs/{paymentRunId} | Retrieve a payment run
[**g_et_payment_run_data**](PaymentRunsApi.md#g_et_payment_run_data) | **GET** /v1/payment-runs/{paymentRunId}/data | Retrieve payment run data
[**g_et_payment_run_summary**](PaymentRunsApi.md#g_et_payment_run_summary) | **GET** /v1/payment-runs/{paymentRunId}/summary | Retrieve a payment run summary
[**g_et_payment_runs**](PaymentRunsApi.md#g_et_payment_runs) | **GET** /v1/payment-runs | List payment runs
[**p_ost_payment_run**](PaymentRunsApi.md#p_ost_payment_run) | **POST** /v1/payment-runs | Create a payment run
[**p_ut_payment_run**](PaymentRunsApi.md#p_ut_payment_run) | **PUT** /v1/payment-runs/{paymentRunId} | Update a payment run


# **d_elete_payment_run**
> CommonResponseType d_elete_payment_run(payment_run_id, zuora_track_id=zuora_track_id)

Delete a payment run

Deletes a payment run. Only payment runs with the Canceled or Error status can be deleted. 

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

    try:
        # Delete a payment run
        api_response = api_instance.d_elete_payment_run(payment_run_id, zuora_track_id=zuora_track_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->d_elete_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | **str**| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_run**
> GETPaymentRunType g_et_payment_run(payment_run_id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Retrieve a payment run

Retrives the information about a specific payment run. 

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

    try:
        # Retrieve a payment run
        api_response = api_instance.g_et_payment_run(payment_run_id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->g_et_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | **str**| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentRunType**](GETPaymentRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_run_data**
> GETPaymentRunDataArrayResponse g_et_payment_run_data(payment_run_id, zuora_track_id=zuora_track_id)

Retrieve payment run data

Retrieves payment run data and the processing result with details, if the `data` field was specified in the Create payment run operation.     

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

    try:
        # Retrieve payment run data
        api_response = api_instance.g_et_payment_run_data(payment_run_id, zuora_track_id=zuora_track_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->g_et_payment_run_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | **str**| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GETPaymentRunDataArrayResponse**](GETPaymentRunDataArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_run_summary**
> GETPaymentRunSummaryResponse g_et_payment_run_summary(payment_run_id, zuora_track_id=zuora_track_id)

Retrieve a payment run summary

Retrives the summary of a payment run. 

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

    try:
        # Retrieve a payment run summary
        api_response = api_instance.g_et_payment_run_summary(payment_run_id, zuora_track_id=zuora_track_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->g_et_payment_run_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | **str**| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GETPaymentRunSummaryResponse**](GETPaymentRunSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_runs**
> GETPaymentRunCollectionType g_et_payment_runs(zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, created_by_id=created_by_id, created_date=created_date, status=status, target_date=target_date, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

List payment runs

Retrieves the information about all payment runs. You can define filterable fields to restrict the data returned in the response.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/payment-runs?status=Processed  - /v1/payment-runs?targetDate=2017-10-10&status=Pending  - /v1/payment-runs?status=Completed&sort=+updatedDate 

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.  (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.  (optional)
status = 'status_example' # str | This parameter filters the response based on the `status` field.  (optional)
target_date = '2013-10-20' # date | This parameter filters the response based on the `targetDate` field.  (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.  (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by payment run number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - targetDate   - status   - createdDate   - createdById   - updatedDate   - updatedById  Examples:  - /v1/payment-runs?sort=+createdDate  - /v1/payment-runs?status=Processing&sort=-createdById,+targetDate  (optional)

    try:
        # List payment runs
        api_response = api_instance.g_et_payment_runs(zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, created_by_id=created_by_id, created_date=created_date, status=status, target_date=target_date, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->g_et_payment_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.  | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.  | [optional] 
 **status** | **str**| This parameter filters the response based on the &#x60;status&#x60; field.  | [optional] 
 **target_date** | **date**| This parameter filters the response based on the &#x60;targetDate&#x60; field.  | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.  | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by payment run number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - targetDate   - status   - createdDate   - createdById   - updatedDate   - updatedById  Examples:  - /v1/payment-runs?sort&#x3D;+createdDate  - /v1/payment-runs?status&#x3D;Processing&amp;sort&#x3D;-createdById,+targetDate  | [optional] 

### Return type

[**GETPaymentRunCollectionType**](GETPaymentRunCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_run**
> GETPaymentRunType p_ost_payment_run(body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Create a payment run

Creates a payment run. You can create a payment run to be executed immediately after it is created, or a scheduled payment run to be executed in future.  To filter the payments to be collected for a payment run, you can use either of the following methods but not both:    - Use the `accountId`, `batch`, `billCycleDay`, `currency`, `paymentGatewayId`, and `billingRunId` fields to define the billing documents to be collected.   - Use the `data` field to specify the records of accounts and billing documents to be collected, in a more flexible manner. See [Create custom payment runs through Zuora REST API](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/K_Payment_Operations/CA_Payment_Runs/Create_custom_payment_runs_through_Zuora_REST_API) for more information.  If no filter criteria are specified in the request body, the payment run collects payments for all accounts. 

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    body = openapi_client.POSTPaymentRunRequest() # POSTPaymentRunRequest | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

    try:
        # Create a payment run
        api_response = api_instance.p_ost_payment_run(body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->p_ost_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTPaymentRunRequest**](POSTPaymentRunRequest.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentRunType**](GETPaymentRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_payment_run**
> GETPaymentRunType p_ut_payment_run(payment_run_id, body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Update a payment run

Updates the information about an unexecuted payment run. Only pending payment runs can be updated.  If none of the **accountId**, **batch**, **billCycleDay**, **currency**, **paymentGatewayId**, and **billingRunId** fields is specified in the request body, the corresponding payment run collects payments for all accounts. 

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
    api_instance = openapi_client.PaymentRunsApi(api_client)
    payment_run_id = 'payment_run_id_example' # str | The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566. 
body = openapi_client.PUTPaymentRunRequest() # PUTPaymentRunRequest | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

    try:
        # Update a payment run
        api_response = api_instance.p_ut_payment_run(payment_run_id, body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentRunsApi->p_ut_payment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_run_id** | **str**| The unique ID of a payment run. For example, 402890245f097f39015f0f074a2e0566.  | 
 **body** | [**PUTPaymentRunRequest**](PUTPaymentRunRequest.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentRunType**](GETPaymentRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

