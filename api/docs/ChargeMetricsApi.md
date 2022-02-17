# openapi_client.ChargeMetricsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_charge_metrics**](ChargeMetricsApi.md#g_et_charge_metrics) | **GET** /charge-metrics/data/charge-metrics | List charge metrics by time range
[**g_et_charge_metrics_discount_allocation_details**](ChargeMetricsApi.md#g_et_charge_metrics_discount_allocation_details) | **GET** /charge-metrics/data/charge-metrics-discount-allocation-detail | List discount allocation details by time range


# **g_et_charge_metrics**
> ChargeMetricsResponse g_et_charge_metrics(from_timestamp, to_timestamp, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, accept=accept)

List charge metrics by time range

Retrieves key charge metrics about rate plan charges that have changes in a specified time range.  The purpose of `fromTimestamp` and `toTimestamp` is to synchronize charge metrics data incrementally.  

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
    api_instance = openapi_client.ChargeMetricsApi(api_client)
    from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | The starting date and time of a time range when changes are made to charge metrics, in `yyyy-mm-ddThh:mm:ssZ` format. For example, `2020-08-18T09:01:11Z`. The timestamp maps to the `UpdatedOn` timestamp of the to-be-exported object. 
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | The end date and time of a time range when changes are made to charge metrics, in `yyyy-mm-ddThh:mm:ssZ` format. For example, `2020-08-20T09:01:11Z`. The timestamp maps to the `UpdatedOn` timestamp of the to-be-exported object. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
accept = 'accept_example' # str | Expressed as MIME types that the client is able to understand. Using content negotiation, the server then selects one of the proposals, uses it and informs the client of its choice with the `Content-Type` response header. The possible response MIME types are `application/json-seq` compatible with http://jsonlines.org/, and `text/csv` compatible with RFC 4180. `application/json-seq` is the default response MIME type. If the `Accept` header is not sepecified, or set */*, the response body is returned in application/json-seq MIME type.  (optional)

    try:
        # List charge metrics by time range
        api_response = api_instance.g_et_charge_metrics(from_timestamp, to_timestamp, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, accept=accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChargeMetricsApi->g_et_charge_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| The starting date and time of a time range when changes are made to charge metrics, in &#x60;yyyy-mm-ddThh:mm:ssZ&#x60; format. For example, &#x60;2020-08-18T09:01:11Z&#x60;. The timestamp maps to the &#x60;UpdatedOn&#x60; timestamp of the to-be-exported object.  | 
 **to_timestamp** | **datetime**| The end date and time of a time range when changes are made to charge metrics, in &#x60;yyyy-mm-ddThh:mm:ssZ&#x60; format. For example, &#x60;2020-08-20T09:01:11Z&#x60;. The timestamp maps to the &#x60;UpdatedOn&#x60; timestamp of the to-be-exported object.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **accept** | **str**| Expressed as MIME types that the client is able to understand. Using content negotiation, the server then selects one of the proposals, uses it and informs the client of its choice with the &#x60;Content-Type&#x60; response header. The possible response MIME types are &#x60;application/json-seq&#x60; compatible with http://jsonlines.org/, and &#x60;text/csv&#x60; compatible with RFC 4180. &#x60;application/json-seq&#x60; is the default response MIME type. If the &#x60;Accept&#x60; header is not sepecified, or set */*, the response body is returned in application/json-seq MIME type.  | [optional] 

### Return type

[**ChargeMetricsResponse**](ChargeMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json-seq, application/json, 

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**400** | Invalid Parameters |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**429** | Rate limited |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Retry-After - The interval of seconds that you have to wait before another retry.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**500** | Internal Error |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_charge_metrics_discount_allocation_details**
> ChargeMetricsDiscountAllocationDetailResponse g_et_charge_metrics_discount_allocation_details(from_timestamp, to_timestamp, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, accept=accept)

List discount allocation details by time range

Retrieves discount allocation details about rate plan charges that have changes in a specified time range.  The purpose of `fromTimestamp` and `toTimestamp` is to synchronize discount allocation details incrementally.  

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
    api_instance = openapi_client.ChargeMetricsApi(api_client)
    from_timestamp = '2013-10-20T19:20:30+01:00' # datetime | The starting date and time of a time range when changes are made to charge metrics, in `yyyy-mm-ddThh:mm:ssZ` format. For example, `2020-08-18T09:01:11Z`. The timestamp maps to the `UpdatedOn` timestamp of the to-be-exported object. 
to_timestamp = '2013-10-20T19:20:30+01:00' # datetime | The end date and time of a time range when changes are made to charge metrics, in `yyyy-mm-ddThh:mm:ssZ` format. For example, `2020-08-20T09:01:11Z`. The timestamp maps to the `UpdatedOn` timestamp of the to-be-exported object. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
accept = 'accept_example' # str | Expressed as MIME types that the client is able to understand. Using content negotiation, the server then selects one of the proposals, uses it and informs the client of its choice with the `Content-Type` response header. The possible response MIME types are `application/json-seq` compatible with http://jsonlines.org/, and `text/csv` compatible with RFC 4180. `application/json-seq` is the default response MIME type. If the `Accept` header is not sepecified, or set */*, the response body is returned in application/json-seq MIME type.  (optional)

    try:
        # List discount allocation details by time range
        api_response = api_instance.g_et_charge_metrics_discount_allocation_details(from_timestamp, to_timestamp, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, accept=accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChargeMetricsApi->g_et_charge_metrics_discount_allocation_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_timestamp** | **datetime**| The starting date and time of a time range when changes are made to charge metrics, in &#x60;yyyy-mm-ddThh:mm:ssZ&#x60; format. For example, &#x60;2020-08-18T09:01:11Z&#x60;. The timestamp maps to the &#x60;UpdatedOn&#x60; timestamp of the to-be-exported object.  | 
 **to_timestamp** | **datetime**| The end date and time of a time range when changes are made to charge metrics, in &#x60;yyyy-mm-ddThh:mm:ssZ&#x60; format. For example, &#x60;2020-08-20T09:01:11Z&#x60;. The timestamp maps to the &#x60;UpdatedOn&#x60; timestamp of the to-be-exported object.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **accept** | **str**| Expressed as MIME types that the client is able to understand. Using content negotiation, the server then selects one of the proposals, uses it and informs the client of its choice with the &#x60;Content-Type&#x60; response header. The possible response MIME types are &#x60;application/json-seq&#x60; compatible with http://jsonlines.org/, and &#x60;text/csv&#x60; compatible with RFC 4180. &#x60;application/json-seq&#x60; is the default response MIME type. If the &#x60;Accept&#x60; header is not sepecified, or set */*, the response body is returned in application/json-seq MIME type.  | [optional] 

### Return type

[**ChargeMetricsDiscountAllocationDetailResponse**](ChargeMetricsDiscountAllocationDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json, 

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**400** | Invalid Parameters |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**429** | Rate limited |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Retry-After - The interval of seconds that you have to wait before another retry.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**500** | Internal Error |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

