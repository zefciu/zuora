# openapi_client.PaymentGatewayTransactionLogsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_payment_gateway_transaction_log**](PaymentGatewayTransactionLogsApi.md#g_et_payment_gateway_transaction_log) | **GET** /v1/payment-gateway-transaction-log | Retrieve a payment gateway transaction log


# **g_et_payment_gateway_transaction_log**
> GETPaymentGatewayTransactionLogResponse g_et_payment_gateway_transaction_log(zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, payment_id=payment_id, refund_id=refund_id)

Retrieve a payment gateway transaction log

Retrieves transaction log information passed through your [custom payment gateway](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods). 

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
    api_instance = openapi_client.PaymentGatewayTransactionLogsApi(api_client)
    zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
payment_id = 'payment_id_example' # str | The ID of the payment wherein the gateway transaction log was recorded.  (optional)
refund_id = 'refund_id_example' # str | The ID of the refund wherein the gateway transaction log was recorded.  (optional)

    try:
        # Retrieve a payment gateway transaction log
        api_response = api_instance.g_et_payment_gateway_transaction_log(zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, payment_id=payment_id, refund_id=refund_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentGatewayTransactionLogsApi->g_et_payment_gateway_transaction_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **payment_id** | **str**| The ID of the payment wherein the gateway transaction log was recorded.  | [optional] 
 **refund_id** | **str**| The ID of the refund wherein the gateway transaction log was recorded.  | [optional] 

### Return type

[**GETPaymentGatewayTransactionLogResponse**](GETPaymentGatewayTransactionLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * RateLimit-Remaining - The number of requests remaining in the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Reset - The number of seconds until the quota resets for the time window closest to quota exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * RateLimit-Limit - The request limit quota for the time window closest to exhaustion. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

