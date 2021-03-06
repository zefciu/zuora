# openapi_client.OAuthApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](OAuthApi.md#create_token) | **POST** /oauth/token | Create an OAuth token


# **create_token**
> TokenResponse create_token(client_id, client_secret, grant_type, zuora_track_id=zuora_track_id)

Create an OAuth token

Creates a bearer token that enables an OAuth client to authenticate with the Zuora REST API. The OAuth client must have been created using the Zuora UI. See [Authentication](https://www.zuora.com/developer/api-reference/#section/Authentication) for more information.  **Note:** When using this operation, do not set any authentication headers such as `Authorization`, `apiAccessKeyId`, or `apiSecretAccessKey`.  You should not use this operation to generate a large number of bearer tokens in a short period of time; each token should be used until it expires. If you receive a 429 Too Many Requests response when using this operation, reduce the frequency of requests. This endpoint is rate limited by IP address. The rate limit is 100 requests per minute. 

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
    api_instance = openapi_client.OAuthApi(api_client)
    client_id = 'client_id_example' # str | The Client ID of the OAuth client. 
client_secret = 'client_secret_example' # str | The Client Secret that was displayed when the OAuth client was created. 
grant_type = 'grant_type_example' # str | The OAuth grant type that will be used to generate the token. The value of this parameter must be `client_credentials`. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

    try:
        # Create an OAuth token
        api_response = api_instance.create_token(client_id, client_secret, grant_type, zuora_track_id=zuora_track_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OAuthApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The Client ID of the OAuth client.  | 
 **client_secret** | **str**| The Client Secret that was displayed when the OAuth client was created.  | 
 **grant_type** | **str**| The OAuth grant type that will be used to generate the token. The value of this parameter must be &#x60;client_credentials&#x60;.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Remaining-minute - The number of requests that you may make in the next minute. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * X-RateLimit-Limit-minute - The rate limit of this operation, in requests per minute. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |
**429** | Too Many Requests |  * X-RateLimit-Remaining-minute - The number of requests that you may make in the next minute. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Request-Id - The Zuora internal identifier of the API call. You cannot control the value of this header.  <br>  * X-RateLimit-Limit-minute - The rate limit of this operation, in requests per minute. See [rate limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits#Rate_limits) for more information.  <br>  * Zuora-Track-Id - A custom identifier for tracing the API call. If you specified a tracing identifier in the request headers, Zuora returns the same tracing identifier. Otherwise, Zuora does not set this header.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

