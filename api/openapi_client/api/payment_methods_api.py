# coding: utf-8

"""
    API Reference: Billing

      # Introduction  Welcome to the reference for the Zuora Billing REST API!  To learn about the common use cases of Zuora Billing REST APIs, check out the [API Guides](https://www.zuora.com/developer/api-guides/).  In addition to Zuora API Reference; Billing, we also provide API references for other Zuora products:    * [API Reference: Collections](https://www.zuora.com/developer/collect-api/)   * [API Reference: Revenue](https://www.zuora.com/developer/revpro-api/)      The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Billing Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Cloud 1 Production | https://rest.na.zuora.com  | |US Cloud 1 API Sandbox |  https://rest.sandbox.na.zuora.com | |US Cloud 2 Production | https://rest.zuora.com | |US Cloud 2 API Sandbox | https://rest.apisandbox.zuora.com| |US Central Sandbox | https://rest.test.zuora.com |   |US Performance Test | https://rest.pt1.zuora.com | |US Production Copy | Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints. See [REST endpoint base URL of Production Copy (Service) Environment for existing and new customers](https://community.zuora.com/t5/API/REST-endpoint-base-URL-of-Production-Copy-Service-Environment/td-p/29611) for more information. | |EU Production | https://rest.eu.zuora.com | |EU API Sandbox | https://rest.sandbox.eu.zuora.com | |EU Central Sandbox | https://rest.test.eu.zuora.com |  The Production endpoint provides access to your live user data. Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision a Sandbox tenant for you, contact your Zuora representative for assistance.   If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/communities/community-home/digestviewer/viewthread?GroupId=103&MessageKey=6a672528-d068-47fa-a111-a3f118e016f3&CommunityKey=e2a932b4-50c4-4019-a3e8-362e38714df3&tab=digestviewer&ReturnUrl=%2fcommunities%2fcommunity-home%2fdigestviewer%3fMessageKey%3db8cc94ea-9092-4974-9964-ff19dc5c6d67%26CommunityKey%3de2a932b4-50c4-4019-a3e8-362e38714df3\" target=\"_blank\">Changelog</a> of the API Reference: Billing in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. You should reuse the bearer token until it is expired. When the token is expired, call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new one.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.   ## Making asynchronous requests  Most Zuora REST API endpoints documented in this API Reference process requests synchronously. In high-throughput scenarios, your requests to these endpoints are usually rate limited.   One strategy for avoiding rate limits is to make asynchronous requests, and Zuora provides this option to you.  Making asynchronous requests allows you to scale your applications more efficiently by leveraging Zuora's infrastructure to enqueue and execute requests for you without blocking. These requests also use built-in retry semantics, which makes them much less likely to fail for non-deterministic reasons, even in extreme high-throughput scenarios.  Meanwhile, when you send a request to one of these endpoints, you can receive a response in less than 150 milliseconds and these calls are unlikely to trigger rate limit errors.   You can make asynchronous requests to the POST, PUT, or DELETE operations, except [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions), for all resources documented in this API Reference.  Take the following steps to take advantage of the asynchronous API:    1. Set up callout notification   2. Make asynchronous requests  The following sections describes the high-level steps for you to get the most of the asynchronous API. For detailed instructions, see [Make asynchronous requests](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Make_asynchronous_requests) in the Knowledge Center.   ### Set up notifications  You can create callout notification definitions based on the following custom events through the Zuora UI or the [Create a notification definition](https://www.zuora.com/developer/api-reference/#operation/POST_Create_Notification_Definition) API operation:   * Async Request Succeeded   * Async Request Failed  This step ensures that your system receives a callout when an asynchronous request succeeds or fails.   ### Make asynchronous requests  By design, asynchronous requests differ from their synchronous counterparts in endpoints, and the HTTP status response code and response body they return. ​​The header parameters and request body schema for asynchronous operations are the same as their synchronous counterparts.   * The endpoints for asynchronous API operations contain `/async` in the path after `/v1`. See the following table for examples:  | Operation               | Synchronous endpoint  | Asynchronous endpoint      | |:-------- |:-------- |:-------- | | Create an account       | `/v1/accounts`        | `/v1/async/accounts`       | | CRUD: Create an account | `/v1/object/account`  | `/v1/async/object/account` |  * Unlike the 200 OK response for synchronous requests, Zuora returns a 202 Accepted response for all asynchronous requests, and the response body contains only a request ID.   **Note**: These asynchronous API endpoints are in addition to the previously introduced endpoints that support asynchronous processing. You should continue to use them:   * [Perform a mass action](https://www.zuora.com/developer/api-reference/#operation/POST_MassUpdater)   * [Create an order asynchronously](https://www.zuora.com/developer/api-reference/#operation/POST_CreateOrderAsynchronously)   * [Preview an order asynchronously](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrderAsynchronously)   * [Create a job to hard delete billing document files](https://www.zuora.com/developer/api-reference/#operation/POST_BillingDocumentFilesDeletionJob)   * [CRUD: Post or cancel a bill run](https://www.zuora.com/developer/api-reference/#operation/Object_PUTBillRun)   * [Cancel a journal run](https://www.zuora.com/developer/api-reference/#operation/PUT_JournalRun)   * [Run trial balance](https://www.zuora.com/developer/api-reference/#operation/PUT_RunTrialBalance)  For more information, see [Make asynchronous requests](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Make_asynchronous_requests).  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.   # Error Handling  If a request to Zuora Billing REST API with an endpoint starting with `/v1` (except [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations) fails, the response will contain an eight-digit error code with a corresponding error message to indicate the details of the error.  The following code snippet is a sample error response that contains an error code and message pair:  ```  {    \"success\": false,    \"processId\": \"CBCFED6580B4E076\",    \"reasons\":  [      {       \"code\": 53100320,       \"message\": \"'termType' value should be one of: TERMED, EVERGREEN\"      }     ]  } ``` The `success` field indicates whether the API request has succeeded. The `processId` field is a Zuora internal ID that you can provide to Zuora Global Support for troubleshooting purposes.  The `reasons` field contains the actual error code and message pair. The error code begins with `5` or `6` means that you encountered a certain issue that is specific to a REST API resource in Zuora Billing. For example, `53100320` indicates that an invalid value is specified for the `termType` field of the `subscription` object.  The error code beginning with `9` usually indicates that an authentication-related issue occurred, and it can also indicate other unexpected errors depending on different cases. For example, `90000011` indicates that an invalid credential is provided in the request header.   When troubleshooting the error, you can divide the error code into two components: REST API resource code and error category code. See the following Zuora error code sample:  <a href=\"https://assets.zuora.com/zuora-documentation/ZuoraErrorCode.jpeg\" target=\"_blank\"><img src=\"https://assets.zuora.com/zuora-documentation/ZuoraErrorCode.jpeg\" alt=\"Zuora Error Code Sample\"></a>   **Note:** Zuora determines resource codes based on the request payload. Therefore, if GET and DELETE requests that do not contain payloads fail, you will get `500000` as the resource code, which indicates an unknown object and an unknown field.  The error category code of these requests is valid and follows the rules described in the [Error Category Code](https://www.zuora.com/developer/api-reference/#section/Error-Handling/Error-Category-Code) section.  In such case, you can refer to the returned error message to troubleshoot.   ## REST API Resource Code  The 6-digit resource code indicates the REST API resource, typically a field of a Zuora object, on which the issue occurs. In the preceding example, `531003` refers to the `termType` field of the `subscription` object.   The value range for all REST API resource codes is from `500000` to `679999`. See [Resource Codes](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Resource_Codes) in the Knowledge Center for a full list of resource codes.  ## Error Category Code  The 2-digit error category code identifies the type of error, for example, resource not found or missing required field.   The following table describes all error categories and the corresponding resolution:  | Code    | Error category              | Description    | Resolution    | |:--------|:--------|:--------|:--------| | 10      | Permission or access denied | The request cannot be processed because a certain tenant or user permission is missing. | Check the missing tenant or user permission in the response message and contact [Zuora Global Support](https://support.zuora.com) for enablement. | | 11      | Authentication failed       | Authentication fails due to invalid API authentication credentials. | Ensure that a valid API credential is specified. | | 20      | Invalid format or value     | The request cannot be processed due to an invalid field format or value. | Check the invalid field in the error message, and ensure that the format and value of all fields you passed in are valid. | | 21      | Unknown field in request    | The request cannot be processed because an unknown field exists in the request body. | Check the unknown field name in the response message, and ensure that you do not include any unknown field in the request body. | | 22      | Missing required field      | The request cannot be processed because a required field in the request body is missing. | Check the missing field name in the response message, and ensure that you include all required fields in the request body. | | 23      | Missing required parameter  | The request cannot be processed because a required query parameter is missing. | Check the missing parameter name in the response message, and ensure that you include the parameter in the query. | | 30      | Rule restriction            | The request cannot be processed due to the violation of a Zuora business rule. | Check the response message and ensure that the API request meets the specified business rules. | | 40      | Not found                   | The specified resource cannot be found. | Check the response message and ensure that the specified resource exists in your Zuora tenant. | | 45      | Unsupported request         | The requested endpoint does not support the specified HTTP method. | Check your request and ensure that the endpoint and method matches. | | 50      | Locking contention          | This request cannot be processed because the objects this request is trying to modify are being modified by another API request, UI operation, or batch job process. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact [Zuora Global Support](https://support.zuora.com) with the returned `Zuora-Request-Id` value in the response header for assistance.</p> | | 60      | Internal error              | The server encounters an internal error. | Contact [Zuora Global Support](https://support.zuora.com) with the returned `Zuora-Request-Id` value in the response header for assistance. | | 70      | Request exceeded limit      | The total number of concurrent requests exceeds the limit allowed by the system. | <p>Resubmit the request after the number of seconds specified by the `Retry-After` value in the response header.</p> <p>Check [Concurrent request limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits) for details about Zuora’s concurrent request limit policy.</p> | | 90      | Malformed request           | The request cannot be processed due to JSON syntax errors. | Check the syntax error in the JSON request body and ensure that the request is in the correct JSON format. | | 99      | Integration error           | The server encounters an error when communicating with an external system, for example, payment gateway, tax engine provider. | Check the response message and take action accordingly. |   # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. | | chargeId | 256.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | productRatePlanChargeId | 257.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | comment | 256.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Comments about the product rate plan charge, invoice item, or memo item. | | description | 257.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Description of the the product rate plan charge, invoice item, or memo item. | | taxationItems | 309.0 and later | [Preview an order](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrder \"Preview an order\") | List of taxation items for an invoice item or a credit memo item. | | batch | 309.0 and earlier | [Create a billing preview run](https://www.zuora.com/developer/api-reference/#operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. |       | batches | 314.0 and later | [Create a billing preview run](https://www.zuora.com/developer/api-reference/#operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. | | taxationItems | 315.0 and later | [Preview a subscription](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewSubscription \"Preview a subscription\"); [Update a subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update a subscription\")| List of taxation items for an invoice item or a credit memo item. |    #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Billing Object Model  The following diagram is a high-level view of how key business objects are related to one another within Zuora Billing.  Click the diagram to open it in a new tab and zoom in. For more information about the different sections of the diagram, see <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/A_Zuora_Billing_business_object_model\" target=\"_blank\">Zuora Billing business object model</a>.  <a href=\"https://assets.zuora.com/zuora-documentation/Zuora_Billing_object_model_Sep2020.png\" target=\"_blank\"><img src=\"https://assets.zuora.com/zuora-documentation/Zuora_Billing_object_model_Sep2020.png\" alt=\"Zuora Billing object model diagram\"></a>  This diagram is intended to provide a conceptual understanding; it does not illustrate a specific way to integrate with Zuora.  The diagram includes the Orders feature and the Invoice Settlement feature. If your organization does not use either of these features, see <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/B_Zuora_Billing_business_object_model_prior_to_Orders_and_Invoice_Settlement\" target=\"_blank\">Zuora Billing business object model prior to Orders and Invoice Settlement</a> for an alternative diagram.  ## API Names  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun` - API name used  in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query.</p> <p>`BillRun` - API name used in the [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions). See the CRUD oprations of [Bill Run](https://www.zuora.com/developer/api-reference/#tag/Bill-Run) for more information about the `BillRun` object. `BillingRun` and `BillRun` have different fields. |                      | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Notification History - Callout                | `CalloutHistory`                           | | Notification History - Email                  | `EmailHistory`                             | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Line Items                              | `OrderLineItems`                           |     | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    The version of the OpenAPI document: 2022-02-10
    Contact: docs@zuora.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PaymentMethodsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def d_elete_payment_methods(self, payment_method_id, **kwargs):  # noqa: E501
        """Delete a payment method  # noqa: E501

        Deletes a credit card payment method.  If the specified payment method is the account's default payment method, the request will fail.  In that case, you must first designate a different payment method for that customer to be the default.  For a use case of this operation, see [Configure Payment Methods](https://www.zuora.com/developer/api-guides/#Configure-payment-methods).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_elete_payment_methods(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique identifier of a payment method. (Since this ID is unique, and linked to a customer account in the system, no customer identifier is needed.) (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.d_elete_payment_methods_with_http_info(payment_method_id, **kwargs)  # noqa: E501

    def d_elete_payment_methods_with_http_info(self, payment_method_id, **kwargs):  # noqa: E501
        """Delete a payment method  # noqa: E501

        Deletes a credit card payment method.  If the specified payment method is the account's default payment method, the request will fail.  In that case, you must first designate a different payment method for that customer to be the default.  For a use case of this operation, see [Configure Payment Methods](https://www.zuora.com/developer/api-guides/#Configure-payment-methods).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_elete_payment_methods_with_http_info(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique identifier of a payment method. (Since this ID is unique, and linked to a customer account in the system, no customer identifier is needed.) (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CommonResponseType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method d_elete_payment_methods" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `d_elete_payment_methods`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `d_elete_payment_methods`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_payment_method(self, payment_method_id, **kwargs):  # noqa: E501
        """Retrieve a payment method  # noqa: E501

        This operation allows you to get the detailed information about a payment method.  **Note:** This operation also supports retrieving the custom payment method created through the [Open Payment Method](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) service.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_payment_method(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique ID of the payment method to update. (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GETPaymentMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.g_et_payment_method_with_http_info(payment_method_id, **kwargs)  # noqa: E501

    def g_et_payment_method_with_http_info(self, payment_method_id, **kwargs):  # noqa: E501
        """Retrieve a payment method  # noqa: E501

        This operation allows you to get the detailed information about a payment method.  **Note:** This operation also supports retrieving the custom payment method created through the [Open Payment Method](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) service.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_payment_method_with_http_info(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique ID of the payment method to update. (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GETPaymentMethodResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_payment_method" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `g_et_payment_method`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `g_et_payment_method`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETPaymentMethodResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_payment_methods_credit_card(self, account_key, **kwargs):  # noqa: E501
        """List all credit card payment methods of an account  # noqa: E501

        This REST API reference describes how to retrieve all credit card information for the specified customer account.   ## Notes The response includes details of credit or debit cards for the specified customer account. Card numbers are masked. For example: ``` ************1234 ```  Though you can also send requests for bank transfer, ACH, or other supported payment methods, the response will not include effective details of these payment methods.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_payment_methods_credit_card(account_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_key: Account number or account ID. (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GETPaymentMethodsType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.g_et_payment_methods_credit_card_with_http_info(account_key, **kwargs)  # noqa: E501

    def g_et_payment_methods_credit_card_with_http_info(self, account_key, **kwargs):  # noqa: E501
        """List all credit card payment methods of an account  # noqa: E501

        This REST API reference describes how to retrieve all credit card information for the specified customer account.   ## Notes The response includes details of credit or debit cards for the specified customer account. Card numbers are masked. For example: ``` ************1234 ```  Though you can also send requests for bank transfer, ACH, or other supported payment methods, the response will not include effective details of these payment methods.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_payment_methods_credit_card_with_http_info(account_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str account_key: Account number or account ID. (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GETPaymentMethodsType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'account_key',
            'zuora_track_id',
            'zuora_entity_ids',
            'page_size'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_payment_methods_credit_card" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'account_key' is set
        if self.api_client.client_side_validation and ('account_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['account_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `account_key` when calling `g_et_payment_methods_credit_card`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `g_et_payment_methods_credit_card`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] > 40:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `g_et_payment_methods_credit_card`, must be a value less than or equal to `40`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'account_key' in local_var_params:
            path_params['account-key'] = local_var_params['account_key']  # noqa: E501

        query_params = []
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/credit-cards/accounts/{account-key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETPaymentMethodsType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_stored_credential_profiles(self, payment_method_id, **kwargs):  # noqa: E501
        """List stored credential profiles of a payment method  # noqa: E501

        Retrieves the stored credential profiles within a payment method.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_stored_credential_profiles(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param bool include_all: Specifies whether to retrieve all the stored credential profiles within the payment method.  By default, Zuora returns only the stored credential profiles with `Agreed` or `Active` status. If you set this parameter to `true`, Zuora returns all the stored credential profiles. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetStoredCredentialProfilesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.g_et_stored_credential_profiles_with_http_info(payment_method_id, **kwargs)  # noqa: E501

    def g_et_stored_credential_profiles_with_http_info(self, payment_method_id, **kwargs):  # noqa: E501
        """List stored credential profiles of a payment method  # noqa: E501

        Retrieves the stored credential profiles within a payment method.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_stored_credential_profiles_with_http_info(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param bool include_all: Specifies whether to retrieve all the stored credential profiles within the payment method.  By default, Zuora returns only the stored credential profiles with `Agreed` or `Active` status. If you set this parameter to `true`, Zuora returns all the stored credential profiles. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetStoredCredentialProfilesResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'zuora_track_id',
            'zuora_entity_ids',
            'include_all'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_stored_credential_profiles" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `g_et_stored_credential_profiles`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `g_et_stored_credential_profiles`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []
        if 'include_all' in local_var_params and local_var_params['include_all'] is not None:  # noqa: E501
            query_params.append(('includeAll', local_var_params['include_all']))  # noqa: E501

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/profiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetStoredCredentialProfilesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def object_delete_payment_method(self, id, **kwargs):  # noqa: E501
        """CRUD: Delete a payment method  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_delete_payment_method(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Object id (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProxyDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.object_delete_payment_method_with_http_info(id, **kwargs)  # noqa: E501

    def object_delete_payment_method_with_http_info(self, id, **kwargs):  # noqa: E501
        """CRUD: Delete a payment method  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_delete_payment_method_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Object id (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProxyDeleteResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'zuora_entity_ids',
            'zuora_track_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_delete_payment_method" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `object_delete_payment_method`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `object_delete_payment_method`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/object/payment-method/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProxyDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def object_get_payment_method(self, id, **kwargs):  # noqa: E501
        """CRUD: Retrieve a payment method  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_get_payment_method(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Object id (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str fields: Object fields to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProxyGetPaymentMethod
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.object_get_payment_method_with_http_info(id, **kwargs)  # noqa: E501

    def object_get_payment_method_with_http_info(self, id, **kwargs):  # noqa: E501
        """CRUD: Retrieve a payment method  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_get_payment_method_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Object id (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str fields: Object fields to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProxyGetPaymentMethod, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'zuora_entity_ids',
            'zuora_track_id',
            'fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_get_payment_method" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `object_get_payment_method`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `object_get_payment_method`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/object/payment-method/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProxyGetPaymentMethod',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def object_post_payment_method(self, create_request, **kwargs):  # noqa: E501
        """CRUD: Create a payment method  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_post_payment_method(create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ProxyCreatePaymentMethod create_request: (required)
        :param bool reject_unknown_fields: Specifies whether the call fails if the request body contains unknown fields. With `rejectUnknownFields` set to `true`, Zuora returns a 400 response if the request body contains unknown fields. The body of the 400 response is:  ```json {     \"message\": \"Error - unrecognised fields\" } ```  By default, Zuora ignores unknown fields in the request body. 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProxyCreateOrModifyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.object_post_payment_method_with_http_info(create_request, **kwargs)  # noqa: E501

    def object_post_payment_method_with_http_info(self, create_request, **kwargs):  # noqa: E501
        """CRUD: Create a payment method  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_post_payment_method_with_http_info(create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ProxyCreatePaymentMethod create_request: (required)
        :param bool reject_unknown_fields: Specifies whether the call fails if the request body contains unknown fields. With `rejectUnknownFields` set to `true`, Zuora returns a 400 response if the request body contains unknown fields. The body of the 400 response is:  ```json {     \"message\": \"Error - unrecognised fields\" } ```  By default, Zuora ignores unknown fields in the request body. 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProxyCreateOrModifyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'create_request',
            'reject_unknown_fields',
            'zuora_entity_ids',
            'zuora_track_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_post_payment_method" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_request' is set
        if self.api_client.client_side_validation and ('create_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_request` when calling `object_post_payment_method`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `object_post_payment_method`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'reject_unknown_fields' in local_var_params and local_var_params['reject_unknown_fields'] is not None:  # noqa: E501
            query_params.append(('rejectUnknownFields', local_var_params['reject_unknown_fields']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_request' in local_var_params:
            body_params = local_var_params['create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/object/payment-method', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProxyCreateOrModifyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def object_put_payment_method(self, id, modify_request, **kwargs):  # noqa: E501
        """CRUD: Update a payment method  # noqa: E501

        For a use case of this operation, see [Configure Payment Methods](https://www.zuora.com/developer/api-guides/#Configure-payment-methods).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_put_payment_method(id, modify_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Object id (required)
        :param ProxyModifyPaymentMethod modify_request: (required)
        :param bool reject_unknown_fields: Specifies whether the call fails if the request body contains unknown fields. With `rejectUnknownFields` set to `true`, Zuora returns a 400 response if the request body contains unknown fields. The body of the 400 response is:  ```json {     \"message\": \"Error - unrecognised fields\" } ```  By default, Zuora ignores unknown fields in the request body. 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProxyCreateOrModifyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.object_put_payment_method_with_http_info(id, modify_request, **kwargs)  # noqa: E501

    def object_put_payment_method_with_http_info(self, id, modify_request, **kwargs):  # noqa: E501
        """CRUD: Update a payment method  # noqa: E501

        For a use case of this operation, see [Configure Payment Methods](https://www.zuora.com/developer/api-guides/#Configure-payment-methods).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.object_put_payment_method_with_http_info(id, modify_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Object id (required)
        :param ProxyModifyPaymentMethod modify_request: (required)
        :param bool reject_unknown_fields: Specifies whether the call fails if the request body contains unknown fields. With `rejectUnknownFields` set to `true`, Zuora returns a 400 response if the request body contains unknown fields. The body of the 400 response is:  ```json {     \"message\": \"Error - unrecognised fields\" } ```  By default, Zuora ignores unknown fields in the request body. 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProxyCreateOrModifyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'modify_request',
            'reject_unknown_fields',
            'zuora_entity_ids',
            'zuora_track_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_put_payment_method" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `object_put_payment_method`")  # noqa: E501
        # verify the required parameter 'modify_request' is set
        if self.api_client.client_side_validation and ('modify_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['modify_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `modify_request` when calling `object_put_payment_method`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `object_put_payment_method`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'reject_unknown_fields' in local_var_params and local_var_params['reject_unknown_fields'] is not None:  # noqa: E501
            query_params.append(('rejectUnknownFields', local_var_params['reject_unknown_fields']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'modify_request' in local_var_params:
            body_params = local_var_params['modify_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/object/payment-method/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProxyCreateOrModifyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_cancel_authorization(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Cancel authorization  # noqa: E501

        Allows you to cancel an authorization.   The following payment gateways support this operation:   - Adyen Integration v2.0   - CyberSource 1.28 and 1.97   - Chase Paymentech Orbital   - Ingenico ePayments   - Verifi Global Payment Gateway   - SlimPay   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_cancel_authorization(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The unique ID of the payment method where the authorization is cancelled.  (required)
        :param POSTVoidAuthorize request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: POSTVoidAuthorizeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_cancel_authorization_with_http_info(payment_method_id, request, **kwargs)  # noqa: E501

    def p_ost_cancel_authorization_with_http_info(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Cancel authorization  # noqa: E501

        Allows you to cancel an authorization.   The following payment gateways support this operation:   - Adyen Integration v2.0   - CyberSource 1.28 and 1.97   - Chase Paymentech Orbital   - Ingenico ePayments   - Verifi Global Payment Gateway   - SlimPay   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_cancel_authorization_with_http_info(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The unique ID of the payment method where the authorization is cancelled.  (required)
        :param POSTVoidAuthorize request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(POSTVoidAuthorizeResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_cancel_authorization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ost_cancel_authorization`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ost_cancel_authorization`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_cancel_authorization`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/voidAuthorize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTVoidAuthorizeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_cancel_stored_credential_profile(self, payment_method_id, profile_number, **kwargs):  # noqa: E501
        """Cancel a stored credential profile  # noqa: E501

        Cancels a stored credential profile within a payment method.  Cancelling the stored credential profile indicates that the stored credentials are no longer valid, per a customer request. You cannot reactivate the stored credential profile after you have cancelled it.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_cancel_stored_credential_profile(payment_method_id, profile_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param int profile_number: Number that identifies a stored credential profile within the payment method.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModifiedStoredCredentialProfileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_cancel_stored_credential_profile_with_http_info(payment_method_id, profile_number, **kwargs)  # noqa: E501

    def p_ost_cancel_stored_credential_profile_with_http_info(self, payment_method_id, profile_number, **kwargs):  # noqa: E501
        """Cancel a stored credential profile  # noqa: E501

        Cancels a stored credential profile within a payment method.  Cancelling the stored credential profile indicates that the stored credentials are no longer valid, per a customer request. You cannot reactivate the stored credential profile after you have cancelled it.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_cancel_stored_credential_profile_with_http_info(payment_method_id, profile_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param int profile_number: Number that identifies a stored credential profile within the payment method.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModifiedStoredCredentialProfileResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'profile_number',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_cancel_stored_credential_profile" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ost_cancel_stored_credential_profile`")  # noqa: E501
        # verify the required parameter 'profile_number' is set
        if self.api_client.client_side_validation and ('profile_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['profile_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `profile_number` when calling `p_ost_cancel_stored_credential_profile`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_cancel_stored_credential_profile`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501
        if 'profile_number' in local_var_params:
            path_params['profile-number'] = local_var_params['profile_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/profiles/{profile-number}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifiedStoredCredentialProfileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_create_authorization(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Create authorization  # noqa: E501

        Enables you to authorize the availability of funds for a transaction but delay the capture of funds until a later time. Subsequently, use [CRUD: Create a payment](https://www.zuora.com/developer/api-reference/#operation/Object_POSTPayment) or [Create a payment](https://www.zuora.com/developer/api-reference/#operation/POST_CreatePayment) to capture the authorized funds, or use [Cancel authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CancelAuthorization) to cancel the authorization.   The following payment gateways support this operation:  * Adyen Integration v2.0 * CyberSource 1.28 * CyberSource 1.97 * CyberSource 2.0 - This gateway supports the Delayed Capture feature for both Credit Cards and Credit Card Reference payment methods. This gateway does not support [Cancel authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CancelAuthorization). * Chase Paymentech Orbital * Ingenico ePayments * SlimPay * Verifi Global Payment Gateway  If you have the Invoice Settlement feature enabled, use the [Create payment](https://www.zuora.com/developer/api-reference/#operation/POST_CreatePayment) operation to capture the funds instead of the [CRUD: Create payment](https://www.zuora.com/developer/api-reference/#operation/Object_POSTPayment) operation.          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_create_authorization(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The unique ID of the payment method where the authorization is created.  (required)
        :param POSTDelayAuthorizeCapture request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: POSTAuthorizeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_create_authorization_with_http_info(payment_method_id, request, **kwargs)  # noqa: E501

    def p_ost_create_authorization_with_http_info(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Create authorization  # noqa: E501

        Enables you to authorize the availability of funds for a transaction but delay the capture of funds until a later time. Subsequently, use [CRUD: Create a payment](https://www.zuora.com/developer/api-reference/#operation/Object_POSTPayment) or [Create a payment](https://www.zuora.com/developer/api-reference/#operation/POST_CreatePayment) to capture the authorized funds, or use [Cancel authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CancelAuthorization) to cancel the authorization.   The following payment gateways support this operation:  * Adyen Integration v2.0 * CyberSource 1.28 * CyberSource 1.97 * CyberSource 2.0 - This gateway supports the Delayed Capture feature for both Credit Cards and Credit Card Reference payment methods. This gateway does not support [Cancel authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CancelAuthorization). * Chase Paymentech Orbital * Ingenico ePayments * SlimPay * Verifi Global Payment Gateway  If you have the Invoice Settlement feature enabled, use the [Create payment](https://www.zuora.com/developer/api-reference/#operation/POST_CreatePayment) operation to capture the funds instead of the [CRUD: Create payment](https://www.zuora.com/developer/api-reference/#operation/Object_POSTPayment) operation.          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_create_authorization_with_http_info(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The unique ID of the payment method where the authorization is created.  (required)
        :param POSTDelayAuthorizeCapture request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(POSTAuthorizeResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_create_authorization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ost_create_authorization`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ost_create_authorization`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_create_authorization`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/authorize', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTAuthorizeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_create_stored_credential_profile(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Create a stored credential profile  # noqa: E501

        Creates a stored credential profile within a payment method.  The stored credential profile represents a consent agreement that you have established with a customer. When you use the payment method in a transaction, Zuora may include information from the stored credential profile to inform the payment processor that the transaction is related to your pre-existing consent agreement with the customer.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_create_stored_credential_profile(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param CreateStoredCredentialProfileRequest request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModifiedStoredCredentialProfileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_create_stored_credential_profile_with_http_info(payment_method_id, request, **kwargs)  # noqa: E501

    def p_ost_create_stored_credential_profile_with_http_info(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Create a stored credential profile  # noqa: E501

        Creates a stored credential profile within a payment method.  The stored credential profile represents a consent agreement that you have established with a customer. When you use the payment method in a transaction, Zuora may include information from the stored credential profile to inform the payment processor that the transaction is related to your pre-existing consent agreement with the customer.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_create_stored_credential_profile_with_http_info(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param CreateStoredCredentialProfileRequest request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModifiedStoredCredentialProfileResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_create_stored_credential_profile" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ost_create_stored_credential_profile`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ost_create_stored_credential_profile`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_create_stored_credential_profile`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/profiles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifiedStoredCredentialProfileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_expire_stored_credential_profile(self, payment_method_id, profile_number, **kwargs):  # noqa: E501
        """Expire a stored credential profile  # noqa: E501

        Expires a stored credential profile within a payment method.  Expiring the stored credential profile indicates that the stored credentials are no longer valid, per an expiration policy in the stored credential transaction framework. You cannot reactivate the stored credential profile after you have expired it.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_expire_stored_credential_profile(payment_method_id, profile_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param int profile_number: Number that identifies a stored credential profile within the payment method.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModifiedStoredCredentialProfileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_expire_stored_credential_profile_with_http_info(payment_method_id, profile_number, **kwargs)  # noqa: E501

    def p_ost_expire_stored_credential_profile_with_http_info(self, payment_method_id, profile_number, **kwargs):  # noqa: E501
        """Expire a stored credential profile  # noqa: E501

        Expires a stored credential profile within a payment method.  Expiring the stored credential profile indicates that the stored credentials are no longer valid, per an expiration policy in the stored credential transaction framework. You cannot reactivate the stored credential profile after you have expired it.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_expire_stored_credential_profile_with_http_info(payment_method_id, profile_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: ID of a payment method.  (required)
        :param int profile_number: Number that identifies a stored credential profile within the payment method.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModifiedStoredCredentialProfileResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'profile_number',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_expire_stored_credential_profile" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ost_expire_stored_credential_profile`")  # noqa: E501
        # verify the required parameter 'profile_number' is set
        if self.api_client.client_side_validation and ('profile_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['profile_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `profile_number` when calling `p_ost_expire_stored_credential_profile`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_expire_stored_credential_profile`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501
        if 'profile_number' in local_var_params:
            path_params['profile-number'] = local_var_params['profile_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/profiles/{profile-number}/expire', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifiedStoredCredentialProfileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_payment_methods(self, request, **kwargs):  # noqa: E501
        """Create a payment method  # noqa: E501

        You can use this operation to create either a payment method associated with a specific customer account, or an orphan payment method that is not associated with any customer account. The orphan payment method must be associated with a customer account within 10 days. Otherwise, it will be deleted.  This operation supports the payment methods listed below.  ### PayPal Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (required)  ### PayPal Native Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (optional)  ### PayPal Adaptive The following request body fields are specific to this payment method: * `preapprovalKey` (required) * `email` (required)  ### Credit Card The following request body fields are applicable to this payment method: * `cardHolderInfo` (`cardHolderName` required) * `cardNumber` (required) * `cardType` (required) * `expirationMonth` (required) * `expirationYear` (required) * `mitConsentAgreementRef` * `mitConsentAgreementSrc` * `mitNetworkTransactionId` * `mitProfileAction` * `mitProfileType` * `mitProfileAgreedOn` * `securityCode` * `checkDuplicated` * `mandateInfo`  ### Credit Card (CC) Reference Transaction The following request body fields are applicable to this payment method: * `tokenId` (required) * `secondTokenId` * `creditCardMaskNumber` * `mandateInfo`  ### ACH The following request body fields are applicable to this payment method: * `bankABACode` (required) * `bankAccountName` (required) * `bankAccountNumber` (required) * `bankAccountType` (required) * `bankName` (required) * `addressLine1` * `addressLine2` * `phone` * `email` * `city` * `country` * `state` * `zipCode` * `mandateInfo`  ### SEPA The following request body fields are applicable to this payment method: * `IBAN` (required) * `accountHolderInfo` (required) * `businessIdentificationCode` * `mandateInfo`  ### Betalingsservice (Direct Debit DK) The following request body fields are applicable to this payment method: * `accountNumber` (required) * `identityNumber` (required) * `bankCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Autogiro (Direct Debit SE) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `identityNumber` (required) * `branchCode` (required) * `accountHolderInfo` (required)  * `mandateInfo`  ### Bacs (Direct Debit UK) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `bankCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Becs (Direct Entry AU) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `branchCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Becsnz (Direct Debit NZ) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `bankCode` (required) * `branchCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### PAD (Pre-Authorized Debit) The following request body fields are applicable to this payment method: * `accountNumber` (required) * `bankCode` (required) * `branchCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Apple Pay on Adyen Integration v2.0 Only available in the Sandbox environment. See [Set up Adyen Apple Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Apple_Pay_on_Web/Set_up_Adyen_Apple_Pay) for details.  ### Google Pay on Adyen Integration v2.0 Only available in the Sandbox environment. See [Set up Adyen Google Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Set_up_Adyen_Google_Pay) for details.  ### Custom payment methods Note: This feature is in the Early Adopter phase. If you want to use this feature, submit a request at [Zuora Global Support](http://support.zuora.com/) to enable the Universal Payment Connector and Open Payment Method services that support this feature.  With the support of Universal Payment Connector (UPC) and Open Payment Method (OPM) services, you can create custom payment methods by using the fields defined in a definition file for this type of custom payment method. See [Set up custom payment gateways and payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) for details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_payment_methods(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param POSTPaymentMethodRequest request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: POSTPaymentMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_payment_methods_with_http_info(request, **kwargs)  # noqa: E501

    def p_ost_payment_methods_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create a payment method  # noqa: E501

        You can use this operation to create either a payment method associated with a specific customer account, or an orphan payment method that is not associated with any customer account. The orphan payment method must be associated with a customer account within 10 days. Otherwise, it will be deleted.  This operation supports the payment methods listed below.  ### PayPal Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (required)  ### PayPal Native Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (optional)  ### PayPal Adaptive The following request body fields are specific to this payment method: * `preapprovalKey` (required) * `email` (required)  ### Credit Card The following request body fields are applicable to this payment method: * `cardHolderInfo` (`cardHolderName` required) * `cardNumber` (required) * `cardType` (required) * `expirationMonth` (required) * `expirationYear` (required) * `mitConsentAgreementRef` * `mitConsentAgreementSrc` * `mitNetworkTransactionId` * `mitProfileAction` * `mitProfileType` * `mitProfileAgreedOn` * `securityCode` * `checkDuplicated` * `mandateInfo`  ### Credit Card (CC) Reference Transaction The following request body fields are applicable to this payment method: * `tokenId` (required) * `secondTokenId` * `creditCardMaskNumber` * `mandateInfo`  ### ACH The following request body fields are applicable to this payment method: * `bankABACode` (required) * `bankAccountName` (required) * `bankAccountNumber` (required) * `bankAccountType` (required) * `bankName` (required) * `addressLine1` * `addressLine2` * `phone` * `email` * `city` * `country` * `state` * `zipCode` * `mandateInfo`  ### SEPA The following request body fields are applicable to this payment method: * `IBAN` (required) * `accountHolderInfo` (required) * `businessIdentificationCode` * `mandateInfo`  ### Betalingsservice (Direct Debit DK) The following request body fields are applicable to this payment method: * `accountNumber` (required) * `identityNumber` (required) * `bankCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Autogiro (Direct Debit SE) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `identityNumber` (required) * `branchCode` (required) * `accountHolderInfo` (required)  * `mandateInfo`  ### Bacs (Direct Debit UK) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `bankCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Becs (Direct Entry AU) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `branchCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Becsnz (Direct Debit NZ) The following request body fields are applicable to this payment method:         * `accountNumber` (required) * `bankCode` (required) * `branchCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### PAD (Pre-Authorized Debit) The following request body fields are applicable to this payment method: * `accountNumber` (required) * `bankCode` (required) * `branchCode` (required) * `accountHolderInfo` (required) * `mandateInfo`  ### Apple Pay on Adyen Integration v2.0 Only available in the Sandbox environment. See [Set up Adyen Apple Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Apple_Pay_on_Web/Set_up_Adyen_Apple_Pay) for details.  ### Google Pay on Adyen Integration v2.0 Only available in the Sandbox environment. See [Set up Adyen Google Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Set_up_Adyen_Google_Pay) for details.  ### Custom payment methods Note: This feature is in the Early Adopter phase. If you want to use this feature, submit a request at [Zuora Global Support](http://support.zuora.com/) to enable the Universal Payment Connector and Open Payment Method services that support this feature.  With the support of Universal Payment Connector (UPC) and Open Payment Method (OPM) services, you can create custom payment methods by using the fields defined in a definition file for this type of custom payment method. See [Set up custom payment gateways and payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) for details.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_payment_methods_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param POSTPaymentMethodRequest request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(POSTPaymentMethodResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_payment_methods" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ost_payment_methods`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_payment_methods`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTPaymentMethodResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_payment_methods_credit_card(self, request, **kwargs):  # noqa: E501
        """Create a credit card payment method  # noqa: E501

        You can create a credit card payment method for a customer account or an orphan credit card payment method that is not associated with any customer account. The orphan payment method must be associated with a customer account within 10 days. Otherwise, it will be deleted.  This API call is CORS Enabled. Use client-side JavaScript to invoke the call.   **Note**: If you use this operation to create credit card payment methods instead of using the [iFrame of Hosted Payment Pages](https://knowledgecenter.zuora.com/CB_Billing/LA_Hosted_Payment_Pages/C_Hosted_Payment_Pages/B_Implementing_Hosted_Payment_Pages_on_Your_Website/C_Embed_and_Submit_the_iFrame), you are subject to PCI-compliance audit requirements.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_payment_methods_credit_card(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param POSTPaymentMethodType request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: POSTPaymentMethodResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_payment_methods_credit_card_with_http_info(request, **kwargs)  # noqa: E501

    def p_ost_payment_methods_credit_card_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create a credit card payment method  # noqa: E501

        You can create a credit card payment method for a customer account or an orphan credit card payment method that is not associated with any customer account. The orphan payment method must be associated with a customer account within 10 days. Otherwise, it will be deleted.  This API call is CORS Enabled. Use client-side JavaScript to invoke the call.   **Note**: If you use this operation to create credit card payment methods instead of using the [iFrame of Hosted Payment Pages](https://knowledgecenter.zuora.com/CB_Billing/LA_Hosted_Payment_Pages/C_Hosted_Payment_Pages/B_Implementing_Hosted_Payment_Pages_on_Your_Website/C_Embed_and_Submit_the_iFrame), you are subject to PCI-compliance audit requirements.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_payment_methods_credit_card_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param POSTPaymentMethodType request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(POSTPaymentMethodResponseType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_payment_methods_credit_card" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ost_payment_methods_credit_card`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_payment_methods_credit_card`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/credit-cards', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTPaymentMethodResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_payment_methods_decryption(self, request, **kwargs):  # noqa: E501
        """Create an Apple Pay payment method  # noqa: E501

        The decryption API endpoint can conditionally perform 3 tasks in one atomic call:   * Decrypt Apple Pay Payment token   * Create Credit Card Payment Method in Zuora with decrypted Apple Pay information   * Process Payment on a specified Invoice (optional)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_payment_methods_decryption(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param POSTPaymentMethodDecryption request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: POSTPaymentMethodResponseDecryption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ost_payment_methods_decryption_with_http_info(request, **kwargs)  # noqa: E501

    def p_ost_payment_methods_decryption_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create an Apple Pay payment method  # noqa: E501

        The decryption API endpoint can conditionally perform 3 tasks in one atomic call:   * Decrypt Apple Pay Payment token   * Create Credit Card Payment Method in Zuora with decrypted Apple Pay information   * Process Payment on a specified Invoice (optional)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_payment_methods_decryption_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param POSTPaymentMethodDecryption request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(POSTPaymentMethodResponseDecryption, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_payment_methods_decryption" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ost_payment_methods_decryption`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_payment_methods_decryption`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/decryption', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTPaymentMethodResponseDecryption',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_payment_method(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Update a payment method  # noqa: E501

        This operation allows you to update an existing payment method.   The following request body fields can be updated regardless of payment method types: * `authGateway` * `gatewayOptions` * `accountHolderInfo` * Custom fields  The following request body fields can be updated only for the Credit Card payment method: * `expirationMonth`  * `expirationYear` * `securityCode`  The following request body field can be updated for the Credit Card, Credit Card Reference Transaction, ACH, and Bank Transfer payment methods: * `mandateInfo`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_payment_method(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique ID of the payment method to update. (required)
        :param PUTPaymentMethodRequest request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PUTPaymentMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ut_payment_method_with_http_info(payment_method_id, request, **kwargs)  # noqa: E501

    def p_ut_payment_method_with_http_info(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Update a payment method  # noqa: E501

        This operation allows you to update an existing payment method.   The following request body fields can be updated regardless of payment method types: * `authGateway` * `gatewayOptions` * `accountHolderInfo` * Custom fields  The following request body fields can be updated only for the Credit Card payment method: * `expirationMonth`  * `expirationYear` * `securityCode`  The following request body field can be updated for the Credit Card, Credit Card Reference Transaction, ACH, and Bank Transfer payment methods: * `mandateInfo`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_payment_method_with_http_info(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique ID of the payment method to update. (required)
        :param PUTPaymentMethodRequest request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PUTPaymentMethodResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_payment_method" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ut_payment_method`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ut_payment_method`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ut_payment_method`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PUTPaymentMethodResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_payment_methods_credit_card(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Update a credit card payment method  # noqa: E501

        Updates an existing credit card payment method.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_payment_methods_credit_card(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique ID of the payment method to update. (required)
        :param PUTPaymentMethodType request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PUTPaymentMethodResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ut_payment_methods_credit_card_with_http_info(payment_method_id, request, **kwargs)  # noqa: E501

    def p_ut_payment_methods_credit_card_with_http_info(self, payment_method_id, request, **kwargs):  # noqa: E501
        """Update a credit card payment method  # noqa: E501

        Updates an existing credit card payment method.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_payment_methods_credit_card_with_http_info(payment_method_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: Unique ID of the payment method to update. (required)
        :param PUTPaymentMethodType request: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PUTPaymentMethodResponseType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'request',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_payment_methods_credit_card" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ut_payment_methods_credit_card`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in local_var_params or  # noqa: E501
                                                        local_var_params['request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request` when calling `p_ut_payment_methods_credit_card`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ut_payment_methods_credit_card`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in local_var_params:
            body_params = local_var_params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/credit-cards/{payment-method-id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PUTPaymentMethodResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_scrub_payment_methods(self, payment_method_id, **kwargs):  # noqa: E501
        """Scrub a payment method  # noqa: E501

         This operation enables you to replace all sensitive data in a payment method, related payment method snapshot table, and four related log tables with dummy values that will be stored in Zuora databases.   This operation will scrub the sensitive data and soft-delete the specified payment method at the same time.   If you want to delete or anonymize personal data in Zuora, you must scrub the payment method before anonymizing the associated account and contact. See [Delete or anonymize personal data](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Responding_to_individual_requests_for_access%2C_correction%2C_and_deletion_of_data_under_applicable_privacy_laws#Edit_and_correct_personal_data) for more information.  **Note:** In order to use this operation, you must ensure that the **Scrub Sensitive Data of Specific Payment Method payments** permission is enabled in your user role. Contact your tenant administrator if you want to enable this permission. See [Scrub Payment Methods](https://knowledgecenter.zuora.com/CB_Billing/L_Payment_Methods/Scrub_Payment_Methods) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_scrub_payment_methods(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The ID of the payment method where you want to scrub the sensitive data.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ut_scrub_payment_methods_with_http_info(payment_method_id, **kwargs)  # noqa: E501

    def p_ut_scrub_payment_methods_with_http_info(self, payment_method_id, **kwargs):  # noqa: E501
        """Scrub a payment method  # noqa: E501

         This operation enables you to replace all sensitive data in a payment method, related payment method snapshot table, and four related log tables with dummy values that will be stored in Zuora databases.   This operation will scrub the sensitive data and soft-delete the specified payment method at the same time.   If you want to delete or anonymize personal data in Zuora, you must scrub the payment method before anonymizing the associated account and contact. See [Delete or anonymize personal data](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Responding_to_individual_requests_for_access%2C_correction%2C_and_deletion_of_data_under_applicable_privacy_laws#Edit_and_correct_personal_data) for more information.  **Note:** In order to use this operation, you must ensure that the **Scrub Sensitive Data of Specific Payment Method payments** permission is enabled in your user role. Contact your tenant administrator if you want to enable this permission. See [Scrub Payment Methods](https://knowledgecenter.zuora.com/CB_Billing/L_Payment_Methods/Scrub_Payment_Methods) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_scrub_payment_methods_with_http_info(payment_method_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The ID of the payment method where you want to scrub the sensitive data.  (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CommonResponseType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'zuora_track_id',
            'zuora_entity_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_scrub_payment_methods" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ut_scrub_payment_methods`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ut_scrub_payment_methods`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501
        if 'zuora_entity_ids' in local_var_params:
            header_params['Zuora-Entity-Ids'] = local_var_params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/scrub', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_verify_payment_methods(self, payment_method_id, body, **kwargs):  # noqa: E501
        """Verify a payment method  # noqa: E501

        Sends an authorization request to the corresponding payment gateway to verify the payment method, even though no changes are made for the payment method. Supported payment methods are Credit Cards and Paypal.  Zuora now supports performing a standalone zero dollar verification or one dollar authorization for credit cards. It also supports a billing agreement status check on PayPal payment methods.  If a payment method is created by Hosted Payment Pages and is not assigned to any billing account, the payment method cannot be verified through this operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_verify_payment_methods(payment_method_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The ID of the payment method to be verified.  (required)
        :param PUTVerifyPaymentMethodType body: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PUTVerifyPaymentMethodResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.p_ut_verify_payment_methods_with_http_info(payment_method_id, body, **kwargs)  # noqa: E501

    def p_ut_verify_payment_methods_with_http_info(self, payment_method_id, body, **kwargs):  # noqa: E501
        """Verify a payment method  # noqa: E501

        Sends an authorization request to the corresponding payment gateway to verify the payment method, even though no changes are made for the payment method. Supported payment methods are Credit Cards and Paypal.  Zuora now supports performing a standalone zero dollar verification or one dollar authorization for credit cards. It also supports a billing agreement status check on PayPal payment methods.  If a payment method is created by Hosted Payment Pages and is not assigned to any billing account, the payment method cannot be verified through this operation.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_verify_payment_methods_with_http_info(payment_method_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_method_id: The ID of the payment method to be verified.  (required)
        :param PUTVerifyPaymentMethodType body: (required)
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PUTVerifyPaymentMethodResponseType, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'payment_method_id',
            'body',
            'zuora_track_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_verify_payment_methods" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_method_id' is set
        if self.api_client.client_side_validation and ('payment_method_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['payment_method_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `payment_method_id` when calling `p_ut_verify_payment_methods`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `p_ut_verify_payment_methods`")  # noqa: E501

        if self.api_client.client_side_validation and ('zuora_track_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['zuora_track_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `zuora_track_id` when calling `p_ut_verify_payment_methods`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_method_id' in local_var_params:
            path_params['payment-method-id'] = local_var_params['payment_method_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_track_id' in local_var_params:
            header_params['Zuora-Track-Id'] = local_var_params['zuora_track_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/payment-methods/{payment-method-id}/verify', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PUTVerifyPaymentMethodResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
