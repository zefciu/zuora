# coding: utf-8

"""
    API Reference: Billing

      # Introduction  Welcome to the reference for the Zuora Billing REST API!  To learn about the common use cases of Zuora Billing REST APIs, check out the [API Guides](https://www.zuora.com/developer/api-guides/).  In addition to Zuora API Reference; Billing, we also provide API references for other Zuora products:    * [API Reference: Collections](https://www.zuora.com/developer/collect-api/)   * [API Reference: Revenue](https://www.zuora.com/developer/revpro-api/)      The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Billing Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Cloud 1 Production | https://rest.na.zuora.com  | |US Cloud 1 API Sandbox |  https://rest.sandbox.na.zuora.com | |US Cloud 2 Production | https://rest.zuora.com | |US Cloud 2 API Sandbox | https://rest.apisandbox.zuora.com| |US Central Sandbox | https://rest.test.zuora.com |   |US Performance Test | https://rest.pt1.zuora.com | |US Production Copy | Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints. See [REST endpoint base URL of Production Copy (Service) Environment for existing and new customers](https://community.zuora.com/t5/API/REST-endpoint-base-URL-of-Production-Copy-Service-Environment/td-p/29611) for more information. | |EU Production | https://rest.eu.zuora.com | |EU API Sandbox | https://rest.sandbox.eu.zuora.com | |EU Central Sandbox | https://rest.test.eu.zuora.com |  The Production endpoint provides access to your live user data. Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision a Sandbox tenant for you, contact your Zuora representative for assistance.   If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/communities/community-home/digestviewer/viewthread?GroupId=103&MessageKey=6a672528-d068-47fa-a111-a3f118e016f3&CommunityKey=e2a932b4-50c4-4019-a3e8-362e38714df3&tab=digestviewer&ReturnUrl=%2fcommunities%2fcommunity-home%2fdigestviewer%3fMessageKey%3db8cc94ea-9092-4974-9964-ff19dc5c6d67%26CommunityKey%3de2a932b4-50c4-4019-a3e8-362e38714df3\" target=\"_blank\">Changelog</a> of the API Reference: Billing in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. You should reuse the bearer token until it is expired. When the token is expired, call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new one.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.   ## Making asynchronous requests  Most Zuora REST API endpoints documented in this API Reference process requests synchronously. In high-throughput scenarios, your requests to these endpoints are usually rate limited.   One strategy for avoiding rate limits is to make asynchronous requests, and Zuora provides this option to you.  Making asynchronous requests allows you to scale your applications more efficiently by leveraging Zuora's infrastructure to enqueue and execute requests for you without blocking. These requests also use built-in retry semantics, which makes them much less likely to fail for non-deterministic reasons, even in extreme high-throughput scenarios.  Meanwhile, when you send a request to one of these endpoints, you can receive a response in less than 150 milliseconds and these calls are unlikely to trigger rate limit errors.   You can make asynchronous requests to the POST, PUT, or DELETE operations, except [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions), for all resources documented in this API Reference.  Take the following steps to take advantage of the asynchronous API:    1. Set up callout notification   2. Make asynchronous requests  The following sections describes the high-level steps for you to get the most of the asynchronous API. For detailed instructions, see [Make asynchronous requests](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Make_asynchronous_requests) in the Knowledge Center.   ### Set up notifications  You can create callout notification definitions based on the following custom events through the Zuora UI or the [Create a notification definition](https://www.zuora.com/developer/api-reference/#operation/POST_Create_Notification_Definition) API operation:   * Async Request Succeeded   * Async Request Failed  This step ensures that your system receives a callout when an asynchronous request succeeds or fails.   ### Make asynchronous requests  By design, asynchronous requests differ from their synchronous counterparts in endpoints, and the HTTP status response code and response body they return. ​​The header parameters and request body schema for asynchronous operations are the same as their synchronous counterparts.   * The endpoints for asynchronous API operations contain `/async` in the path after `/v1`. See the following table for examples:  | Operation               | Synchronous endpoint  | Asynchronous endpoint      | |:-------- |:-------- |:-------- | | Create an account       | `/v1/accounts`        | `/v1/async/accounts`       | | CRUD: Create an account | `/v1/object/account`  | `/v1/async/object/account` |  * Unlike the 200 OK response for synchronous requests, Zuora returns a 202 Accepted response for all asynchronous requests, and the response body contains only a request ID.   **Note**: These asynchronous API endpoints are in addition to the previously introduced endpoints that support asynchronous processing. You should continue to use them:   * [Perform a mass action](https://www.zuora.com/developer/api-reference/#operation/POST_MassUpdater)   * [Create an order asynchronously](https://www.zuora.com/developer/api-reference/#operation/POST_CreateOrderAsynchronously)   * [Preview an order asynchronously](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrderAsynchronously)   * [Create a job to hard delete billing document files](https://www.zuora.com/developer/api-reference/#operation/POST_BillingDocumentFilesDeletionJob)   * [CRUD: Post or cancel a bill run](https://www.zuora.com/developer/api-reference/#operation/Object_PUTBillRun)   * [Cancel a journal run](https://www.zuora.com/developer/api-reference/#operation/PUT_JournalRun)   * [Run trial balance](https://www.zuora.com/developer/api-reference/#operation/PUT_RunTrialBalance)  For more information, see [Make asynchronous requests](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Make_asynchronous_requests).  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.   # Error Handling  If a request to Zuora Billing REST API with an endpoint starting with `/v1` (except [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations) fails, the response will contain an eight-digit error code with a corresponding error message to indicate the details of the error.  The following code snippet is a sample error response that contains an error code and message pair:  ```  {    \"success\": false,    \"processId\": \"CBCFED6580B4E076\",    \"reasons\":  [      {       \"code\": 53100320,       \"message\": \"'termType' value should be one of: TERMED, EVERGREEN\"      }     ]  } ``` The `success` field indicates whether the API request has succeeded. The `processId` field is a Zuora internal ID that you can provide to Zuora Global Support for troubleshooting purposes.  The `reasons` field contains the actual error code and message pair. The error code begins with `5` or `6` means that you encountered a certain issue that is specific to a REST API resource in Zuora Billing. For example, `53100320` indicates that an invalid value is specified for the `termType` field of the `subscription` object.  The error code beginning with `9` usually indicates that an authentication-related issue occurred, and it can also indicate other unexpected errors depending on different cases. For example, `90000011` indicates that an invalid credential is provided in the request header.   When troubleshooting the error, you can divide the error code into two components: REST API resource code and error category code. See the following Zuora error code sample:  <a href=\"https://assets.zuora.com/zuora-documentation/ZuoraErrorCode.jpeg\" target=\"_blank\"><img src=\"https://assets.zuora.com/zuora-documentation/ZuoraErrorCode.jpeg\" alt=\"Zuora Error Code Sample\"></a>   **Note:** Zuora determines resource codes based on the request payload. Therefore, if GET and DELETE requests that do not contain payloads fail, you will get `500000` as the resource code, which indicates an unknown object and an unknown field.  The error category code of these requests is valid and follows the rules described in the [Error Category Code](https://www.zuora.com/developer/api-reference/#section/Error-Handling/Error-Category-Code) section.  In such case, you can refer to the returned error message to troubleshoot.   ## REST API Resource Code  The 6-digit resource code indicates the REST API resource, typically a field of a Zuora object, on which the issue occurs. In the preceding example, `531003` refers to the `termType` field of the `subscription` object.   The value range for all REST API resource codes is from `500000` to `679999`. See [Resource Codes](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Resource_Codes) in the Knowledge Center for a full list of resource codes.  ## Error Category Code  The 2-digit error category code identifies the type of error, for example, resource not found or missing required field.   The following table describes all error categories and the corresponding resolution:  | Code    | Error category              | Description    | Resolution    | |:--------|:--------|:--------|:--------| | 10      | Permission or access denied | The request cannot be processed because a certain tenant or user permission is missing. | Check the missing tenant or user permission in the response message and contact [Zuora Global Support](https://support.zuora.com) for enablement. | | 11      | Authentication failed       | Authentication fails due to invalid API authentication credentials. | Ensure that a valid API credential is specified. | | 20      | Invalid format or value     | The request cannot be processed due to an invalid field format or value. | Check the invalid field in the error message, and ensure that the format and value of all fields you passed in are valid. | | 21      | Unknown field in request    | The request cannot be processed because an unknown field exists in the request body. | Check the unknown field name in the response message, and ensure that you do not include any unknown field in the request body. | | 22      | Missing required field      | The request cannot be processed because a required field in the request body is missing. | Check the missing field name in the response message, and ensure that you include all required fields in the request body. | | 23      | Missing required parameter  | The request cannot be processed because a required query parameter is missing. | Check the missing parameter name in the response message, and ensure that you include the parameter in the query. | | 30      | Rule restriction            | The request cannot be processed due to the violation of a Zuora business rule. | Check the response message and ensure that the API request meets the specified business rules. | | 40      | Not found                   | The specified resource cannot be found. | Check the response message and ensure that the specified resource exists in your Zuora tenant. | | 45      | Unsupported request         | The requested endpoint does not support the specified HTTP method. | Check your request and ensure that the endpoint and method matches. | | 50      | Locking contention          | This request cannot be processed because the objects this request is trying to modify are being modified by another API request, UI operation, or batch job process. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact [Zuora Global Support](https://support.zuora.com) with the returned `Zuora-Request-Id` value in the response header for assistance.</p> | | 60      | Internal error              | The server encounters an internal error. | Contact [Zuora Global Support](https://support.zuora.com) with the returned `Zuora-Request-Id` value in the response header for assistance. | | 70      | Request exceeded limit      | The total number of concurrent requests exceeds the limit allowed by the system. | <p>Resubmit the request after the number of seconds specified by the `Retry-After` value in the response header.</p> <p>Check [Concurrent request limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits) for details about Zuora’s concurrent request limit policy.</p> | | 90      | Malformed request           | The request cannot be processed due to JSON syntax errors. | Check the syntax error in the JSON request body and ensure that the request is in the correct JSON format. | | 99      | Integration error           | The server encounters an error when communicating with an external system, for example, payment gateway, tax engine provider. | Check the response message and take action accordingly. |   # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. | | chargeId | 256.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | productRatePlanChargeId | 257.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | comment | 256.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Comments about the product rate plan charge, invoice item, or memo item. | | description | 257.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Description of the the product rate plan charge, invoice item, or memo item. | | taxationItems | 309.0 and later | [Preview an order](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrder \"Preview an order\") | List of taxation items for an invoice item or a credit memo item. | | batch | 309.0 and earlier | [Create a billing preview run](https://www.zuora.com/developer/api-reference/#operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. |       | batches | 314.0 and later | [Create a billing preview run](https://www.zuora.com/developer/api-reference/#operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. | | taxationItems | 315.0 and later | [Preview a subscription](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewSubscription \"Preview a subscription\"); [Update a subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update a subscription\")| List of taxation items for an invoice item or a credit memo item. |    #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Billing Object Model  The following diagram is a high-level view of how key business objects are related to one another within Zuora Billing.  Click the diagram to open it in a new tab and zoom in. For more information about the different sections of the diagram, see <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/A_Zuora_Billing_business_object_model\" target=\"_blank\">Zuora Billing business object model</a>.  <a href=\"https://assets.zuora.com/zuora-documentation/Zuora_Billing_object_model_Sep2020.png\" target=\"_blank\"><img src=\"https://assets.zuora.com/zuora-documentation/Zuora_Billing_object_model_Sep2020.png\" alt=\"Zuora Billing object model diagram\"></a>  This diagram is intended to provide a conceptual understanding; it does not illustrate a specific way to integrate with Zuora.  The diagram includes the Orders feature and the Invoice Settlement feature. If your organization does not use either of these features, see <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/B_Zuora_Billing_business_object_model_prior_to_Orders_and_Invoice_Settlement\" target=\"_blank\">Zuora Billing business object model prior to Orders and Invoice Settlement</a> for an alternative diagram.  ## API Names  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun` - API name used  in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query.</p> <p>`BillRun` - API name used in the [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions). See the CRUD oprations of [Bill Run](https://www.zuora.com/developer/api-reference/#tag/Bill-Run) for more information about the `BillRun` object. `BillingRun` and `BillRun` have different fields. |                      | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Notification History - Callout                | `CalloutHistory`                           | | Notification History - Email                  | `EmailHistory`                             | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Line Items                              | `OrderLineItems`                           |     | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    The version of the OpenAPI document: 2022-02-10
    Contact: docs@zuora.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class POSTPaymentMethodRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'baid': 'str',
        'email': 'str',
        'preapproval_key': 'str',
        'card_holder_info': 'CreatePaymentMethodCardholderInfo',
        'card_number': 'str',
        'card_type': 'str',
        'check_duplicated': 'bool',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'mit_consent_agreement_ref': 'str',
        'mit_consent_agreement_src': 'str',
        'mit_network_transaction_id': 'str',
        'mit_profile_action': 'str',
        'mit_profile_agreed_on': 'date',
        'mit_profile_type': 'str',
        'security_code': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'bank_aba_code': 'str',
        'bank_account_name': 'str',
        'bank_account_number': 'str',
        'bank_account_type': 'str',
        'bank_name': 'str',
        'city': 'str',
        'country': 'str',
        'phone': 'str',
        'state': 'str',
        'zip_code': 'str',
        'account_key': 'str',
        'auth_gateway': 'str',
        'gateway_options': 'CreatePaymentMethodCommonGatewayOptions',
        'make_default': 'bool',
        'mandate_info': 'CreatePaymentMethodCommonMandateInfo',
        'skip_validation': 'bool',
        'iban': 'str',
        'account_holder_info': 'CreatePaymentMethodBankTransferAccountHolderInfo',
        'account_number': 'str',
        'bank_code': 'str',
        'branch_code': 'str',
        'business_identification_code': 'str',
        'currency_code': 'str',
        'identity_number': 'str',
        'credit_card_mask_number': 'str',
        'second_token_id': 'str',
        'token_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'baid': 'BAID',
        'email': 'email',
        'preapproval_key': 'preapprovalKey',
        'card_holder_info': 'cardHolderInfo',
        'card_number': 'cardNumber',
        'card_type': 'cardType',
        'check_duplicated': 'checkDuplicated',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'mit_consent_agreement_ref': 'mitConsentAgreementRef',
        'mit_consent_agreement_src': 'mitConsentAgreementSrc',
        'mit_network_transaction_id': 'mitNetworkTransactionId',
        'mit_profile_action': 'mitProfileAction',
        'mit_profile_agreed_on': 'mitProfileAgreedOn',
        'mit_profile_type': 'mitProfileType',
        'security_code': 'securityCode',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'bank_aba_code': 'bankABACode',
        'bank_account_name': 'bankAccountName',
        'bank_account_number': 'bankAccountNumber',
        'bank_account_type': 'bankAccountType',
        'bank_name': 'bankName',
        'city': 'city',
        'country': 'country',
        'phone': 'phone',
        'state': 'state',
        'zip_code': 'zipCode',
        'account_key': 'accountKey',
        'auth_gateway': 'authGateway',
        'gateway_options': 'gatewayOptions',
        'make_default': 'makeDefault',
        'mandate_info': 'mandateInfo',
        'skip_validation': 'skipValidation',
        'iban': 'IBAN',
        'account_holder_info': 'accountHolderInfo',
        'account_number': 'accountNumber',
        'bank_code': 'bankCode',
        'branch_code': 'branchCode',
        'business_identification_code': 'businessIdentificationCode',
        'currency_code': 'currencyCode',
        'identity_number': 'identityNumber',
        'credit_card_mask_number': 'creditCardMaskNumber',
        'second_token_id': 'secondTokenId',
        'token_id': 'tokenId'
    }

    def __init__(self, type=None, baid=None, email=None, preapproval_key=None, card_holder_info=None, card_number=None, card_type=None, check_duplicated=None, expiration_month=None, expiration_year=None, mit_consent_agreement_ref=None, mit_consent_agreement_src=None, mit_network_transaction_id=None, mit_profile_action=None, mit_profile_agreed_on=None, mit_profile_type=None, security_code=None, address_line1=None, address_line2=None, bank_aba_code=None, bank_account_name=None, bank_account_number=None, bank_account_type=None, bank_name=None, city=None, country=None, phone=None, state=None, zip_code=None, account_key=None, auth_gateway=None, gateway_options=None, make_default=False, mandate_info=None, skip_validation=False, iban=None, account_holder_info=None, account_number=None, bank_code=None, branch_code=None, business_identification_code=None, currency_code=None, identity_number=None, credit_card_mask_number=None, second_token_id=None, token_id=None, local_vars_configuration=None):  # noqa: E501
        """POSTPaymentMethodRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._baid = None
        self._email = None
        self._preapproval_key = None
        self._card_holder_info = None
        self._card_number = None
        self._card_type = None
        self._check_duplicated = None
        self._expiration_month = None
        self._expiration_year = None
        self._mit_consent_agreement_ref = None
        self._mit_consent_agreement_src = None
        self._mit_network_transaction_id = None
        self._mit_profile_action = None
        self._mit_profile_agreed_on = None
        self._mit_profile_type = None
        self._security_code = None
        self._address_line1 = None
        self._address_line2 = None
        self._bank_aba_code = None
        self._bank_account_name = None
        self._bank_account_number = None
        self._bank_account_type = None
        self._bank_name = None
        self._city = None
        self._country = None
        self._phone = None
        self._state = None
        self._zip_code = None
        self._account_key = None
        self._auth_gateway = None
        self._gateway_options = None
        self._make_default = None
        self._mandate_info = None
        self._skip_validation = None
        self._iban = None
        self._account_holder_info = None
        self._account_number = None
        self._bank_code = None
        self._branch_code = None
        self._business_identification_code = None
        self._currency_code = None
        self._identity_number = None
        self._credit_card_mask_number = None
        self._second_token_id = None
        self._token_id = None
        self.discriminator = None

        self.type = type
        if baid is not None:
            self.baid = baid
        if email is not None:
            self.email = email
        if preapproval_key is not None:
            self.preapproval_key = preapproval_key
        if card_holder_info is not None:
            self.card_holder_info = card_holder_info
        if card_number is not None:
            self.card_number = card_number
        if card_type is not None:
            self.card_type = card_type
        if check_duplicated is not None:
            self.check_duplicated = check_duplicated
        if expiration_month is not None:
            self.expiration_month = expiration_month
        if expiration_year is not None:
            self.expiration_year = expiration_year
        if mit_consent_agreement_ref is not None:
            self.mit_consent_agreement_ref = mit_consent_agreement_ref
        if mit_consent_agreement_src is not None:
            self.mit_consent_agreement_src = mit_consent_agreement_src
        if mit_network_transaction_id is not None:
            self.mit_network_transaction_id = mit_network_transaction_id
        if mit_profile_action is not None:
            self.mit_profile_action = mit_profile_action
        if mit_profile_agreed_on is not None:
            self.mit_profile_agreed_on = mit_profile_agreed_on
        if mit_profile_type is not None:
            self.mit_profile_type = mit_profile_type
        if security_code is not None:
            self.security_code = security_code
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if bank_aba_code is not None:
            self.bank_aba_code = bank_aba_code
        if bank_account_name is not None:
            self.bank_account_name = bank_account_name
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if bank_account_type is not None:
            self.bank_account_type = bank_account_type
        if bank_name is not None:
            self.bank_name = bank_name
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if state is not None:
            self.state = state
        if zip_code is not None:
            self.zip_code = zip_code
        if account_key is not None:
            self.account_key = account_key
        if auth_gateway is not None:
            self.auth_gateway = auth_gateway
        if gateway_options is not None:
            self.gateway_options = gateway_options
        if make_default is not None:
            self.make_default = make_default
        if mandate_info is not None:
            self.mandate_info = mandate_info
        if skip_validation is not None:
            self.skip_validation = skip_validation
        if iban is not None:
            self.iban = iban
        if account_holder_info is not None:
            self.account_holder_info = account_holder_info
        if account_number is not None:
            self.account_number = account_number
        if bank_code is not None:
            self.bank_code = bank_code
        if branch_code is not None:
            self.branch_code = branch_code
        if business_identification_code is not None:
            self.business_identification_code = business_identification_code
        if currency_code is not None:
            self.currency_code = currency_code
        if identity_number is not None:
            self.identity_number = identity_number
        if credit_card_mask_number is not None:
            self.credit_card_mask_number = credit_card_mask_number
        if second_token_id is not None:
            self.second_token_id = second_token_id
        if token_id is not None:
            self.token_id = token_id

    @property
    def type(self):
        """Gets the type of this POSTPaymentMethodRequest.  # noqa: E501

        Type of the payment method. Possible values include:  * `PayPalEC` - PayPal Express Checkout payment method. Use this type if you are using a [PayPal Payflow Pro Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways/PayPal_Payflow_Pro%2C_Website_Payments_Payflow_Edition%2C_Website_Pro_Payment_Gateway) instance. * `PayPalNativeEC` - PayPal Native Express Checkout payment method. Use this type if you are using a [PayPal Express Checkout Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways/PayPal_Express_Checkout_Gateway) instance. * `PayPalAdaptive` - PayPal Adaptive payment method. Use this type if you are using a [PayPal Adaptive Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways/PayPal_Adaptive_Payments_Gateway) instance. * `CreditCard` - Credit card payment method. * `CreditCardReferenceTransaction` - Credit Card Reference Transaction. See [Supported payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Supported_Payment_Methods) for payment gateways that support this type of payment method. * `ACH` - ACH payment method. * `SEPA` - Single Euro Payments Area. * `Betalingsservice` - Direct Debit DK. * `Autogiro` - Direct Debit SE. * `Bacs` - Direct Debit UK. * `Becs` - Direct Entry AU. * `Becsnz` - Direct Debit NZ. * `PAD` - Pre-Authorized Debit. * `AdyenApplePay` - Apple Pay on Adyen Integration v2.0. This support is only available in the Sandbox environment. See [Set up Adyen Apple Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Apple_Pay_on_Web/Set_up_Adyen_Apple_Pay) for details. * `AdyenGooglePay` - Google Pay on Adyen Integration v2.0. This support is only available in the Sandbox environment. See [Set up Adyen Google Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Set_up_Adyen_Google_Pay) for details. * You can also specify a custom payment method type. This type is only available if the Universal Payment Connector and Open Payment Method services are enabled. See [Set up custom payment gateways and payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) for details.  Note that Zuora is continuously adding new payment method types.   # noqa: E501

        :return: The type of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this POSTPaymentMethodRequest.

        Type of the payment method. Possible values include:  * `PayPalEC` - PayPal Express Checkout payment method. Use this type if you are using a [PayPal Payflow Pro Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways/PayPal_Payflow_Pro%2C_Website_Payments_Payflow_Edition%2C_Website_Pro_Payment_Gateway) instance. * `PayPalNativeEC` - PayPal Native Express Checkout payment method. Use this type if you are using a [PayPal Express Checkout Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways/PayPal_Express_Checkout_Gateway) instance. * `PayPalAdaptive` - PayPal Adaptive payment method. Use this type if you are using a [PayPal Adaptive Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways/PayPal_Adaptive_Payments_Gateway) instance. * `CreditCard` - Credit card payment method. * `CreditCardReferenceTransaction` - Credit Card Reference Transaction. See [Supported payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Supported_Payment_Methods) for payment gateways that support this type of payment method. * `ACH` - ACH payment method. * `SEPA` - Single Euro Payments Area. * `Betalingsservice` - Direct Debit DK. * `Autogiro` - Direct Debit SE. * `Bacs` - Direct Debit UK. * `Becs` - Direct Entry AU. * `Becsnz` - Direct Debit NZ. * `PAD` - Pre-Authorized Debit. * `AdyenApplePay` - Apple Pay on Adyen Integration v2.0. This support is only available in the Sandbox environment. See [Set up Adyen Apple Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Apple_Pay_on_Web/Set_up_Adyen_Apple_Pay) for details. * `AdyenGooglePay` - Google Pay on Adyen Integration v2.0. This support is only available in the Sandbox environment. See [Set up Adyen Google Pay](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/L_Payment_Methods/Payment_Method_Types/Set_up_Adyen_Google_Pay) for details. * You can also specify a custom payment method type. This type is only available if the Universal Payment Connector and Open Payment Method services are enabled. See [Set up custom payment gateways and payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) for details.  Note that Zuora is continuously adding new payment method types.   # noqa: E501

        :param type: The type of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def baid(self):
        """Gets the baid of this POSTPaymentMethodRequest.  # noqa: E501

        ID of a PayPal billing agreement. For example, I-1TJ3GAGG82Y9.   # noqa: E501

        :return: The baid of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._baid

    @baid.setter
    def baid(self, baid):
        """Sets the baid of this POSTPaymentMethodRequest.

        ID of a PayPal billing agreement. For example, I-1TJ3GAGG82Y9.   # noqa: E501

        :param baid: The baid of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._baid = baid

    @property
    def email(self):
        """Gets the email of this POSTPaymentMethodRequest.  # noqa: E501

        Email address associated with the payment method. This field is required if you want to create a PayPal Express Checkout payment method or a PayPal Adaptive payment method.   # noqa: E501

        :return: The email of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this POSTPaymentMethodRequest.

        Email address associated with the payment method. This field is required if you want to create a PayPal Express Checkout payment method or a PayPal Adaptive payment method.   # noqa: E501

        :param email: The email of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def preapproval_key(self):
        """Gets the preapproval_key of this POSTPaymentMethodRequest.  # noqa: E501

        The PayPal preapproval key.   # noqa: E501

        :return: The preapproval_key of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._preapproval_key

    @preapproval_key.setter
    def preapproval_key(self, preapproval_key):
        """Sets the preapproval_key of this POSTPaymentMethodRequest.

        The PayPal preapproval key.   # noqa: E501

        :param preapproval_key: The preapproval_key of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._preapproval_key = preapproval_key

    @property
    def card_holder_info(self):
        """Gets the card_holder_info of this POSTPaymentMethodRequest.  # noqa: E501


        :return: The card_holder_info of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: CreatePaymentMethodCardholderInfo
        """
        return self._card_holder_info

    @card_holder_info.setter
    def card_holder_info(self, card_holder_info):
        """Sets the card_holder_info of this POSTPaymentMethodRequest.


        :param card_holder_info: The card_holder_info of this POSTPaymentMethodRequest.  # noqa: E501
        :type: CreatePaymentMethodCardholderInfo
        """

        self._card_holder_info = card_holder_info

    @property
    def card_number(self):
        """Gets the card_number of this POSTPaymentMethodRequest.  # noqa: E501

        Credit card number.   # noqa: E501

        :return: The card_number of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this POSTPaymentMethodRequest.

        Credit card number.   # noqa: E501

        :param card_number: The card_number of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def card_type(self):
        """Gets the card_type of this POSTPaymentMethodRequest.  # noqa: E501

        The type of the credit card.  Possible values include `Visa`, `MasterCard`, `AmericanExpress`, `Discover`, `JCB`, and `Diners`. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).   # noqa: E501

        :return: The card_type of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this POSTPaymentMethodRequest.

        The type of the credit card.  Possible values include `Visa`, `MasterCard`, `AmericanExpress`, `Discover`, `JCB`, and `Diners`. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).   # noqa: E501

        :param card_type: The card_type of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._card_type = card_type

    @property
    def check_duplicated(self):
        """Gets the check_duplicated of this POSTPaymentMethodRequest.  # noqa: E501

        Indicates whether the duplication check is performed when you create a new credit card payment method. The default value is `false`.  With this field set to `true`, Zuora will check all active payment methods associated with the same billing account to ensure that no duplicate credit card payment methods are created. An error is returned if a duplicate payment method is found.          The following fields are used for the duplication check:   * `cardHolderName`   * `expirationMonth`   * `expirationYear`   * `creditCardMaskNumber`. It is the masked credit card number generated by Zuora. For example:     ```     ************1234     ```   # noqa: E501

        :return: The check_duplicated of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: bool
        """
        return self._check_duplicated

    @check_duplicated.setter
    def check_duplicated(self, check_duplicated):
        """Sets the check_duplicated of this POSTPaymentMethodRequest.

        Indicates whether the duplication check is performed when you create a new credit card payment method. The default value is `false`.  With this field set to `true`, Zuora will check all active payment methods associated with the same billing account to ensure that no duplicate credit card payment methods are created. An error is returned if a duplicate payment method is found.          The following fields are used for the duplication check:   * `cardHolderName`   * `expirationMonth`   * `expirationYear`   * `creditCardMaskNumber`. It is the masked credit card number generated by Zuora. For example:     ```     ************1234     ```   # noqa: E501

        :param check_duplicated: The check_duplicated of this POSTPaymentMethodRequest.  # noqa: E501
        :type: bool
        """

        self._check_duplicated = check_duplicated

    @property
    def expiration_month(self):
        """Gets the expiration_month of this POSTPaymentMethodRequest.  # noqa: E501

        One or two digit expiration month (1-12) of the credit card.   # noqa: E501

        :return: The expiration_month of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this POSTPaymentMethodRequest.

        One or two digit expiration month (1-12) of the credit card.   # noqa: E501

        :param expiration_month: The expiration_month of this POSTPaymentMethodRequest.  # noqa: E501
        :type: int
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this POSTPaymentMethodRequest.  # noqa: E501

        Four-digit expiration year of the credit card.   # noqa: E501

        :return: The expiration_year of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this POSTPaymentMethodRequest.

        Four-digit expiration year of the credit card.   # noqa: E501

        :param expiration_year: The expiration_year of this POSTPaymentMethodRequest.  # noqa: E501
        :type: int
        """

        self._expiration_year = expiration_year

    @property
    def mit_consent_agreement_ref(self):
        """Gets the mit_consent_agreement_ref of this POSTPaymentMethodRequest.  # noqa: E501

        Specifies your reference for the stored credential consent agreement that you have established with the customer. Only applicable if you set the `mitProfileAction` field.   # noqa: E501

        :return: The mit_consent_agreement_ref of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._mit_consent_agreement_ref

    @mit_consent_agreement_ref.setter
    def mit_consent_agreement_ref(self, mit_consent_agreement_ref):
        """Sets the mit_consent_agreement_ref of this POSTPaymentMethodRequest.

        Specifies your reference for the stored credential consent agreement that you have established with the customer. Only applicable if you set the `mitProfileAction` field.   # noqa: E501

        :param mit_consent_agreement_ref: The mit_consent_agreement_ref of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mit_consent_agreement_ref is not None and len(mit_consent_agreement_ref) > 128):
            raise ValueError("Invalid value for `mit_consent_agreement_ref`, length must be less than or equal to `128`")  # noqa: E501

        self._mit_consent_agreement_ref = mit_consent_agreement_ref

    @property
    def mit_consent_agreement_src(self):
        """Gets the mit_consent_agreement_src of this POSTPaymentMethodRequest.  # noqa: E501

        Required if you set the `mitProfileAction` field.   # noqa: E501

        :return: The mit_consent_agreement_src of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._mit_consent_agreement_src

    @mit_consent_agreement_src.setter
    def mit_consent_agreement_src(self, mit_consent_agreement_src):
        """Sets the mit_consent_agreement_src of this POSTPaymentMethodRequest.

        Required if you set the `mitProfileAction` field.   # noqa: E501

        :param mit_consent_agreement_src: The mit_consent_agreement_src of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["External"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mit_consent_agreement_src not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mit_consent_agreement_src` ({0}), must be one of {1}"  # noqa: E501
                .format(mit_consent_agreement_src, allowed_values)
            )

        self._mit_consent_agreement_src = mit_consent_agreement_src

    @property
    def mit_network_transaction_id(self):
        """Gets the mit_network_transaction_id of this POSTPaymentMethodRequest.  # noqa: E501

        Specifies the ID of a network transaction. Only applicable if you set the `mitProfileAction` field to `Persist`.   # noqa: E501

        :return: The mit_network_transaction_id of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._mit_network_transaction_id

    @mit_network_transaction_id.setter
    def mit_network_transaction_id(self, mit_network_transaction_id):
        """Sets the mit_network_transaction_id of this POSTPaymentMethodRequest.

        Specifies the ID of a network transaction. Only applicable if you set the `mitProfileAction` field to `Persist`.   # noqa: E501

        :param mit_network_transaction_id: The mit_network_transaction_id of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mit_network_transaction_id is not None and len(mit_network_transaction_id) > 128):
            raise ValueError("Invalid value for `mit_network_transaction_id`, length must be less than or equal to `128`")  # noqa: E501

        self._mit_network_transaction_id = mit_network_transaction_id

    @property
    def mit_profile_action(self):
        """Gets the mit_profile_action of this POSTPaymentMethodRequest.  # noqa: E501

        If you set this field, Zuora creates a stored credential profile within the payment method.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.  * `Activate` - Use this value if you are creating the stored credential profile after receiving the customer's consent.    Zuora will create the stored credential profile then send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile. If the CIT succeeds, the status of the stored credential profile will be `Active`. If the CIT does not succeed, Zuora will not create a stored credential profile.      If the payment gateway does not support the stored credential transaction framework, the status of the stored credential profile will be `Agreed`.   * `Persist` - Use this value if the stored credential profile represents a stored credential profile in an external system. The status of the payment method's stored credential profile will be `Active`.   # noqa: E501

        :return: The mit_profile_action of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._mit_profile_action

    @mit_profile_action.setter
    def mit_profile_action(self, mit_profile_action):
        """Sets the mit_profile_action of this POSTPaymentMethodRequest.

        If you set this field, Zuora creates a stored credential profile within the payment method.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.  * `Activate` - Use this value if you are creating the stored credential profile after receiving the customer's consent.    Zuora will create the stored credential profile then send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile. If the CIT succeeds, the status of the stored credential profile will be `Active`. If the CIT does not succeed, Zuora will not create a stored credential profile.      If the payment gateway does not support the stored credential transaction framework, the status of the stored credential profile will be `Agreed`.   * `Persist` - Use this value if the stored credential profile represents a stored credential profile in an external system. The status of the payment method's stored credential profile will be `Active`.   # noqa: E501

        :param mit_profile_action: The mit_profile_action of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Activate", "Persist"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mit_profile_action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mit_profile_action` ({0}), must be one of {1}"  # noqa: E501
                .format(mit_profile_action, allowed_values)
            )

        self._mit_profile_action = mit_profile_action

    @property
    def mit_profile_agreed_on(self):
        """Gets the mit_profile_agreed_on of this POSTPaymentMethodRequest.  # noqa: E501

        The date on which the profile is agreed. The date format is `yyyy-mm-dd`.   # noqa: E501

        :return: The mit_profile_agreed_on of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: date
        """
        return self._mit_profile_agreed_on

    @mit_profile_agreed_on.setter
    def mit_profile_agreed_on(self, mit_profile_agreed_on):
        """Sets the mit_profile_agreed_on of this POSTPaymentMethodRequest.

        The date on which the profile is agreed. The date format is `yyyy-mm-dd`.   # noqa: E501

        :param mit_profile_agreed_on: The mit_profile_agreed_on of this POSTPaymentMethodRequest.  # noqa: E501
        :type: date
        """

        self._mit_profile_agreed_on = mit_profile_agreed_on

    @property
    def mit_profile_type(self):
        """Gets the mit_profile_type of this POSTPaymentMethodRequest.  # noqa: E501

        Required if you set the `mitProfileAction` field. Indicates the type of the stored credential profile to process recurring or unsecheduled transactions.   # noqa: E501

        :return: The mit_profile_type of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._mit_profile_type

    @mit_profile_type.setter
    def mit_profile_type(self, mit_profile_type):
        """Sets the mit_profile_type of this POSTPaymentMethodRequest.

        Required if you set the `mitProfileAction` field. Indicates the type of the stored credential profile to process recurring or unsecheduled transactions.   # noqa: E501

        :param mit_profile_type: The mit_profile_type of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Recurring", "Unscheduled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mit_profile_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mit_profile_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mit_profile_type, allowed_values)
            )

        self._mit_profile_type = mit_profile_type

    @property
    def security_code(self):
        """Gets the security_code of this POSTPaymentMethodRequest.  # noqa: E501

        CVV or CVV2 security code of the credit card.  To ensure PCI compliance, this value is not stored and cannot be queried.   # noqa: E501

        :return: The security_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this POSTPaymentMethodRequest.

        CVV or CVV2 security code of the credit card.  To ensure PCI compliance, this value is not stored and cannot be queried.   # noqa: E501

        :param security_code: The security_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

    @property
    def address_line1(self):
        """Gets the address_line1 of this POSTPaymentMethodRequest.  # noqa: E501

        First address line, 255 characters or less.   # noqa: E501

        :return: The address_line1 of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this POSTPaymentMethodRequest.

        First address line, 255 characters or less.   # noqa: E501

        :param address_line1: The address_line1 of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this POSTPaymentMethodRequest.  # noqa: E501

        Second address line, 255 characters or less.   # noqa: E501

        :return: The address_line2 of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this POSTPaymentMethodRequest.

        Second address line, 255 characters or less.   # noqa: E501

        :param address_line2: The address_line2 of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def bank_aba_code(self):
        """Gets the bank_aba_code of this POSTPaymentMethodRequest.  # noqa: E501

        The nine-digit routing number or ABA number used by banks. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :return: The bank_aba_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_aba_code

    @bank_aba_code.setter
    def bank_aba_code(self, bank_aba_code):
        """Sets the bank_aba_code of this POSTPaymentMethodRequest.

        The nine-digit routing number or ABA number used by banks. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :param bank_aba_code: The bank_aba_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._bank_aba_code = bank_aba_code

    @property
    def bank_account_name(self):
        """Gets the bank_account_name of this POSTPaymentMethodRequest.  # noqa: E501

        The name of the account holder, which can be either a person or a company. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :return: The bank_account_name of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, bank_account_name):
        """Sets the bank_account_name of this POSTPaymentMethodRequest.

        The name of the account holder, which can be either a person or a company. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :param bank_account_name: The bank_account_name of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                bank_account_name is not None and len(bank_account_name) > 70):
            raise ValueError("Invalid value for `bank_account_name`, length must be less than or equal to `70`")  # noqa: E501

        self._bank_account_name = bank_account_name

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this POSTPaymentMethodRequest.  # noqa: E501

        The bank account number associated with the ACH payment. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :return: The bank_account_number of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this POSTPaymentMethodRequest.

        The bank account number associated with the ACH payment. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :param bank_account_number: The bank_account_number of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                bank_account_number is not None and len(bank_account_number) > 30):
            raise ValueError("Invalid value for `bank_account_number`, length must be less than or equal to `30`")  # noqa: E501

        self._bank_account_number = bank_account_number

    @property
    def bank_account_type(self):
        """Gets the bank_account_type of this POSTPaymentMethodRequest.  # noqa: E501

        The type of bank account associated with the ACH payment. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :return: The bank_account_type of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_type

    @bank_account_type.setter
    def bank_account_type(self, bank_account_type):
        """Sets the bank_account_type of this POSTPaymentMethodRequest.

        The type of bank account associated with the ACH payment. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :param bank_account_type: The bank_account_type of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BusinessChecking", "Checking", "Saving"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bank_account_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bank_account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bank_account_type, allowed_values)
            )

        self._bank_account_type = bank_account_type

    @property
    def bank_name(self):
        """Gets the bank_name of this POSTPaymentMethodRequest.  # noqa: E501

        The name of the bank where the ACH payment account is held. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :return: The bank_name of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this POSTPaymentMethodRequest.

        The name of the bank where the ACH payment account is held. This field is only required if the `type` field is set to `ACH`.   # noqa: E501

        :param bank_name: The bank_name of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                bank_name is not None and len(bank_name) > 70):
            raise ValueError("Invalid value for `bank_name`, length must be less than or equal to `70`")  # noqa: E501

        self._bank_name = bank_name

    @property
    def city(self):
        """Gets the city of this POSTPaymentMethodRequest.  # noqa: E501

        City, 40 characters or less.        # noqa: E501

        :return: The city of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this POSTPaymentMethodRequest.

        City, 40 characters or less.        # noqa: E501

        :param city: The city of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this POSTPaymentMethodRequest.  # noqa: E501

        Country, must be a valid country name or abbreviation.   # noqa: E501

        :return: The country of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this POSTPaymentMethodRequest.

        Country, must be a valid country name or abbreviation.   # noqa: E501

        :param country: The country of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this POSTPaymentMethodRequest.  # noqa: E501

        Phone number, 40 characters or less.   # noqa: E501

        :return: The phone of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this POSTPaymentMethodRequest.

        Phone number, 40 characters or less.   # noqa: E501

        :param phone: The phone of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """Gets the state of this POSTPaymentMethodRequest.  # noqa: E501

        State, must be a valid state name or 2-character abbreviation.   # noqa: E501

        :return: The state of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this POSTPaymentMethodRequest.

        State, must be a valid state name or 2-character abbreviation.   # noqa: E501

        :param state: The state of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this POSTPaymentMethodRequest.  # noqa: E501

        Zip code, 20 characters or less.   # noqa: E501

        :return: The zip_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this POSTPaymentMethodRequest.

        Zip code, 20 characters or less.   # noqa: E501

        :param zip_code: The zip_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def account_key(self):
        """Gets the account_key of this POSTPaymentMethodRequest.  # noqa: E501

        Internal ID of the customer account that will own the payment method.   To create an orphan payment method that is not associated with any customer account, you do not need to specify this field during creation. However, you must associate the orphan payment method with a customer account within 10 days. Otherwise, this orphan payment method will be deleted.   # noqa: E501

        :return: The account_key of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this POSTPaymentMethodRequest.

        Internal ID of the customer account that will own the payment method.   To create an orphan payment method that is not associated with any customer account, you do not need to specify this field during creation. However, you must associate the orphan payment method with a customer account within 10 days. Otherwise, this orphan payment method will be deleted.   # noqa: E501

        :param account_key: The account_key of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._account_key = account_key

    @property
    def auth_gateway(self):
        """Gets the auth_gateway of this POSTPaymentMethodRequest.  # noqa: E501

        Internal ID of the payment gateway that Zuora will use to authorize the payments that are made with the payment method.  If you do not set this field, Zuora will use one of the following payment gateways instead:  * The default payment gateway of the customer account that owns the payment method, if the `accountKey` field is set. * The default payment gateway of your Zuora tenant, if the `accountKey` field is not set.   # noqa: E501

        :return: The auth_gateway of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_gateway

    @auth_gateway.setter
    def auth_gateway(self, auth_gateway):
        """Sets the auth_gateway of this POSTPaymentMethodRequest.

        Internal ID of the payment gateway that Zuora will use to authorize the payments that are made with the payment method.  If you do not set this field, Zuora will use one of the following payment gateways instead:  * The default payment gateway of the customer account that owns the payment method, if the `accountKey` field is set. * The default payment gateway of your Zuora tenant, if the `accountKey` field is not set.   # noqa: E501

        :param auth_gateway: The auth_gateway of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._auth_gateway = auth_gateway

    @property
    def gateway_options(self):
        """Gets the gateway_options of this POSTPaymentMethodRequest.  # noqa: E501


        :return: The gateway_options of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: CreatePaymentMethodCommonGatewayOptions
        """
        return self._gateway_options

    @gateway_options.setter
    def gateway_options(self, gateway_options):
        """Sets the gateway_options of this POSTPaymentMethodRequest.


        :param gateway_options: The gateway_options of this POSTPaymentMethodRequest.  # noqa: E501
        :type: CreatePaymentMethodCommonGatewayOptions
        """

        self._gateway_options = gateway_options

    @property
    def make_default(self):
        """Gets the make_default of this POSTPaymentMethodRequest.  # noqa: E501

        Specifies whether the payment method will be the default payment method of the customer account that owns the payment method. Only applicable if the `accountKey` field is set.   # noqa: E501

        :return: The make_default of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: bool
        """
        return self._make_default

    @make_default.setter
    def make_default(self, make_default):
        """Sets the make_default of this POSTPaymentMethodRequest.

        Specifies whether the payment method will be the default payment method of the customer account that owns the payment method. Only applicable if the `accountKey` field is set.   # noqa: E501

        :param make_default: The make_default of this POSTPaymentMethodRequest.  # noqa: E501
        :type: bool
        """

        self._make_default = make_default

    @property
    def mandate_info(self):
        """Gets the mandate_info of this POSTPaymentMethodRequest.  # noqa: E501


        :return: The mandate_info of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: CreatePaymentMethodCommonMandateInfo
        """
        return self._mandate_info

    @mandate_info.setter
    def mandate_info(self, mandate_info):
        """Sets the mandate_info of this POSTPaymentMethodRequest.


        :param mandate_info: The mandate_info of this POSTPaymentMethodRequest.  # noqa: E501
        :type: CreatePaymentMethodCommonMandateInfo
        """

        self._mandate_info = mandate_info

    @property
    def skip_validation(self):
        """Gets the skip_validation of this POSTPaymentMethodRequest.  # noqa: E501

        Specify whether to skip the validation of the information through the payment gateway. For example, when migrating your payment methods, you can set this field to `true` to skip the validation.    # noqa: E501

        :return: The skip_validation of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_validation

    @skip_validation.setter
    def skip_validation(self, skip_validation):
        """Sets the skip_validation of this POSTPaymentMethodRequest.

        Specify whether to skip the validation of the information through the payment gateway. For example, when migrating your payment methods, you can set this field to `true` to skip the validation.    # noqa: E501

        :param skip_validation: The skip_validation of this POSTPaymentMethodRequest.  # noqa: E501
        :type: bool
        """

        self._skip_validation = skip_validation

    @property
    def iban(self):
        """Gets the iban of this POSTPaymentMethodRequest.  # noqa: E501

        The International Bank Account Number. This field is used to create the SEPA payment method.   # noqa: E501

        :return: The iban of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this POSTPaymentMethodRequest.

        The International Bank Account Number. This field is used to create the SEPA payment method.   # noqa: E501

        :param iban: The iban of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def account_holder_info(self):
        """Gets the account_holder_info of this POSTPaymentMethodRequest.  # noqa: E501


        :return: The account_holder_info of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: CreatePaymentMethodBankTransferAccountHolderInfo
        """
        return self._account_holder_info

    @account_holder_info.setter
    def account_holder_info(self, account_holder_info):
        """Sets the account_holder_info of this POSTPaymentMethodRequest.


        :param account_holder_info: The account_holder_info of this POSTPaymentMethodRequest.  # noqa: E501
        :type: CreatePaymentMethodBankTransferAccountHolderInfo
        """

        self._account_holder_info = account_holder_info

    @property
    def account_number(self):
        """Gets the account_number of this POSTPaymentMethodRequest.  # noqa: E501

        The number of the customer's bank account. Use this field for direct debit payment methods.   # noqa: E501

        :return: The account_number of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this POSTPaymentMethodRequest.

        The number of the customer's bank account. Use this field for direct debit payment methods.   # noqa: E501

        :param account_number: The account_number of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def bank_code(self):
        """Gets the bank_code of this POSTPaymentMethodRequest.  # noqa: E501

        The sort code or number that identifies the bank. This is also known as the sort code.    # noqa: E501

        :return: The bank_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this POSTPaymentMethodRequest.

        The sort code or number that identifies the bank. This is also known as the sort code.    # noqa: E501

        :param bank_code: The bank_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def branch_code(self):
        """Gets the branch_code of this POSTPaymentMethodRequest.  # noqa: E501

        The branch code of the bank used for direct debit.     # noqa: E501

        :return: The branch_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this POSTPaymentMethodRequest.

        The branch code of the bank used for direct debit.     # noqa: E501

        :param branch_code: The branch_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._branch_code = branch_code

    @property
    def business_identification_code(self):
        """Gets the business_identification_code of this POSTPaymentMethodRequest.  # noqa: E501

        The BIC code used for SEPA.   # noqa: E501

        :return: The business_identification_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._business_identification_code

    @business_identification_code.setter
    def business_identification_code(self, business_identification_code):
        """Sets the business_identification_code of this POSTPaymentMethodRequest.

        The BIC code used for SEPA.   # noqa: E501

        :param business_identification_code: The business_identification_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._business_identification_code = business_identification_code

    @property
    def currency_code(self):
        """Gets the currency_code of this POSTPaymentMethodRequest.  # noqa: E501

        The currency used for payment method authorization.  If this field is not specified, `currency` specified for the account is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.   # noqa: E501

        :return: The currency_code of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this POSTPaymentMethodRequest.

        The currency used for payment method authorization.  If this field is not specified, `currency` specified for the account is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.   # noqa: E501

        :param currency_code: The currency_code of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def identity_number(self):
        """Gets the identity_number of this POSTPaymentMethodRequest.  # noqa: E501

        The identity number used for Bank Transfer.   # noqa: E501

        :return: The identity_number of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._identity_number

    @identity_number.setter
    def identity_number(self, identity_number):
        """Sets the identity_number of this POSTPaymentMethodRequest.

        The identity number used for Bank Transfer.   # noqa: E501

        :param identity_number: The identity_number of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._identity_number = identity_number

    @property
    def credit_card_mask_number(self):
        """Gets the credit_card_mask_number of this POSTPaymentMethodRequest.  # noqa: E501

        The masked credit card number, such as: ``` *********1112 ```  This field is specific for the CC Reference Transaction payment method. It is an optional field that you can use to distinguish different CC Reference Transaction payment methods.  Though there are no special restrictions on the input string, it is highly recommended to specify a card number that is masked.   # noqa: E501

        :return: The credit_card_mask_number of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_mask_number

    @credit_card_mask_number.setter
    def credit_card_mask_number(self, credit_card_mask_number):
        """Sets the credit_card_mask_number of this POSTPaymentMethodRequest.

        The masked credit card number, such as: ``` *********1112 ```  This field is specific for the CC Reference Transaction payment method. It is an optional field that you can use to distinguish different CC Reference Transaction payment methods.  Though there are no special restrictions on the input string, it is highly recommended to specify a card number that is masked.   # noqa: E501

        :param credit_card_mask_number: The credit_card_mask_number of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                credit_card_mask_number is not None and len(credit_card_mask_number) > 19):
            raise ValueError("Invalid value for `credit_card_mask_number`, length must be less than or equal to `19`")  # noqa: E501

        self._credit_card_mask_number = credit_card_mask_number

    @property
    def second_token_id(self):
        """Gets the second_token_id of this POSTPaymentMethodRequest.  # noqa: E501

        A gateway unique identifier that replaces sensitive payment method data.   `secondTokenId` is conditionally required only when `tokenId` is being used to represent a gateway customer profile. `secondTokenId` is used in the CC Reference Transaction payment method.   # noqa: E501

        :return: The second_token_id of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._second_token_id

    @second_token_id.setter
    def second_token_id(self, second_token_id):
        """Sets the second_token_id of this POSTPaymentMethodRequest.

        A gateway unique identifier that replaces sensitive payment method data.   `secondTokenId` is conditionally required only when `tokenId` is being used to represent a gateway customer profile. `secondTokenId` is used in the CC Reference Transaction payment method.   # noqa: E501

        :param second_token_id: The second_token_id of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._second_token_id = second_token_id

    @property
    def token_id(self):
        """Gets the token_id of this POSTPaymentMethodRequest.  # noqa: E501

        A gateway unique identifier that replaces sensitive payment method data or represents a gateway's unique customer profile. `tokenId` is required for the CC Reference Transaction payment method.  When `tokenId` is used to represent a customer profile, `secondTokenId` is conditionally required for representing the underlying tokenized payment method.  When creating an ACH payment method, if you need to pass in tokenized information, use the `mandateId` instead of `tokenId` field.   # noqa: E501

        :return: The token_id of this POSTPaymentMethodRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this POSTPaymentMethodRequest.

        A gateway unique identifier that replaces sensitive payment method data or represents a gateway's unique customer profile. `tokenId` is required for the CC Reference Transaction payment method.  When `tokenId` is used to represent a customer profile, `secondTokenId` is conditionally required for representing the underlying tokenized payment method.  When creating an ACH payment method, if you need to pass in tokenized information, use the `mandateId` instead of `tokenId` field.   # noqa: E501

        :param token_id: The token_id of this POSTPaymentMethodRequest.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, POSTPaymentMethodRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, POSTPaymentMethodRequest):
            return True

        return self.to_dict() != other.to_dict()
