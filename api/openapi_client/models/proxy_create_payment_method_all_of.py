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


class ProxyCreatePaymentMethodAllOf(object):
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
        'account_id': 'str',
        'ach_aba_code': 'str',
        'ach_account_name': 'str',
        'ach_account_number': 'str',
        'ach_account_type': 'str',
        'ach_address1': 'str',
        'ach_address2': 'str',
        'ach_bank_name': 'str',
        'ach_city': 'str',
        'ach_country': 'str',
        'ach_postal_code': 'str',
        'ach_state': 'str',
        'bank_branch_code': 'str',
        'bank_check_digit': 'str',
        'bank_transfer_account_name': 'str',
        'bank_transfer_account_number': 'str',
        'bank_transfer_account_number_mask': 'str',
        'bank_transfer_type': 'str',
        'business_identification_code': 'str',
        'city': 'str',
        'company_name': 'str',
        'country': 'str',
        'credit_card_address1': 'str',
        'credit_card_address2': 'str',
        'credit_card_city': 'str',
        'credit_card_country': 'str',
        'credit_card_expiration_month': 'int',
        'credit_card_expiration_year': 'int',
        'credit_card_holder_name': 'str',
        'credit_card_number': 'str',
        'credit_card_postal_code': 'str',
        'credit_card_security_code': 'str',
        'credit_card_state': 'str',
        'credit_card_type': 'str',
        'device_session_id': 'str',
        'email': 'str',
        'existing_mandate': 'str',
        'first_name': 'str',
        'gateway_option_data': 'ProxyCreatePaymentAllOfGatewayOptionData',
        'iban': 'str',
        'ip_address': 'str',
        'identity_number': 'str',
        'is_company': 'bool',
        'last_name': 'str',
        'last_transaction_date_time': 'datetime',
        'mandate_creation_date': 'date',
        'mandate_id': 'str',
        'mandate_received': 'str',
        'mandate_update_date': 'date',
        'max_consecutive_payment_failures': 'int',
        'num_consecutive_failures': 'int',
        'payment_retry_window': 'int',
        'paypal_baid': 'str',
        'paypal_email': 'str',
        'paypal_preapproval_key': 'str',
        'paypal_type': 'str',
        'phone': 'str',
        'postal_code': 'str',
        'second_token_id': 'str',
        'skip_validation': 'bool',
        'state': 'str',
        'street_name': 'str',
        'street_number': 'str',
        'token_id': 'str',
        'type': 'str',
        'use_default_retry_rule': 'bool',
        'currency_code': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'ach_aba_code': 'AchAbaCode',
        'ach_account_name': 'AchAccountName',
        'ach_account_number': 'AchAccountNumber',
        'ach_account_type': 'AchAccountType',
        'ach_address1': 'AchAddress1',
        'ach_address2': 'AchAddress2',
        'ach_bank_name': 'AchBankName',
        'ach_city': 'AchCity',
        'ach_country': 'AchCountry',
        'ach_postal_code': 'AchPostalCode',
        'ach_state': 'AchState',
        'bank_branch_code': 'BankBranchCode',
        'bank_check_digit': 'BankCheckDigit',
        'bank_transfer_account_name': 'BankTransferAccountName',
        'bank_transfer_account_number': 'BankTransferAccountNumber',
        'bank_transfer_account_number_mask': 'BankTransferAccountNumberMask',
        'bank_transfer_type': 'BankTransferType',
        'business_identification_code': 'BusinessIdentificationCode',
        'city': 'City',
        'company_name': 'CompanyName',
        'country': 'Country',
        'credit_card_address1': 'CreditCardAddress1',
        'credit_card_address2': 'CreditCardAddress2',
        'credit_card_city': 'CreditCardCity',
        'credit_card_country': 'CreditCardCountry',
        'credit_card_expiration_month': 'CreditCardExpirationMonth',
        'credit_card_expiration_year': 'CreditCardExpirationYear',
        'credit_card_holder_name': 'CreditCardHolderName',
        'credit_card_number': 'CreditCardNumber',
        'credit_card_postal_code': 'CreditCardPostalCode',
        'credit_card_security_code': 'CreditCardSecurityCode',
        'credit_card_state': 'CreditCardState',
        'credit_card_type': 'CreditCardType',
        'device_session_id': 'DeviceSessionId',
        'email': 'Email',
        'existing_mandate': 'ExistingMandate',
        'first_name': 'FirstName',
        'gateway_option_data': 'GatewayOptionData',
        'iban': 'IBAN',
        'ip_address': 'IPAddress',
        'identity_number': 'IdentityNumber',
        'is_company': 'IsCompany',
        'last_name': 'LastName',
        'last_transaction_date_time': 'LastTransactionDateTime',
        'mandate_creation_date': 'MandateCreationDate',
        'mandate_id': 'MandateID',
        'mandate_received': 'MandateReceived',
        'mandate_update_date': 'MandateUpdateDate',
        'max_consecutive_payment_failures': 'MaxConsecutivePaymentFailures',
        'num_consecutive_failures': 'NumConsecutiveFailures',
        'payment_retry_window': 'PaymentRetryWindow',
        'paypal_baid': 'PaypalBaid',
        'paypal_email': 'PaypalEmail',
        'paypal_preapproval_key': 'PaypalPreapprovalKey',
        'paypal_type': 'PaypalType',
        'phone': 'Phone',
        'postal_code': 'PostalCode',
        'second_token_id': 'SecondTokenId',
        'skip_validation': 'SkipValidation',
        'state': 'State',
        'street_name': 'StreetName',
        'street_number': 'StreetNumber',
        'token_id': 'TokenId',
        'type': 'Type',
        'use_default_retry_rule': 'UseDefaultRetryRule',
        'currency_code': 'currencyCode'
    }

    def __init__(self, account_id=None, ach_aba_code=None, ach_account_name=None, ach_account_number=None, ach_account_type=None, ach_address1=None, ach_address2=None, ach_bank_name=None, ach_city=None, ach_country=None, ach_postal_code=None, ach_state=None, bank_branch_code=None, bank_check_digit=None, bank_transfer_account_name=None, bank_transfer_account_number=None, bank_transfer_account_number_mask=None, bank_transfer_type=None, business_identification_code=None, city=None, company_name=None, country=None, credit_card_address1=None, credit_card_address2=None, credit_card_city=None, credit_card_country=None, credit_card_expiration_month=None, credit_card_expiration_year=None, credit_card_holder_name=None, credit_card_number=None, credit_card_postal_code=None, credit_card_security_code=None, credit_card_state=None, credit_card_type=None, device_session_id=None, email=None, existing_mandate=None, first_name=None, gateway_option_data=None, iban=None, ip_address=None, identity_number=None, is_company=False, last_name=None, last_transaction_date_time=None, mandate_creation_date=None, mandate_id=None, mandate_received=None, mandate_update_date=None, max_consecutive_payment_failures=None, num_consecutive_failures=None, payment_retry_window=None, paypal_baid=None, paypal_email=None, paypal_preapproval_key=None, paypal_type=None, phone=None, postal_code=None, second_token_id=None, skip_validation=None, state=None, street_name=None, street_number=None, token_id=None, type=None, use_default_retry_rule=None, currency_code=None, local_vars_configuration=None):  # noqa: E501
        """ProxyCreatePaymentMethodAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._ach_aba_code = None
        self._ach_account_name = None
        self._ach_account_number = None
        self._ach_account_type = None
        self._ach_address1 = None
        self._ach_address2 = None
        self._ach_bank_name = None
        self._ach_city = None
        self._ach_country = None
        self._ach_postal_code = None
        self._ach_state = None
        self._bank_branch_code = None
        self._bank_check_digit = None
        self._bank_transfer_account_name = None
        self._bank_transfer_account_number = None
        self._bank_transfer_account_number_mask = None
        self._bank_transfer_type = None
        self._business_identification_code = None
        self._city = None
        self._company_name = None
        self._country = None
        self._credit_card_address1 = None
        self._credit_card_address2 = None
        self._credit_card_city = None
        self._credit_card_country = None
        self._credit_card_expiration_month = None
        self._credit_card_expiration_year = None
        self._credit_card_holder_name = None
        self._credit_card_number = None
        self._credit_card_postal_code = None
        self._credit_card_security_code = None
        self._credit_card_state = None
        self._credit_card_type = None
        self._device_session_id = None
        self._email = None
        self._existing_mandate = None
        self._first_name = None
        self._gateway_option_data = None
        self._iban = None
        self._ip_address = None
        self._identity_number = None
        self._is_company = None
        self._last_name = None
        self._last_transaction_date_time = None
        self._mandate_creation_date = None
        self._mandate_id = None
        self._mandate_received = None
        self._mandate_update_date = None
        self._max_consecutive_payment_failures = None
        self._num_consecutive_failures = None
        self._payment_retry_window = None
        self._paypal_baid = None
        self._paypal_email = None
        self._paypal_preapproval_key = None
        self._paypal_type = None
        self._phone = None
        self._postal_code = None
        self._second_token_id = None
        self._skip_validation = None
        self._state = None
        self._street_name = None
        self._street_number = None
        self._token_id = None
        self._type = None
        self._use_default_retry_rule = None
        self._currency_code = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if ach_aba_code is not None:
            self.ach_aba_code = ach_aba_code
        if ach_account_name is not None:
            self.ach_account_name = ach_account_name
        if ach_account_number is not None:
            self.ach_account_number = ach_account_number
        if ach_account_type is not None:
            self.ach_account_type = ach_account_type
        if ach_address1 is not None:
            self.ach_address1 = ach_address1
        if ach_address2 is not None:
            self.ach_address2 = ach_address2
        if ach_bank_name is not None:
            self.ach_bank_name = ach_bank_name
        if ach_city is not None:
            self.ach_city = ach_city
        if ach_country is not None:
            self.ach_country = ach_country
        if ach_postal_code is not None:
            self.ach_postal_code = ach_postal_code
        if ach_state is not None:
            self.ach_state = ach_state
        if bank_branch_code is not None:
            self.bank_branch_code = bank_branch_code
        if bank_check_digit is not None:
            self.bank_check_digit = bank_check_digit
        if bank_transfer_account_name is not None:
            self.bank_transfer_account_name = bank_transfer_account_name
        if bank_transfer_account_number is not None:
            self.bank_transfer_account_number = bank_transfer_account_number
        if bank_transfer_account_number_mask is not None:
            self.bank_transfer_account_number_mask = bank_transfer_account_number_mask
        if bank_transfer_type is not None:
            self.bank_transfer_type = bank_transfer_type
        if business_identification_code is not None:
            self.business_identification_code = business_identification_code
        if city is not None:
            self.city = city
        if company_name is not None:
            self.company_name = company_name
        if country is not None:
            self.country = country
        if credit_card_address1 is not None:
            self.credit_card_address1 = credit_card_address1
        if credit_card_address2 is not None:
            self.credit_card_address2 = credit_card_address2
        if credit_card_city is not None:
            self.credit_card_city = credit_card_city
        if credit_card_country is not None:
            self.credit_card_country = credit_card_country
        if credit_card_expiration_month is not None:
            self.credit_card_expiration_month = credit_card_expiration_month
        if credit_card_expiration_year is not None:
            self.credit_card_expiration_year = credit_card_expiration_year
        if credit_card_holder_name is not None:
            self.credit_card_holder_name = credit_card_holder_name
        if credit_card_number is not None:
            self.credit_card_number = credit_card_number
        if credit_card_postal_code is not None:
            self.credit_card_postal_code = credit_card_postal_code
        if credit_card_security_code is not None:
            self.credit_card_security_code = credit_card_security_code
        if credit_card_state is not None:
            self.credit_card_state = credit_card_state
        if credit_card_type is not None:
            self.credit_card_type = credit_card_type
        if device_session_id is not None:
            self.device_session_id = device_session_id
        if email is not None:
            self.email = email
        if existing_mandate is not None:
            self.existing_mandate = existing_mandate
        if first_name is not None:
            self.first_name = first_name
        if gateway_option_data is not None:
            self.gateway_option_data = gateway_option_data
        if iban is not None:
            self.iban = iban
        if ip_address is not None:
            self.ip_address = ip_address
        if identity_number is not None:
            self.identity_number = identity_number
        if is_company is not None:
            self.is_company = is_company
        if last_name is not None:
            self.last_name = last_name
        if last_transaction_date_time is not None:
            self.last_transaction_date_time = last_transaction_date_time
        if mandate_creation_date is not None:
            self.mandate_creation_date = mandate_creation_date
        if mandate_id is not None:
            self.mandate_id = mandate_id
        if mandate_received is not None:
            self.mandate_received = mandate_received
        if mandate_update_date is not None:
            self.mandate_update_date = mandate_update_date
        if max_consecutive_payment_failures is not None:
            self.max_consecutive_payment_failures = max_consecutive_payment_failures
        if num_consecutive_failures is not None:
            self.num_consecutive_failures = num_consecutive_failures
        if payment_retry_window is not None:
            self.payment_retry_window = payment_retry_window
        if paypal_baid is not None:
            self.paypal_baid = paypal_baid
        if paypal_email is not None:
            self.paypal_email = paypal_email
        if paypal_preapproval_key is not None:
            self.paypal_preapproval_key = paypal_preapproval_key
        if paypal_type is not None:
            self.paypal_type = paypal_type
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if second_token_id is not None:
            self.second_token_id = second_token_id
        if skip_validation is not None:
            self.skip_validation = skip_validation
        if state is not None:
            self.state = state
        if street_name is not None:
            self.street_name = street_name
        if street_number is not None:
            self.street_number = street_number
        if token_id is not None:
            self.token_id = token_id
        if type is not None:
            self.type = type
        if use_default_retry_rule is not None:
            self.use_default_retry_rule = use_default_retry_rule
        if currency_code is not None:
            self.currency_code = currency_code

    @property
    def account_id(self):
        """Gets the account_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The ID of the customer account associated with this payment method. To create an orphan payment method that is not associated with any customer account, you do not need to specify this field during creation. However, you must associate the orphan payment method with a customer account within 10 days. Otherwise, this orphan payment method will be deleted.  # noqa: E501

        :return: The account_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProxyCreatePaymentMethodAllOf.

        The ID of the customer account associated with this payment method. To create an orphan payment method that is not associated with any customer account, you do not need to specify this field during creation. However, you must associate the orphan payment method with a customer account within 10 days. Otherwise, this orphan payment method will be deleted.  # noqa: E501

        :param account_id: The account_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def ach_aba_code(self):
        """Gets the ach_aba_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The nine-digit routing number or ABA number used by banks. This field is only required if the `Type` field is set to `ACH`.  **Character limit**: 9 **Values**: a string of 9 characters or fewer   # noqa: E501

        :return: The ach_aba_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_aba_code

    @ach_aba_code.setter
    def ach_aba_code(self, ach_aba_code):
        """Sets the ach_aba_code of this ProxyCreatePaymentMethodAllOf.

         The nine-digit routing number or ABA number used by banks. This field is only required if the `Type` field is set to `ACH`.  **Character limit**: 9 **Values**: a string of 9 characters or fewer   # noqa: E501

        :param ach_aba_code: The ach_aba_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_aba_code = ach_aba_code

    @property
    def ach_account_name(self):
        """Gets the ach_account_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The name of the account holder, which can be either a person or a company. This field is only required if the `Type` field is set to `ACH`.  **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The ach_account_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_account_name

    @ach_account_name.setter
    def ach_account_name(self, ach_account_name):
        """Sets the ach_account_name of this ProxyCreatePaymentMethodAllOf.

         The name of the account holder, which can be either a person or a company. This field is only required if the `Type` field is set to `ACH`.  **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param ach_account_name: The ach_account_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_account_name = ach_account_name

    @property
    def ach_account_number(self):
        """Gets the ach_account_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The bank account number associated with the ACH payment. This field is only required if the `Type` field is set to `ACH`. **Character limit**: 30 **Values**: a string of 30 numeric characters or fewer   # noqa: E501

        :return: The ach_account_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_account_number

    @ach_account_number.setter
    def ach_account_number(self, ach_account_number):
        """Sets the ach_account_number of this ProxyCreatePaymentMethodAllOf.

        The bank account number associated with the ACH payment. This field is only required if the `Type` field is set to `ACH`. **Character limit**: 30 **Values**: a string of 30 numeric characters or fewer   # noqa: E501

        :param ach_account_number: The ach_account_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_account_number = ach_account_number

    @property
    def ach_account_type(self):
        """Gets the ach_account_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The type of bank account associated with the ACH payment. This field is only required if the `Type` field is set to `ACH`. **Character limit**: 16 **Values**: - `BusinessChecking` - `Checking` - `Saving`   # noqa: E501

        :return: The ach_account_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_account_type

    @ach_account_type.setter
    def ach_account_type(self, ach_account_type):
        """Sets the ach_account_type of this ProxyCreatePaymentMethodAllOf.

         The type of bank account associated with the ACH payment. This field is only required if the `Type` field is set to `ACH`. **Character limit**: 16 **Values**: - `BusinessChecking` - `Checking` - `Saving`   # noqa: E501

        :param ach_account_type: The ach_account_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_account_type = ach_account_type

    @property
    def ach_address1(self):
        """Gets the ach_address1 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         Line 1 for the ACH address. This field is required for creating a payment method for the Vantiv payment gateway. **Character limit**: 255 **Values**: an address   # noqa: E501

        :return: The ach_address1 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_address1

    @ach_address1.setter
    def ach_address1(self, ach_address1):
        """Sets the ach_address1 of this ProxyCreatePaymentMethodAllOf.

         Line 1 for the ACH address. This field is required for creating a payment method for the Vantiv payment gateway. **Character limit**: 255 **Values**: an address   # noqa: E501

        :param ach_address1: The ach_address1 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_address1 = ach_address1

    @property
    def ach_address2(self):
        """Gets the ach_address2 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         Line 2 for the ACH address. This field is required for creating a payment method for the Vantiv payment gateway. **Character limit**: 255 **Values**: an address   # noqa: E501

        :return: The ach_address2 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_address2

    @ach_address2.setter
    def ach_address2(self, ach_address2):
        """Sets the ach_address2 of this ProxyCreatePaymentMethodAllOf.

         Line 2 for the ACH address. This field is required for creating a payment method for the Vantiv payment gateway. **Character limit**: 255 **Values**: an address   # noqa: E501

        :param ach_address2: The ach_address2 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_address2 = ach_address2

    @property
    def ach_bank_name(self):
        """Gets the ach_bank_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The name of the bank where the ACH payment account is held. This field is only required if the `Type` field is set to `ACH`. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The ach_bank_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_bank_name

    @ach_bank_name.setter
    def ach_bank_name(self, ach_bank_name):
        """Sets the ach_bank_name of this ProxyCreatePaymentMethodAllOf.

         The name of the bank where the ACH payment account is held. This field is only required if the `Type` field is set to `ACH`. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param ach_bank_name: The ach_bank_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_bank_name = ach_bank_name

    @property
    def ach_city(self):
        """Gets the ach_city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The city of the ACH address. Use this field for ACH payment methods. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The ach_city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_city

    @ach_city.setter
    def ach_city(self, ach_city):
        """Sets the ach_city of this ProxyCreatePaymentMethodAllOf.

        The city of the ACH address. Use this field for ACH payment methods. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param ach_city: The ach_city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_city = ach_city

    @property
    def ach_country(self):
        """Gets the ach_country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The country of the ACH address. See [Country Names and Their ISO Standard 2- and 3-Digit Codes](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/A_Country_Names_and_Their_ISO_Codes) for the list of supported country names. Use this field for ACH methods. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 40 **Values**: a supported country name   # noqa: E501

        :return: The ach_country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_country

    @ach_country.setter
    def ach_country(self, ach_country):
        """Sets the ach_country of this ProxyCreatePaymentMethodAllOf.

        The country of the ACH address. See [Country Names and Their ISO Standard 2- and 3-Digit Codes](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/A_Country_Names_and_Their_ISO_Codes) for the list of supported country names. Use this field for ACH methods. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 40 **Values**: a supported country name   # noqa: E501

        :param ach_country: The ach_country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_country = ach_country

    @property
    def ach_postal_code(self):
        """Gets the ach_postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The billing address's zip code. This field is required only when you define an ACH payment method. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :return: The ach_postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_postal_code

    @ach_postal_code.setter
    def ach_postal_code(self, ach_postal_code):
        """Sets the ach_postal_code of this ProxyCreatePaymentMethodAllOf.

        The billing address's zip code. This field is required only when you define an ACH payment method. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :param ach_postal_code: The ach_postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_postal_code = ach_postal_code

    @property
    def ach_state(self):
        """Gets the ach_state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The billing address's state. Use this field is if the `ACHCountry` value is either `Canada` or the `US`. State names must be spelled in full. For more information, see the list of [supported state names](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/B_State_Names_and_2-Digit_Codes). This field is required only when you define an ACH payment method. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 50 **Values**: a valid state name   # noqa: E501

        :return: The ach_state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ach_state

    @ach_state.setter
    def ach_state(self, ach_state):
        """Sets the ach_state of this ProxyCreatePaymentMethodAllOf.

        The billing address's state. Use this field is if the `ACHCountry` value is either `Canada` or the `US`. State names must be spelled in full. For more information, see the list of [supported state names](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/B_State_Names_and_2-Digit_Codes). This field is required only when you define an ACH payment method. **Note**: This field is only specific to the NMI payment gateway. **Character limit**: 50 **Values**: a valid state name   # noqa: E501

        :param ach_state: The ach_state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ach_state = ach_state

    @property
    def bank_branch_code(self):
        """Gets the bank_branch_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The branch code of the bank used for direct debit. Use this field for direct debit payment methods. **Character limit**: 10 **Values**: a string of 10 characters or fewer   # noqa: E501

        :return: The bank_branch_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bank_branch_code

    @bank_branch_code.setter
    def bank_branch_code(self, bank_branch_code):
        """Sets the bank_branch_code of this ProxyCreatePaymentMethodAllOf.

         The branch code of the bank used for direct debit. Use this field for direct debit payment methods. **Character limit**: 10 **Values**: a string of 10 characters or fewer   # noqa: E501

        :param bank_branch_code: The bank_branch_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._bank_branch_code = bank_branch_code

    @property
    def bank_check_digit(self):
        """Gets the bank_check_digit of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The check digit in the international bank account number, which confirms the validity of the account. Use this field for direct debit payment methods. **Character limit**: 4 **Values**: a string of 4 characters or fewer   # noqa: E501

        :return: The bank_check_digit of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bank_check_digit

    @bank_check_digit.setter
    def bank_check_digit(self, bank_check_digit):
        """Sets the bank_check_digit of this ProxyCreatePaymentMethodAllOf.

        The check digit in the international bank account number, which confirms the validity of the account. Use this field for direct debit payment methods. **Character limit**: 4 **Values**: a string of 4 characters or fewer   # noqa: E501

        :param bank_check_digit: The bank_check_digit of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._bank_check_digit = bank_check_digit

    @property
    def bank_transfer_account_name(self):
        """Gets the bank_transfer_account_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The name on the direct debit bank account. Use this field for direct debit payment methods.  **Character limit**: 60 **Values**: a string of 60 characters or fewer   # noqa: E501

        :return: The bank_transfer_account_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_account_name

    @bank_transfer_account_name.setter
    def bank_transfer_account_name(self, bank_transfer_account_name):
        """Sets the bank_transfer_account_name of this ProxyCreatePaymentMethodAllOf.

        The name on the direct debit bank account. Use this field for direct debit payment methods.  **Character limit**: 60 **Values**: a string of 60 characters or fewer   # noqa: E501

        :param bank_transfer_account_name: The bank_transfer_account_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._bank_transfer_account_name = bank_transfer_account_name

    @property
    def bank_transfer_account_number(self):
        """Gets the bank_transfer_account_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The number of the customer's bank account. Use this field for direct debit payment methods.  **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :return: The bank_transfer_account_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_account_number

    @bank_transfer_account_number.setter
    def bank_transfer_account_number(self, bank_transfer_account_number):
        """Sets the bank_transfer_account_number of this ProxyCreatePaymentMethodAllOf.

        The number of the customer's bank account. Use this field for direct debit payment methods.  **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :param bank_transfer_account_number: The bank_transfer_account_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._bank_transfer_account_number = bank_transfer_account_number

    @property
    def bank_transfer_account_number_mask(self):
        """Gets the bank_transfer_account_number_mask of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         This is a masked displayable version of the ACH account number, used for security purposes. For example: `XXXXXXXXX54321`.  **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The bank_transfer_account_number_mask of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_account_number_mask

    @bank_transfer_account_number_mask.setter
    def bank_transfer_account_number_mask(self, bank_transfer_account_number_mask):
        """Sets the bank_transfer_account_number_mask of this ProxyCreatePaymentMethodAllOf.

         This is a masked displayable version of the ACH account number, used for security purposes. For example: `XXXXXXXXX54321`.  **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param bank_transfer_account_number_mask: The bank_transfer_account_number_mask of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._bank_transfer_account_number_mask = bank_transfer_account_number_mask

    @property
    def bank_transfer_type(self):
        """Gets the bank_transfer_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The type of direct debit transfer. The value of this field is dependent on the country of the user. This field is only required if the `Type` field is set to `BankTransfer`.   **Values**:      - `SEPA`         - `AutomatischIncasso` (Netherlands)     - `LastschriftDE` (Germany)     - `LastschriftAT` (Austria)     - `DemandeDePrelevement` (France)     - `DirectEntryAU` (Australia)     - `DirectDebitUK` (UK)     - `Domicil` (Belgium)     - `LastschriftCH` (Switzerland)     - `RID` (Italy)     - `OrdenDeDomiciliacion` (Spain)    - `Autogiro` (Sweden)    - `Betalingsservice` (Denmark)   # noqa: E501

        :return: The bank_transfer_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_type

    @bank_transfer_type.setter
    def bank_transfer_type(self, bank_transfer_type):
        """Sets the bank_transfer_type of this ProxyCreatePaymentMethodAllOf.

        The type of direct debit transfer. The value of this field is dependent on the country of the user. This field is only required if the `Type` field is set to `BankTransfer`.   **Values**:      - `SEPA`         - `AutomatischIncasso` (Netherlands)     - `LastschriftDE` (Germany)     - `LastschriftAT` (Austria)     - `DemandeDePrelevement` (France)     - `DirectEntryAU` (Australia)     - `DirectDebitUK` (UK)     - `Domicil` (Belgium)     - `LastschriftCH` (Switzerland)     - `RID` (Italy)     - `OrdenDeDomiciliacion` (Spain)    - `Autogiro` (Sweden)    - `Betalingsservice` (Denmark)   # noqa: E501

        :param bank_transfer_type: The bank_transfer_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                bank_transfer_type is not None and len(bank_transfer_type) > 20):
            raise ValueError("Invalid value for `bank_transfer_type`, length must be less than or equal to `20`")  # noqa: E501

        self._bank_transfer_type = bank_transfer_type

    @property
    def business_identification_code(self):
        """Gets the business_identification_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The business identification code for Swiss direct payment methods that use the Global Collect payment gateway. Use this field only for direct debit payments in Switzerland with Global Collect. **Character limit**: 11 **Values**: a string of 11 characters or fewer   # noqa: E501

        :return: The business_identification_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._business_identification_code

    @business_identification_code.setter
    def business_identification_code(self, business_identification_code):
        """Sets the business_identification_code of this ProxyCreatePaymentMethodAllOf.

         The business identification code for Swiss direct payment methods that use the Global Collect payment gateway. Use this field only for direct debit payments in Switzerland with Global Collect. **Character limit**: 11 **Values**: a string of 11 characters or fewer   # noqa: E501

        :param business_identification_code: The business_identification_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._business_identification_code = business_identification_code

    @property
    def city(self):
        """Gets the city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The city of the customer's address. Use this field for direct debit payment methods. **Character limit**:80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :return: The city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ProxyCreatePaymentMethodAllOf.

         The city of the customer's address. Use this field for direct debit payment methods. **Character limit**:80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :param city: The city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company_name(self):
        """Gets the company_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The name of the company.  Zuora does not recommend that you use this field.   # noqa: E501

        :return: The company_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ProxyCreatePaymentMethodAllOf.

        The name of the company.  Zuora does not recommend that you use this field.   # noqa: E501

        :param company_name: The company_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) > 80):
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `80`")  # noqa: E501

        self._company_name = company_name

    @property
    def country(self):
        """Gets the country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The two-letter country code of the customer's address. This field is only required if the `Type` field is set to `BankTransfer`, and the `BankTransferType` field is set to either `DirectDebitUK`, `DirectEntryAU`, or `DirectDebitNZ`. **Character limit**: 2 **Values**: a valid country code   # noqa: E501

        :return: The country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ProxyCreatePaymentMethodAllOf.

         The two-letter country code of the customer's address. This field is only required if the `Type` field is set to `BankTransfer`, and the `BankTransferType` field is set to either `DirectDebitUK`, `DirectEntryAU`, or `DirectDebitNZ`. **Character limit**: 2 **Values**: a valid country code   # noqa: E501

        :param country: The country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def credit_card_address1(self):
        """Gets the credit_card_address1 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The first line of the card holder's address, which is often a street address or business name. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The credit_card_address1 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_address1

    @credit_card_address1.setter
    def credit_card_address1(self, credit_card_address1):
        """Sets the credit_card_address1 of this ProxyCreatePaymentMethodAllOf.

         The first line of the card holder's address, which is often a street address or business name. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param credit_card_address1: The credit_card_address1 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_address1 = credit_card_address1

    @property
    def credit_card_address2(self):
        """Gets the credit_card_address2 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The second line of the card holder's address. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The credit_card_address2 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_address2

    @credit_card_address2.setter
    def credit_card_address2(self, credit_card_address2):
        """Sets the credit_card_address2 of this ProxyCreatePaymentMethodAllOf.

         The second line of the card holder's address. Use this field for credit card and direct debit payment methods. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param credit_card_address2: The credit_card_address2 of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_address2 = credit_card_address2

    @property
    def credit_card_city(self):
        """Gets the credit_card_city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The city of the card holder's address. Use this field for credit card and direct debit payment methods **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The credit_card_city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_city

    @credit_card_city.setter
    def credit_card_city(self, credit_card_city):
        """Sets the credit_card_city of this ProxyCreatePaymentMethodAllOf.

         The city of the card holder's address. Use this field for credit card and direct debit payment methods **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param credit_card_city: The credit_card_city of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_city = credit_card_city

    @property
    def credit_card_country(self):
        """Gets the credit_card_country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The country of the card holder's address.   # noqa: E501

        :return: The credit_card_country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_country

    @credit_card_country.setter
    def credit_card_country(self, credit_card_country):
        """Sets the credit_card_country of this ProxyCreatePaymentMethodAllOf.

         The country of the card holder's address.   # noqa: E501

        :param credit_card_country: The credit_card_country of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_country = credit_card_country

    @property
    def credit_card_expiration_month(self):
        """Gets the credit_card_expiration_month of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The expiration month of the credit card or debit card. This field is only required if the `Type` field is set to `CreditCard` or `DebitCard`. **Character limit**: 2 **Values**: a two-digit number, 01 - 12   # noqa: E501

        :return: The credit_card_expiration_month of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_expiration_month

    @credit_card_expiration_month.setter
    def credit_card_expiration_month(self, credit_card_expiration_month):
        """Sets the credit_card_expiration_month of this ProxyCreatePaymentMethodAllOf.

         The expiration month of the credit card or debit card. This field is only required if the `Type` field is set to `CreditCard` or `DebitCard`. **Character limit**: 2 **Values**: a two-digit number, 01 - 12   # noqa: E501

        :param credit_card_expiration_month: The credit_card_expiration_month of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: int
        """

        self._credit_card_expiration_month = credit_card_expiration_month

    @property
    def credit_card_expiration_year(self):
        """Gets the credit_card_expiration_year of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The expiration month of the credit card or debit card. This field is only required if the `Type` field is set to `CreditCard` or `DebitCard`. **Character limit**: 4 **Values**: a four-digit number   # noqa: E501

        :return: The credit_card_expiration_year of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_expiration_year

    @credit_card_expiration_year.setter
    def credit_card_expiration_year(self, credit_card_expiration_year):
        """Sets the credit_card_expiration_year of this ProxyCreatePaymentMethodAllOf.

         The expiration month of the credit card or debit card. This field is only required if the `Type` field is set to `CreditCard` or `DebitCard`. **Character limit**: 4 **Values**: a four-digit number   # noqa: E501

        :param credit_card_expiration_year: The credit_card_expiration_year of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: int
        """

        self._credit_card_expiration_year = credit_card_expiration_year

    @property
    def credit_card_holder_name(self):
        """Gets the credit_card_holder_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The full name of the card holder. This field is only required if the `Type` field is set to `CreditCard` or `DebitCard`.  **Character limit**: 50 **Values**: a string of 50 characters or fewer   # noqa: E501

        :return: The credit_card_holder_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_holder_name

    @credit_card_holder_name.setter
    def credit_card_holder_name(self, credit_card_holder_name):
        """Sets the credit_card_holder_name of this ProxyCreatePaymentMethodAllOf.

         The full name of the card holder. This field is only required if the `Type` field is set to `CreditCard` or `DebitCard`.  **Character limit**: 50 **Values**: a string of 50 characters or fewer   # noqa: E501

        :param credit_card_holder_name: The credit_card_holder_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_holder_name = credit_card_holder_name

    @property
    def credit_card_number(self):
        """Gets the credit_card_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        Credit card number, a string of up to 16 characters. This field can only be set when creating a new payment method; it cannot be queried or updated.   # noqa: E501

        :return: The credit_card_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, credit_card_number):
        """Sets the credit_card_number of this ProxyCreatePaymentMethodAllOf.

        Credit card number, a string of up to 16 characters. This field can only be set when creating a new payment method; it cannot be queried or updated.   # noqa: E501

        :param credit_card_number: The credit_card_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_number = credit_card_number

    @property
    def credit_card_postal_code(self):
        """Gets the credit_card_postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The billing address's zip code. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :return: The credit_card_postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_postal_code

    @credit_card_postal_code.setter
    def credit_card_postal_code(self, credit_card_postal_code):
        """Sets the credit_card_postal_code of this ProxyCreatePaymentMethodAllOf.

         The billing address's zip code. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :param credit_card_postal_code: The credit_card_postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_postal_code = credit_card_postal_code

    @property
    def credit_card_security_code(self):
        """Gets the credit_card_security_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The CVV or CVV2 security code. See [How do I control what information Zuora sends over to the Payment Gateway?](https://knowledgecenter.zuora.com/kb/How_do_I_control_information_sent_to_payment_gateways_when_verifying_payment_methods%3F) for more information. To ensure PCI compliance, this value is not stored and cannot be queried.   # noqa: E501

        :return: The credit_card_security_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_security_code

    @credit_card_security_code.setter
    def credit_card_security_code(self, credit_card_security_code):
        """Sets the credit_card_security_code of this ProxyCreatePaymentMethodAllOf.

        The CVV or CVV2 security code. See [How do I control what information Zuora sends over to the Payment Gateway?](https://knowledgecenter.zuora.com/kb/How_do_I_control_information_sent_to_payment_gateways_when_verifying_payment_methods%3F) for more information. To ensure PCI compliance, this value is not stored and cannot be queried.   # noqa: E501

        :param credit_card_security_code: The credit_card_security_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_security_code = credit_card_security_code

    @property
    def credit_card_state(self):
        """Gets the credit_card_state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The billing address's state. Use this field if the `CreditCardCountry` value is either Canada or the US. State names must be spelled in full.   # noqa: E501

        :return: The credit_card_state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_state

    @credit_card_state.setter
    def credit_card_state(self, credit_card_state):
        """Sets the credit_card_state of this ProxyCreatePaymentMethodAllOf.

         The billing address's state. Use this field if the `CreditCardCountry` value is either Canada or the US. State names must be spelled in full.   # noqa: E501

        :param credit_card_state: The credit_card_state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_state = credit_card_state

    @property
    def credit_card_type(self):
        """Gets the credit_card_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The type of the credit card.  Possible values  include `Visa`, `MasterCard`, `AmericanExpress`, `Discover`, `JCB`, and `Diners`. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).   # noqa: E501

        :return: The credit_card_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_type

    @credit_card_type.setter
    def credit_card_type(self, credit_card_type):
        """Sets the credit_card_type of this ProxyCreatePaymentMethodAllOf.

        The type of the credit card.  Possible values  include `Visa`, `MasterCard`, `AmericanExpress`, `Discover`, `JCB`, and `Diners`. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).   # noqa: E501

        :param credit_card_type: The credit_card_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._credit_card_type = credit_card_type

    @property
    def device_session_id(self):
        """Gets the device_session_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The session ID of the user when the `PaymentMethod` was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently only Verifi supports this field. **Character limit**: 255 **Values**:   # noqa: E501

        :return: The device_session_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._device_session_id

    @device_session_id.setter
    def device_session_id(self, device_session_id):
        """Sets the device_session_id of this ProxyCreatePaymentMethodAllOf.

         The session ID of the user when the `PaymentMethod` was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently only Verifi supports this field. **Character limit**: 255 **Values**:   # noqa: E501

        :param device_session_id: The device_session_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._device_session_id = device_session_id

    @property
    def email(self):
        """Gets the email of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         An email address for the payment method in addition to the bill to contact email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :return: The email of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ProxyCreatePaymentMethodAllOf.

         An email address for the payment method in addition to the bill to contact email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :param email: The email of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def existing_mandate(self):
        """Gets the existing_mandate of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         Indicates if the customer has an existing mandate or a new mandate. A mandate is a signed authorization for UK and NL customers. When you are migrating mandates from another system, be sure to set this field correctly. If you indicate that a new mandate is an existing mandate or vice-versa, then transactions fail. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No`   # noqa: E501

        :return: The existing_mandate of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._existing_mandate

    @existing_mandate.setter
    def existing_mandate(self, existing_mandate):
        """Sets the existing_mandate of this ProxyCreatePaymentMethodAllOf.

         Indicates if the customer has an existing mandate or a new mandate. A mandate is a signed authorization for UK and NL customers. When you are migrating mandates from another system, be sure to set this field correctly. If you indicate that a new mandate is an existing mandate or vice-versa, then transactions fail. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No`   # noqa: E501

        :param existing_mandate: The existing_mandate of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._existing_mandate = existing_mandate

    @property
    def first_name(self):
        """Gets the first_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The customer's first name. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :return: The first_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ProxyCreatePaymentMethodAllOf.

         The customer's first name. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :param first_name: The first_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def gateway_option_data(self):
        """Gets the gateway_option_data of this ProxyCreatePaymentMethodAllOf.  # noqa: E501


        :return: The gateway_option_data of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: ProxyCreatePaymentAllOfGatewayOptionData
        """
        return self._gateway_option_data

    @gateway_option_data.setter
    def gateway_option_data(self, gateway_option_data):
        """Sets the gateway_option_data of this ProxyCreatePaymentMethodAllOf.


        :param gateway_option_data: The gateway_option_data of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: ProxyCreatePaymentAllOfGatewayOptionData
        """

        self._gateway_option_data = gateway_option_data

    @property
    def iban(self):
        """Gets the iban of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The International Bank Account Number. This field is used only for the direct debit payment method. **Character limit**: 42 **Values**: a string of 42 characters or fewer   # noqa: E501

        :return: The iban of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this ProxyCreatePaymentMethodAllOf.

         The International Bank Account Number. This field is used only for the direct debit payment method. **Character limit**: 42 **Values**: a string of 42 characters or fewer   # noqa: E501

        :param iban: The iban of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def ip_address(self):
        """Gets the ip_address of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The IP address of the user when the payment method was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently PayPal, CyberSource, Authorize.Net, Verifi, and WorldPay support this field. **Character limit**: 15 **Values**: a string of 15 characters or fewer   # noqa: E501

        :return: The ip_address of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ProxyCreatePaymentMethodAllOf.

         The IP address of the user when the payment method was created or updated. Some gateways use this field for fraud prevention. If this field is passed to Zuora, then Zuora passes this field to supported gateways. Currently PayPal, CyberSource, Authorize.Net, Verifi, and WorldPay support this field. **Character limit**: 15 **Values**: a string of 15 characters or fewer   # noqa: E501

        :param ip_address: The ip_address of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def identity_number(self):
        """Gets the identity_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The unique identity number of the customer account.   This field is required only if the `BankTransferType` field is set to `Autogiro` or `Betalingsservice`. It is a string of 12 characters for a Swedish identity number, and a string of 10 characters for a Denish identity number.   # noqa: E501

        :return: The identity_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._identity_number

    @identity_number.setter
    def identity_number(self, identity_number):
        """Sets the identity_number of this ProxyCreatePaymentMethodAllOf.

        The unique identity number of the customer account.   This field is required only if the `BankTransferType` field is set to `Autogiro` or `Betalingsservice`. It is a string of 12 characters for a Swedish identity number, and a string of 10 characters for a Denish identity number.   # noqa: E501

        :param identity_number: The identity_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._identity_number = identity_number

    @property
    def is_company(self):
        """Gets the is_company of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        Whether the customer account is a company.  Zuora does not recommend that you use this field.    # noqa: E501

        :return: The is_company of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_company

    @is_company.setter
    def is_company(self, is_company):
        """Sets the is_company of this ProxyCreatePaymentMethodAllOf.

        Whether the customer account is a company.  Zuora does not recommend that you use this field.    # noqa: E501

        :param is_company: The is_company of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: bool
        """

        self._is_company = is_company

    @property
    def last_name(self):
        """Gets the last_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The customer's last name. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The last_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ProxyCreatePaymentMethodAllOf.

         The customer's last name. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param last_name: The last_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def last_transaction_date_time(self):
        """Gets the last_transaction_date_time of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The date of the most recent transaction. **Character limit**: 29 **Values**: a valid date and time value   # noqa: E501

        :return: The last_transaction_date_time of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._last_transaction_date_time

    @last_transaction_date_time.setter
    def last_transaction_date_time(self, last_transaction_date_time):
        """Sets the last_transaction_date_time of this ProxyCreatePaymentMethodAllOf.

         The date of the most recent transaction. **Character limit**: 29 **Values**: a valid date and time value   # noqa: E501

        :param last_transaction_date_time: The last_transaction_date_time of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: datetime
        """

        self._last_transaction_date_time = last_transaction_date_time

    @property
    def mandate_creation_date(self):
        """Gets the mandate_creation_date of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The date when the mandate was created, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :return: The mandate_creation_date of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: date
        """
        return self._mandate_creation_date

    @mandate_creation_date.setter
    def mandate_creation_date(self, mandate_creation_date):
        """Sets the mandate_creation_date of this ProxyCreatePaymentMethodAllOf.

         The date when the mandate was created, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :param mandate_creation_date: The mandate_creation_date of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: date
        """

        self._mandate_creation_date = mandate_creation_date

    @property
    def mandate_id(self):
        """Gets the mandate_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The ID of the mandate. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 36 **Values**: a string of 36 characters or fewer   # noqa: E501

        :return: The mandate_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mandate_id

    @mandate_id.setter
    def mandate_id(self, mandate_id):
        """Sets the mandate_id of this ProxyCreatePaymentMethodAllOf.

         The ID of the mandate. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 36 **Values**: a string of 36 characters or fewer   # noqa: E501

        :param mandate_id: The mandate_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._mandate_id = mandate_id

    @property
    def mandate_received(self):
        """Gets the mandate_received of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         Indicates if  the mandate was received. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No `(case-sensitive)   # noqa: E501

        :return: The mandate_received of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mandate_received

    @mandate_received.setter
    def mandate_received(self, mandate_received):
        """Sets the mandate_received of this ProxyCreatePaymentMethodAllOf.

         Indicates if  the mandate was received. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 3 **Values**: `Yes`, `No `(case-sensitive)   # noqa: E501

        :param mandate_received: The mandate_received of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._mandate_received = mandate_received

    @property
    def mandate_update_date(self):
        """Gets the mandate_update_date of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The date when the mandate was last updated, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :return: The mandate_update_date of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: date
        """
        return self._mandate_update_date

    @mandate_update_date.setter
    def mandate_update_date(self, mandate_update_date):
        """Sets the mandate_update_date of this ProxyCreatePaymentMethodAllOf.

         The date when the mandate was last updated, in `yyyy-mm-dd` format. A mandate is a signed authorization for UK and NL customers. This field is used only for the direct debit payment method. **Character limit**: 29   # noqa: E501

        :param mandate_update_date: The mandate_update_date of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: date
        """

        self._mandate_update_date = mandate_update_date

    @property
    def max_consecutive_payment_failures(self):
        """Gets the max_consecutive_payment_failures of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         Specifies the number of allowable consecutive failures Zuora attempts with the payment method before stopping. When the `UseDefaultRetryRule` field is set to `false`, this field is only required if the `PaymentRetryWindow` field is not defined. **Values**: a valid number   # noqa: E501

        :return: The max_consecutive_payment_failures of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: int
        """
        return self._max_consecutive_payment_failures

    @max_consecutive_payment_failures.setter
    def max_consecutive_payment_failures(self, max_consecutive_payment_failures):
        """Sets the max_consecutive_payment_failures of this ProxyCreatePaymentMethodAllOf.

         Specifies the number of allowable consecutive failures Zuora attempts with the payment method before stopping. When the `UseDefaultRetryRule` field is set to `false`, this field is only required if the `PaymentRetryWindow` field is not defined. **Values**: a valid number   # noqa: E501

        :param max_consecutive_payment_failures: The max_consecutive_payment_failures of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: int
        """

        self._max_consecutive_payment_failures = max_consecutive_payment_failures

    @property
    def num_consecutive_failures(self):
        """Gets the num_consecutive_failures of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The number of consecutive failed payments for this payment method. It is reset to `0` upon successful payment.    # noqa: E501

        :return: The num_consecutive_failures of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: int
        """
        return self._num_consecutive_failures

    @num_consecutive_failures.setter
    def num_consecutive_failures(self, num_consecutive_failures):
        """Sets the num_consecutive_failures of this ProxyCreatePaymentMethodAllOf.

        The number of consecutive failed payments for this payment method. It is reset to `0` upon successful payment.    # noqa: E501

        :param num_consecutive_failures: The num_consecutive_failures of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_consecutive_failures is not None and num_consecutive_failures > 100):  # noqa: E501
            raise ValueError("Invalid value for `num_consecutive_failures`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_consecutive_failures is not None and num_consecutive_failures < 0):  # noqa: E501
            raise ValueError("Invalid value for `num_consecutive_failures`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_consecutive_failures = num_consecutive_failures

    @property
    def payment_retry_window(self):
        """Gets the payment_retry_window of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The retry interval setting, which prevents making a payment attempt if the last failed attempt was within the last specified number of hours. When the `UseDefaultRetryRule` field is set to `false`, this field is only required if the `MaxConsecutivePaymentFailures` field is not defined. **Character limit**: 4 **Values**: a whole number between 1 and 1000, exclusive   # noqa: E501

        :return: The payment_retry_window of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: int
        """
        return self._payment_retry_window

    @payment_retry_window.setter
    def payment_retry_window(self, payment_retry_window):
        """Sets the payment_retry_window of this ProxyCreatePaymentMethodAllOf.

         The retry interval setting, which prevents making a payment attempt if the last failed attempt was within the last specified number of hours. When the `UseDefaultRetryRule` field is set to `false`, this field is only required if the `MaxConsecutivePaymentFailures` field is not defined. **Character limit**: 4 **Values**: a whole number between 1 and 1000, exclusive   # noqa: E501

        :param payment_retry_window: The payment_retry_window of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: int
        """

        self._payment_retry_window = payment_retry_window

    @property
    def paypal_baid(self):
        """Gets the paypal_baid of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The PayPal billing agreement ID, which is a contract between two PayPal accounts. Typically, the selling party initiates a request to create a BAID, and sends it to buying party for acceptance. The seller can keep track of the BAID and use it for future charges against the buyer. This field is only required if the `Type` field is set to `PayPal`. **Character limit**: 64 **Values**: a string of 64 characters or fewer   # noqa: E501

        :return: The paypal_baid of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._paypal_baid

    @paypal_baid.setter
    def paypal_baid(self, paypal_baid):
        """Sets the paypal_baid of this ProxyCreatePaymentMethodAllOf.

         The PayPal billing agreement ID, which is a contract between two PayPal accounts. Typically, the selling party initiates a request to create a BAID, and sends it to buying party for acceptance. The seller can keep track of the BAID and use it for future charges against the buyer. This field is only required if the `Type` field is set to `PayPal`. **Character limit**: 64 **Values**: a string of 64 characters or fewer   # noqa: E501

        :param paypal_baid: The paypal_baid of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._paypal_baid = paypal_baid

    @property
    def paypal_email(self):
        """Gets the paypal_email of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The email address associated with the account holder's PayPal account or of the PayPal account of the person paying for the service. This field is only required if the `Type` field is set to `PayPal`. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :return: The paypal_email of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._paypal_email

    @paypal_email.setter
    def paypal_email(self, paypal_email):
        """Sets the paypal_email of this ProxyCreatePaymentMethodAllOf.

         The email address associated with the account holder's PayPal account or of the PayPal account of the person paying for the service. This field is only required if the `Type` field is set to `PayPal`. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :param paypal_email: The paypal_email of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._paypal_email = paypal_email

    @property
    def paypal_preapproval_key(self):
        """Gets the paypal_preapproval_key of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         PayPal's Adaptive Payments API key. Zuora does not create this key, nor does it call PayPal to generate it. You must use PayPal's Adaptive Payments' API to generate this key, and then pass it to Zuora. Zuora uses this key to authorize future payments to PayPal's Adaptive Payments API. This field is only required if you use PayPal Adaptive Payments gateway. **Character limit**: 32 **Values**: a valid PayPal Adaptive Payment pre-approval key   # noqa: E501

        :return: The paypal_preapproval_key of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._paypal_preapproval_key

    @paypal_preapproval_key.setter
    def paypal_preapproval_key(self, paypal_preapproval_key):
        """Sets the paypal_preapproval_key of this ProxyCreatePaymentMethodAllOf.

         PayPal's Adaptive Payments API key. Zuora does not create this key, nor does it call PayPal to generate it. You must use PayPal's Adaptive Payments' API to generate this key, and then pass it to Zuora. Zuora uses this key to authorize future payments to PayPal's Adaptive Payments API. This field is only required if you use PayPal Adaptive Payments gateway. **Character limit**: 32 **Values**: a valid PayPal Adaptive Payment pre-approval key   # noqa: E501

        :param paypal_preapproval_key: The paypal_preapproval_key of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._paypal_preapproval_key = paypal_preapproval_key

    @property
    def paypal_type(self):
        """Gets the paypal_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         Specifies the PayPal gateway: PayFlow Pro (Express Checkout) or Adaptive Payments. This field is only required if you use PayPal Adaptive Payments or Payflow Pro (Express Checkout) gateways. **Character limit**: 32 **Values**: `ExpressCheckout`, `AdaptivePayments`   # noqa: E501

        :return: The paypal_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._paypal_type

    @paypal_type.setter
    def paypal_type(self, paypal_type):
        """Sets the paypal_type of this ProxyCreatePaymentMethodAllOf.

         Specifies the PayPal gateway: PayFlow Pro (Express Checkout) or Adaptive Payments. This field is only required if you use PayPal Adaptive Payments or Payflow Pro (Express Checkout) gateways. **Character limit**: 32 **Values**: `ExpressCheckout`, `AdaptivePayments`   # noqa: E501

        :param paypal_type: The paypal_type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._paypal_type = paypal_type

    @property
    def phone(self):
        """Gets the phone of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The phone number that the account holder registered with the bank. This field is used for credit card validation when passing to a gateway. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The phone of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ProxyCreatePaymentMethodAllOf.

         The phone number that the account holder registered with the bank. This field is used for credit card validation when passing to a gateway. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param phone: The phone of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         The zip code of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :return: The postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ProxyCreatePaymentMethodAllOf.

         The zip code of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 20 **Values**: a string of 20 characters or fewer   # noqa: E501

        :param postal_code: The postal_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def second_token_id(self):
        """Gets the second_token_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

         A gateway unique identifier that replaces sensitive payment method data. `SecondTokenId` is conditionally required only when `TokenId` is being used to represent a gateway customer profile. `SecondTokenId` is used in the CC Reference Transaction payment method. **Character limit**: 64 **Values**: a string of 64 characters or fewer   # noqa: E501

        :return: The second_token_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._second_token_id

    @second_token_id.setter
    def second_token_id(self, second_token_id):
        """Sets the second_token_id of this ProxyCreatePaymentMethodAllOf.

         A gateway unique identifier that replaces sensitive payment method data. `SecondTokenId` is conditionally required only when `TokenId` is being used to represent a gateway customer profile. `SecondTokenId` is used in the CC Reference Transaction payment method. **Character limit**: 64 **Values**: a string of 64 characters or fewer   # noqa: E501

        :param second_token_id: The second_token_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._second_token_id = second_token_id

    @property
    def skip_validation(self):
        """Gets the skip_validation of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        If you set this field to `false`, Zuora will send an authorization request to the payment gateway. If the authorization fails, the Create Payment Method request will fail as well. If the user knows that the card number or token is valid, we recommend disabling this feature because authorization requests to the card network incur additional processing fees. Currently, Zuora sends all authorizations as keyed entries. If you set this field to `true`, the authorization request is not sent. **Character limit**: 5 **Values**: `true` or `false`   # noqa: E501

        :return: The skip_validation of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._skip_validation

    @skip_validation.setter
    def skip_validation(self, skip_validation):
        """Sets the skip_validation of this ProxyCreatePaymentMethodAllOf.

        If you set this field to `false`, Zuora will send an authorization request to the payment gateway. If the authorization fails, the Create Payment Method request will fail as well. If the user knows that the card number or token is valid, we recommend disabling this feature because authorization requests to the card network incur additional processing fees. Currently, Zuora sends all authorizations as keyed entries. If you set this field to `true`, the authorization request is not sent. **Character limit**: 5 **Values**: `true` or `false`   # noqa: E501

        :param skip_validation: The skip_validation of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: bool
        """

        self._skip_validation = skip_validation

    @property
    def state(self):
        """Gets the state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The state of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :return: The state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProxyCreatePaymentMethodAllOf.

        The state of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 70 **Values**: a string of 70 characters or fewer   # noqa: E501

        :param state: The state of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def street_name(self):
        """Gets the street_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The street name of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The street_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this ProxyCreatePaymentMethodAllOf.

        The street name of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param street_name: The street_name of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def street_number(self):
        """Gets the street_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The street number of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :return: The street_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """Sets the street_number of this ProxyCreatePaymentMethodAllOf.

        The street number of the customer's address. This field is used only for the direct debit payment method. **Character limit**: 30 **Values**: a string of 30 characters or fewer   # noqa: E501

        :param street_number: The street_number of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._street_number = street_number

    @property
    def token_id(self):
        """Gets the token_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        A gateway unique identifier that replaces sensitive payment method data or represents a gateway's unique customer profile. When `TokenId` is used to represent a customer profile, `SecondTokenId` is conditionally required for representing the underlying tokenized payment method. `TokenId` is required for the CC Reference Transaction payment method. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The token_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this ProxyCreatePaymentMethodAllOf.

        A gateway unique identifier that replaces sensitive payment method data or represents a gateway's unique customer profile. When `TokenId` is used to represent a customer profile, `SecondTokenId` is conditionally required for representing the underlying tokenized payment method. `TokenId` is required for the CC Reference Transaction payment method. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param token_id: The token_id of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def type(self):
        """Gets the type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The type of payment method.   If you want to create an Amazon Pay payment method, specify `CreditCardReferenceTransaction` for this field.   If you want create a custom payment method, specify the name of the custom payment method type. This type is only available if the Universal Payment Connector and Open Payment Method services are enabled. See [Set up custom payment gateways and payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) for details.   # noqa: E501

        :return: The type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProxyCreatePaymentMethodAllOf.

        The type of payment method.   If you want to create an Amazon Pay payment method, specify `CreditCardReferenceTransaction` for this field.   If you want create a custom payment method, specify the name of the custom payment method type. This type is only available if the Universal Payment Connector and Open Payment Method services are enabled. See [Set up custom payment gateways and payment methods](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/MB_Set_up_custom_payment_gateways_and_payment_methods) for details.   # noqa: E501

        :param type: The type of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACH", "BankTransfer", "CreditCard", "CreditCardReferenceTransaction", "DebitCard", "PayPal"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def use_default_retry_rule(self):
        """Gets the use_default_retry_rule of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        Determines whether to use the default retry rules configured in the Z-Payments settings. Set this to `true` to use the default retry rules. Set this to `false` to set the specific rules for this payment method. If you set this value to `false`, then the fields, `PaymentRetryWindow` and `MaxConsecutivePaymentFailures`, are required. **Character limit**: 5 **Values**: `true` or `false`   # noqa: E501

        :return: The use_default_retry_rule of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_retry_rule

    @use_default_retry_rule.setter
    def use_default_retry_rule(self, use_default_retry_rule):
        """Sets the use_default_retry_rule of this ProxyCreatePaymentMethodAllOf.

        Determines whether to use the default retry rules configured in the Z-Payments settings. Set this to `true` to use the default retry rules. Set this to `false` to set the specific rules for this payment method. If you set this value to `false`, then the fields, `PaymentRetryWindow` and `MaxConsecutivePaymentFailures`, are required. **Character limit**: 5 **Values**: `true` or `false`   # noqa: E501

        :param use_default_retry_rule: The use_default_retry_rule of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: bool
        """

        self._use_default_retry_rule = use_default_retry_rule

    @property
    def currency_code(self):
        """Gets the currency_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501

        The currency used for payment method authorization.  If this field is not specified, `currency` specified for the account is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.   # noqa: E501

        :return: The currency_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ProxyCreatePaymentMethodAllOf.

        The currency used for payment method authorization.  If this field is not specified, `currency` specified for the account is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.   # noqa: E501

        :param currency_code: The currency_code of this ProxyCreatePaymentMethodAllOf.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

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
        if not isinstance(other, ProxyCreatePaymentMethodAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProxyCreatePaymentMethodAllOf):
            return True

        return self.to_dict() != other.to_dict()
