# openapi_client.BillingDocumentsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_billing_document_files_deletion_job**](BillingDocumentsApi.md#g_et_billing_document_files_deletion_job) | **GET** /v1/accounts/billing-documents/files/deletion-jobs/{jobId} | Retrieve a job of hard deleting billing document files
[**g_et_billing_documents**](BillingDocumentsApi.md#g_et_billing_documents) | **GET** /v1/billing-documents | List billing documents for an account
[**p_ost_billing_document_files_deletion_job**](BillingDocumentsApi.md#p_ost_billing_document_files_deletion_job) | **POST** /v1/accounts/billing-documents/files/deletion-jobs | Create a job to hard delete billing document files
[**p_ost_generate_billing_documents**](BillingDocumentsApi.md#p_ost_generate_billing_documents) | **POST** /v1/accounts/{id}/billing-documents/generate | Generate billing documents by account ID


# **g_et_billing_document_files_deletion_job**
> GETBillingDocumentFilesDeletionJobResponse g_et_billing_document_files_deletion_job(job_id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Retrieve a job of hard deleting billing document files

Retrieves information about an asynchronous job of permanently deleting all billing document PDF files for specific accounts.  **Note**: This operation can be used only if you have the Billing user permission \"Hard Delete Billing Document Files\" enabled.  

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
    api_instance = openapi_client.BillingDocumentsApi(api_client)
    job_id = 'job_id_example' # str | The unique ID of a billing document file deletion job. For example, 2c92c8f83dc4f752013dc72c24ee016c.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

    try:
        # Retrieve a job of hard deleting billing document files
        api_response = api_instance.g_et_billing_document_files_deletion_job(job_id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingDocumentsApi->g_et_billing_document_files_deletion_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The unique ID of a billing document file deletion job. For example, 2c92c8f83dc4f752013dc72c24ee016c. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETBillingDocumentFilesDeletionJobResponse**](GETBillingDocumentFilesDeletionJobResponse.md)

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

# **g_et_billing_documents**
> BillingDocumentQueryResponseElementType g_et_billing_documents(account_id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, document_date=document_date, status=status, sort=sort)

List billing documents for an account

Retrieves the information about all billing documents associated with a specified account. The billing documents contain invoices, credit memos, and debit memos.   To retrieve information about credit memos and debit memos, you must have the Invoice Settlement feature enabled.   You can use query parameters to restrict the data returned in the response.  Examples: - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1&sort=+documentDate - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1&status=Posted 

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
    api_instance = openapi_client.BillingDocumentsApi(api_client)
    account_id = 'account_id_example' # str | The ID of the customer account that the billing documents are associated with.  
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)
document_date = '2013-10-20' # date | The date of the billing document. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  (optional)
status = 'status_example' # str | The status of the billing document.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  If you do not specify any sortable field, the response data is sorted by the `documentDate` field in descending order.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.      - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - documentDate   - documentType    Examples: - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1   &sort=+documentDate,-documentType - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1   &status=Posted&sort=+documentDate&page=2&pageSize=15  (optional)

    try:
        # List billing documents for an account
        api_response = api_instance.g_et_billing_documents(account_id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, document_date=document_date, status=status, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingDocumentsApi->g_et_billing_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| The ID of the customer account that the billing documents are associated with.   | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]
 **document_date** | **date**| The date of the billing document. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  | [optional] 
 **status** | **str**| The status of the billing document.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  If you do not specify any sortable field, the response data is sorted by the &#x60;documentDate&#x60; field in descending order.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.      - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - documentDate   - documentType    Examples: - /billing-documents?accountId&#x3D;4028905f5e4feb38015e50af9aa002d1   &amp;sort&#x3D;+documentDate,-documentType - /billing-documents?accountId&#x3D;4028905f5e4feb38015e50af9aa002d1   &amp;status&#x3D;Posted&amp;sort&#x3D;+documentDate&amp;page&#x3D;2&amp;pageSize&#x3D;15  | [optional] 

### Return type

[**BillingDocumentQueryResponseElementType**](BillingDocumentQueryResponseElementType.md)

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

# **p_ost_billing_document_files_deletion_job**
> POSTBillingDocumentFilesDeletionJobResponse p_ost_billing_document_files_deletion_job(body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Create a job to hard delete billing document files

Creates an asynchronous job to permanently delete all billing document PDF files for specific accounts.   After the deletion job is completed, all billing document PDF files are permanently deleted. To retrieve the status of a deletion job, call [Retrieve a job of hard deleting billing document files](https://www.zuora.com/developer/api-reference/#operation/GET_BillingDocumentFilesDeletionJob).  **Note**: This operation can be used only if you have the Billing user permission \"Hard Delete Billing Document Files\" enabled.  

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
    api_instance = openapi_client.BillingDocumentsApi(api_client)
    body = openapi_client.POSTBillingDocumentFilesDeletionJobRequest() # POSTBillingDocumentFilesDeletionJobRequest | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

    try:
        # Create a job to hard delete billing document files
        api_response = api_instance.p_ost_billing_document_files_deletion_job(body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingDocumentsApi->p_ost_billing_document_files_deletion_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTBillingDocumentFilesDeletionJobRequest**](POSTBillingDocumentFilesDeletionJobRequest.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTBillingDocumentFilesDeletionJobResponse**](POSTBillingDocumentFilesDeletionJobResponse.md)

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

# **p_ost_generate_billing_documents**
> GenerateBillingDocumentResponseType p_ost_generate_billing_documents(id, body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Generate billing documents by account ID

Generates draft or posted billing documents for a specified account. You can also generate billing documents for specified subscriptions of a specified account. The billing documents contain invoices and credit memos. To generate credit memos, you must have the Invoice Settlement feature enabled.  **Note**: You cannot generate billing documents for cancelled or suspended subscriptions. 

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
    api_instance = openapi_client.BillingDocumentsApi(api_client)
    id = 'id_example' # str | The ID of the customer account that billing documents are generated for. For example, 8a8082e65b27f6c3015ba3e326b26419. 
body = openapi_client.PostGenerateBillingDocumentType() # PostGenerateBillingDocumentType | 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

    try:
        # Generate billing documents by account ID
        api_response = api_instance.p_ost_generate_billing_documents(id, body, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingDocumentsApi->p_ost_generate_billing_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the customer account that billing documents are generated for. For example, 8a8082e65b27f6c3015ba3e326b26419.  | 
 **body** | [**PostGenerateBillingDocumentType**](PostGenerateBillingDocumentType.md)|  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GenerateBillingDocumentResponseType**](GenerateBillingDocumentResponseType.md)

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

