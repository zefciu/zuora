# coding: utf-8

"""
    API Reference: Billing

      # Introduction  Welcome to the reference for the Zuora Billing REST API!  To learn about the common use cases of Zuora Billing REST APIs, check out the [API Guides](https://www.zuora.com/developer/api-guides/).  In addition to Zuora API Reference; Billing, we also provide API references for other Zuora products:    * [API Reference: Collections](https://www.zuora.com/developer/collect-api/)   * [API Reference: Revenue](https://www.zuora.com/developer/revpro-api/)      The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Billing Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Cloud 1 Production | https://rest.na.zuora.com  | |US Cloud 1 API Sandbox |  https://rest.sandbox.na.zuora.com | |US Cloud 2 Production | https://rest.zuora.com | |US Cloud 2 API Sandbox | https://rest.apisandbox.zuora.com| |US Central Sandbox | https://rest.test.zuora.com |   |US Performance Test | https://rest.pt1.zuora.com | |US Production Copy | Submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints. See [REST endpoint base URL of Production Copy (Service) Environment for existing and new customers](https://community.zuora.com/t5/API/REST-endpoint-base-URL-of-Production-Copy-Service-Environment/td-p/29611) for more information. | |EU Production | https://rest.eu.zuora.com | |EU API Sandbox | https://rest.sandbox.eu.zuora.com | |EU Central Sandbox | https://rest.test.eu.zuora.com |  The Production endpoint provides access to your live user data. Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision a Sandbox tenant for you, contact your Zuora representative for assistance.   If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/communities/community-home/digestviewer/viewthread?GroupId=103&MessageKey=6a672528-d068-47fa-a111-a3f118e016f3&CommunityKey=e2a932b4-50c4-4019-a3e8-362e38714df3&tab=digestviewer&ReturnUrl=%2fcommunities%2fcommunity-home%2fdigestviewer%3fMessageKey%3db8cc94ea-9092-4974-9964-ff19dc5c6d67%26CommunityKey%3de2a932b4-50c4-4019-a3e8-362e38714df3\" target=\"_blank\">Changelog</a> of the API Reference: Billing in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. You should reuse the bearer token until it is expired. When the token is expired, call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new one.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.   ## Making asynchronous requests  Most Zuora REST API endpoints documented in this API Reference process requests synchronously. In high-throughput scenarios, your requests to these endpoints are usually rate limited.   One strategy for avoiding rate limits is to make asynchronous requests, and Zuora provides this option to you.  Making asynchronous requests allows you to scale your applications more efficiently by leveraging Zuora's infrastructure to enqueue and execute requests for you without blocking. These requests also use built-in retry semantics, which makes them much less likely to fail for non-deterministic reasons, even in extreme high-throughput scenarios.  Meanwhile, when you send a request to one of these endpoints, you can receive a response in less than 150 milliseconds and these calls are unlikely to trigger rate limit errors.   You can make asynchronous requests to the POST, PUT, or DELETE operations, except [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions), for all resources documented in this API Reference.  Take the following steps to take advantage of the asynchronous API:    1. Set up callout notification   2. Make asynchronous requests  The following sections describes the high-level steps for you to get the most of the asynchronous API. For detailed instructions, see [Make asynchronous requests](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Make_asynchronous_requests) in the Knowledge Center.   ### Set up notifications  You can create callout notification definitions based on the following custom events through the Zuora UI or the [Create a notification definition](https://www.zuora.com/developer/api-reference/#operation/POST_Create_Notification_Definition) API operation:   * Async Request Succeeded   * Async Request Failed  This step ensures that your system receives a callout when an asynchronous request succeeds or fails.   ### Make asynchronous requests  By design, asynchronous requests differ from their synchronous counterparts in endpoints, and the HTTP status response code and response body they return. ??????The header parameters and request body schema for asynchronous operations are the same as their synchronous counterparts.   * The endpoints for asynchronous API operations contain `/async` in the path after `/v1`. See the following table for examples:  | Operation               | Synchronous endpoint  | Asynchronous endpoint      | |:-------- |:-------- |:-------- | | Create an account       | `/v1/accounts`        | `/v1/async/accounts`       | | CRUD: Create an account | `/v1/object/account`  | `/v1/async/object/account` |  * Unlike the 200 OK response for synchronous requests, Zuora returns a 202 Accepted response for all asynchronous requests, and the response body contains only a request ID.   **Note**: These asynchronous API endpoints are in addition to the previously introduced endpoints that support asynchronous processing. You should continue to use them:   * [Perform a mass action](https://www.zuora.com/developer/api-reference/#operation/POST_MassUpdater)   * [Create an order asynchronously](https://www.zuora.com/developer/api-reference/#operation/POST_CreateOrderAsynchronously)   * [Preview an order asynchronously](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrderAsynchronously)   * [Create a job to hard delete billing document files](https://www.zuora.com/developer/api-reference/#operation/POST_BillingDocumentFilesDeletionJob)   * [CRUD: Post or cancel a bill run](https://www.zuora.com/developer/api-reference/#operation/Object_PUTBillRun)   * [Cancel a journal run](https://www.zuora.com/developer/api-reference/#operation/PUT_JournalRun)   * [Run trial balance](https://www.zuora.com/developer/api-reference/#operation/PUT_RunTrialBalance)  For more information, see [Make asynchronous requests](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Make_asynchronous_requests).  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.   # Error Handling  If a request to Zuora Billing REST API with an endpoint starting with `/v1` (except [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations) fails, the response will contain an eight-digit error code with a corresponding error message to indicate the details of the error.  The following code snippet is a sample error response that contains an error code and message pair:  ```  {    \"success\": false,    \"processId\": \"CBCFED6580B4E076\",    \"reasons\":  [      {       \"code\": 53100320,       \"message\": \"'termType' value should be one of: TERMED, EVERGREEN\"      }     ]  } ``` The `success` field indicates whether the API request has succeeded. The `processId` field is a Zuora internal ID that you can provide to Zuora Global Support for troubleshooting purposes.  The `reasons` field contains the actual error code and message pair. The error code begins with `5` or `6` means that you encountered a certain issue that is specific to a REST API resource in Zuora Billing. For example, `53100320` indicates that an invalid value is specified for the `termType` field of the `subscription` object.  The error code beginning with `9` usually indicates that an authentication-related issue occurred, and it can also indicate other unexpected errors depending on different cases. For example, `90000011` indicates that an invalid credential is provided in the request header.   When troubleshooting the error, you can divide the error code into two components: REST API resource code and error category code. See the following Zuora error code sample:  <a href=\"https://assets.zuora.com/zuora-documentation/ZuoraErrorCode.jpeg\" target=\"_blank\"><img src=\"https://assets.zuora.com/zuora-documentation/ZuoraErrorCode.jpeg\" alt=\"Zuora Error Code Sample\"></a>   **Note:** Zuora determines resource codes based on the request payload. Therefore, if GET and DELETE requests that do not contain payloads fail, you will get `500000` as the resource code, which indicates an unknown object and an unknown field.  The error category code of these requests is valid and follows the rules described in the [Error Category Code](https://www.zuora.com/developer/api-reference/#section/Error-Handling/Error-Category-Code) section.  In such case, you can refer to the returned error message to troubleshoot.   ## REST API Resource Code  The 6-digit resource code indicates the REST API resource, typically a field of a Zuora object, on which the issue occurs. In the preceding example, `531003` refers to the `termType` field of the `subscription` object.   The value range for all REST API resource codes is from `500000` to `679999`. See [Resource Codes](https://knowledgecenter.zuora.com/Central_Platform/API/AA_REST_API/Resource_Codes) in the Knowledge Center for a full list of resource codes.  ## Error Category Code  The 2-digit error category code identifies the type of error, for example, resource not found or missing required field.   The following table describes all error categories and the corresponding resolution:  | Code    | Error category              | Description    | Resolution    | |:--------|:--------|:--------|:--------| | 10      | Permission or access denied | The request cannot be processed because a certain tenant or user permission is missing. | Check the missing tenant or user permission in the response message and contact [Zuora Global Support](https://support.zuora.com) for enablement. | | 11      | Authentication failed       | Authentication fails due to invalid API authentication credentials. | Ensure that a valid API credential is specified. | | 20      | Invalid format or value     | The request cannot be processed due to an invalid field format or value. | Check the invalid field in the error message, and ensure that the format and value of all fields you passed in are valid. | | 21      | Unknown field in request    | The request cannot be processed because an unknown field exists in the request body. | Check the unknown field name in the response message, and ensure that you do not include any unknown field in the request body. | | 22      | Missing required field      | The request cannot be processed because a required field in the request body is missing. | Check the missing field name in the response message, and ensure that you include all required fields in the request body. | | 23      | Missing required parameter  | The request cannot be processed because a required query parameter is missing. | Check the missing parameter name in the response message, and ensure that you include the parameter in the query. | | 30      | Rule restriction            | The request cannot be processed due to the violation of a Zuora business rule. | Check the response message and ensure that the API request meets the specified business rules. | | 40      | Not found                   | The specified resource cannot be found. | Check the response message and ensure that the specified resource exists in your Zuora tenant. | | 45      | Unsupported request         | The requested endpoint does not support the specified HTTP method. | Check your request and ensure that the endpoint and method matches. | | 50      | Locking contention          | This request cannot be processed because the objects this request is trying to modify are being modified by another API request, UI operation, or batch job process. | <p>Resubmit the request first to have another try.</p> <p>If this error still occurs, contact [Zuora Global Support](https://support.zuora.com) with the returned `Zuora-Request-Id` value in the response header for assistance.</p> | | 60      | Internal error              | The server encounters an internal error. | Contact [Zuora Global Support](https://support.zuora.com) with the returned `Zuora-Request-Id` value in the response header for assistance. | | 70      | Request exceeded limit      | The total number of concurrent requests exceeds the limit allowed by the system. | <p>Resubmit the request after the number of seconds specified by the `Retry-After` value in the response header.</p> <p>Check [Concurrent request limits](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits) for details about Zuora???s concurrent request limit policy.</p> | | 90      | Malformed request           | The request cannot be processed due to JSON syntax errors. | Check the syntax error in the JSON request body and ensure that the request is in the correct JSON format. | | 99      | Integration error           | The server encounters an error when communicating with an external system, for example, payment gateway, tax engine provider. | Check the response message and take action accordingly. |   # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. | | chargeId | 256.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | productRatePlanChargeId | 257.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | ID of the product rate plan charge that the memo is created from. | | comment | 256.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Comments about the product rate plan charge, invoice item, or memo item. | | description | 257.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\"); [Create credit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromInvoice \"Create credit memo from invoice\"); [Create debit memo from invoice](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromInvoice \"Create debit memo from invoice\"); [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Description of the the product rate plan charge, invoice item, or memo item. | | taxationItems | 309.0 and later | [Preview an order](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewOrder \"Preview an order\") | List of taxation items for an invoice item or a credit memo item. | | batch | 309.0 and earlier | [Create a billing preview run](https://www.zuora.com/developer/api-reference/#operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. |       | batches | 314.0 and later | [Create a billing preview run](https://www.zuora.com/developer/api-reference/#operation/POST_BillingPreviewRun \"Create a billing preview run\") | The customer batches to include in the billing preview run. | | taxationItems | 315.0 and later | [Preview a subscription](https://www.zuora.com/developer/api-reference/#operation/POST_PreviewSubscription \"Preview a subscription\"); [Update a subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update a subscription\")| List of taxation items for an invoice item or a credit memo item. |    #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Billing Object Model  The following diagram is a high-level view of how key business objects are related to one another within Zuora Billing.  Click the diagram to open it in a new tab and zoom in. For more information about the different sections of the diagram, see <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/A_Zuora_Billing_business_object_model\" target=\"_blank\">Zuora Billing business object model</a>.  <a href=\"https://assets.zuora.com/zuora-documentation/Zuora_Billing_object_model_Sep2020.png\" target=\"_blank\"><img src=\"https://assets.zuora.com/zuora-documentation/Zuora_Billing_object_model_Sep2020.png\" alt=\"Zuora Billing object model diagram\"></a>  This diagram is intended to provide a conceptual understanding; it does not illustrate a specific way to integrate with Zuora.  The diagram includes the Orders feature and the Invoice Settlement feature. If your organization does not use either of these features, see <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/B_Zuora_Billing_business_object_model_prior_to_Orders_and_Invoice_Settlement\" target=\"_blank\">Zuora Billing business object model prior to Orders and Invoice Settlement</a> for an alternative diagram.  ## API Names  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun` - API name used  in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query.</p> <p>`BillRun` - API name used in the [Actions](https://www.zuora.com/developer/api-reference/#tag/Actions). See the CRUD oprations of [Bill Run](https://www.zuora.com/developer/api-reference/#tag/Bill-Run) for more information about the `BillRun` object. `BillingRun` and `BillRun` have different fields. |                      | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Notification History - Callout                | `CalloutHistory`                           | | Notification History - Email                  | `EmailHistory`                             | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Line Items                              | `OrderLineItems`                           |     | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    The version of the OpenAPI document: 2022-02-10
    Contact: docs@zuora.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class POSTAccountTypeAllOf(object):
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
        'account_number': 'str',
        'additional_email_addresses': 'list[str]',
        'application_order': 'list[str]',
        'apply_credit': 'bool',
        'apply_credit_balance': 'bool',
        'auto_pay': 'bool',
        'batch': 'str',
        'bill_cycle_day': 'int',
        'bill_to_contact': 'POSTAccountTypeBillToContact',
        'collect': 'bool',
        'communication_profile_id': 'str',
        'credit_card': 'POSTAccountTypeCreditCard',
        'credit_memo_template_id': 'str',
        'crm_id': 'str',
        'currency': 'str',
        'debit_memo_template_id': 'str',
        'document_date': 'date',
        'hpm_credit_card_payment_method_id': 'str',
        'invoice': 'bool',
        'invoice_collect': 'bool',
        'invoice_delivery_prefs_email': 'bool',
        'invoice_delivery_prefs_print': 'bool',
        'invoice_target_date': 'date',
        'invoice_template_id': 'str',
        'name': 'str',
        'notes': 'str',
        'parent_id': 'str',
        'payment_gateway': 'str',
        'payment_method': 'POSTAccountTypePaymentMethod',
        'payment_term': 'str',
        'run_billing': 'bool',
        'sales_rep': 'str',
        'sequence_set_id': 'str',
        'sold_to_contact': 'POSTAccountTypeSoldToContact',
        'sold_to_same_as_bill_to': 'bool',
        'subscription': 'POSTAccountTypeSubscription',
        'tagging': 'str',
        'target_date': 'date',
        'tax_info': 'POSTAccountTypeAllOfTaxInfo'
    }

    attribute_map = {
        'account_number': 'accountNumber',
        'additional_email_addresses': 'additionalEmailAddresses',
        'application_order': 'applicationOrder',
        'apply_credit': 'applyCredit',
        'apply_credit_balance': 'applyCreditBalance',
        'auto_pay': 'autoPay',
        'batch': 'batch',
        'bill_cycle_day': 'billCycleDay',
        'bill_to_contact': 'billToContact',
        'collect': 'collect',
        'communication_profile_id': 'communicationProfileId',
        'credit_card': 'creditCard',
        'credit_memo_template_id': 'creditMemoTemplateId',
        'crm_id': 'crmId',
        'currency': 'currency',
        'debit_memo_template_id': 'debitMemoTemplateId',
        'document_date': 'documentDate',
        'hpm_credit_card_payment_method_id': 'hpmCreditCardPaymentMethodId',
        'invoice': 'invoice',
        'invoice_collect': 'invoiceCollect',
        'invoice_delivery_prefs_email': 'invoiceDeliveryPrefsEmail',
        'invoice_delivery_prefs_print': 'invoiceDeliveryPrefsPrint',
        'invoice_target_date': 'invoiceTargetDate',
        'invoice_template_id': 'invoiceTemplateId',
        'name': 'name',
        'notes': 'notes',
        'parent_id': 'parentId',
        'payment_gateway': 'paymentGateway',
        'payment_method': 'paymentMethod',
        'payment_term': 'paymentTerm',
        'run_billing': 'runBilling',
        'sales_rep': 'salesRep',
        'sequence_set_id': 'sequenceSetId',
        'sold_to_contact': 'soldToContact',
        'sold_to_same_as_bill_to': 'soldToSameAsBillTo',
        'subscription': 'subscription',
        'tagging': 'tagging',
        'target_date': 'targetDate',
        'tax_info': 'taxInfo'
    }

    def __init__(self, account_number=None, additional_email_addresses=None, application_order=None, apply_credit=None, apply_credit_balance=None, auto_pay=None, batch=None, bill_cycle_day=None, bill_to_contact=None, collect=True, communication_profile_id=None, credit_card=None, credit_memo_template_id=None, crm_id=None, currency=None, debit_memo_template_id=None, document_date=None, hpm_credit_card_payment_method_id=None, invoice=True, invoice_collect=True, invoice_delivery_prefs_email=False, invoice_delivery_prefs_print=False, invoice_target_date=None, invoice_template_id=None, name=None, notes=None, parent_id=None, payment_gateway=None, payment_method=None, payment_term=None, run_billing=True, sales_rep=None, sequence_set_id=None, sold_to_contact=None, sold_to_same_as_bill_to=None, subscription=None, tagging=None, target_date=None, tax_info=None, local_vars_configuration=None):  # noqa: E501
        """POSTAccountTypeAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_number = None
        self._additional_email_addresses = None
        self._application_order = None
        self._apply_credit = None
        self._apply_credit_balance = None
        self._auto_pay = None
        self._batch = None
        self._bill_cycle_day = None
        self._bill_to_contact = None
        self._collect = None
        self._communication_profile_id = None
        self._credit_card = None
        self._credit_memo_template_id = None
        self._crm_id = None
        self._currency = None
        self._debit_memo_template_id = None
        self._document_date = None
        self._hpm_credit_card_payment_method_id = None
        self._invoice = None
        self._invoice_collect = None
        self._invoice_delivery_prefs_email = None
        self._invoice_delivery_prefs_print = None
        self._invoice_target_date = None
        self._invoice_template_id = None
        self._name = None
        self._notes = None
        self._parent_id = None
        self._payment_gateway = None
        self._payment_method = None
        self._payment_term = None
        self._run_billing = None
        self._sales_rep = None
        self._sequence_set_id = None
        self._sold_to_contact = None
        self._sold_to_same_as_bill_to = None
        self._subscription = None
        self._tagging = None
        self._target_date = None
        self._tax_info = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        if additional_email_addresses is not None:
            self.additional_email_addresses = additional_email_addresses
        if application_order is not None:
            self.application_order = application_order
        if apply_credit is not None:
            self.apply_credit = apply_credit
        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if batch is not None:
            self.batch = batch
        if bill_cycle_day is not None:
            self.bill_cycle_day = bill_cycle_day
        self.bill_to_contact = bill_to_contact
        if collect is not None:
            self.collect = collect
        if communication_profile_id is not None:
            self.communication_profile_id = communication_profile_id
        if credit_card is not None:
            self.credit_card = credit_card
        if credit_memo_template_id is not None:
            self.credit_memo_template_id = credit_memo_template_id
        if crm_id is not None:
            self.crm_id = crm_id
        self.currency = currency
        if debit_memo_template_id is not None:
            self.debit_memo_template_id = debit_memo_template_id
        if document_date is not None:
            self.document_date = document_date
        if hpm_credit_card_payment_method_id is not None:
            self.hpm_credit_card_payment_method_id = hpm_credit_card_payment_method_id
        if invoice is not None:
            self.invoice = invoice
        if invoice_collect is not None:
            self.invoice_collect = invoice_collect
        if invoice_delivery_prefs_email is not None:
            self.invoice_delivery_prefs_email = invoice_delivery_prefs_email
        if invoice_delivery_prefs_print is not None:
            self.invoice_delivery_prefs_print = invoice_delivery_prefs_print
        if invoice_target_date is not None:
            self.invoice_target_date = invoice_target_date
        if invoice_template_id is not None:
            self.invoice_template_id = invoice_template_id
        self.name = name
        if notes is not None:
            self.notes = notes
        if parent_id is not None:
            self.parent_id = parent_id
        if payment_gateway is not None:
            self.payment_gateway = payment_gateway
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_term is not None:
            self.payment_term = payment_term
        if run_billing is not None:
            self.run_billing = run_billing
        if sales_rep is not None:
            self.sales_rep = sales_rep
        if sequence_set_id is not None:
            self.sequence_set_id = sequence_set_id
        if sold_to_contact is not None:
            self.sold_to_contact = sold_to_contact
        if sold_to_same_as_bill_to is not None:
            self.sold_to_same_as_bill_to = sold_to_same_as_bill_to
        if subscription is not None:
            self.subscription = subscription
        if tagging is not None:
            self.tagging = tagging
        if target_date is not None:
            self.target_date = target_date
        if tax_info is not None:
            self.tax_info = tax_info

    @property
    def account_number(self):
        """Gets the account_number of this POSTAccountTypeAllOf.  # noqa: E501

        A unique account number, up to 50 characters that do not begin with the default account number prefix.  If no account number is specified, one is generated.   # noqa: E501

        :return: The account_number of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this POSTAccountTypeAllOf.

        A unique account number, up to 50 characters that do not begin with the default account number prefix.  If no account number is specified, one is generated.   # noqa: E501

        :param account_number: The account_number of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def additional_email_addresses(self):
        """Gets the additional_email_addresses of this POSTAccountTypeAllOf.  # noqa: E501

        A list of additional email addresses to receive email notifications. Use commas to separate email addresses.   # noqa: E501

        :return: The additional_email_addresses of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_email_addresses

    @additional_email_addresses.setter
    def additional_email_addresses(self, additional_email_addresses):
        """Sets the additional_email_addresses of this POSTAccountTypeAllOf.

        A list of additional email addresses to receive email notifications. Use commas to separate email addresses.   # noqa: E501

        :param additional_email_addresses: The additional_email_addresses of this POSTAccountTypeAllOf.  # noqa: E501
        :type: list[str]
        """

        self._additional_email_addresses = additional_email_addresses

    @property
    def application_order(self):
        """Gets the application_order of this POSTAccountTypeAllOf.  # noqa: E501

        The priority order to apply credit memos and/or unapplied payments to an invoice. Possible item values are: `CreditMemo`, `UnappliedPayment`.  **Note:**   - This field is valid only if the `applyCredit` field is set to `true`.   - If no value is specified for this field, the default priority order is used, [\"CreditMemo\", \"UnappliedPayment\"], to apply credit memos first and then apply unapplied payments.   - If only one item is specified, only the items of the spedified type are applied to invoices. For example, if the value is `[\"CreditMemo\"]`, only credit memos are used to apply to invoices.   # noqa: E501

        :return: The application_order of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._application_order

    @application_order.setter
    def application_order(self, application_order):
        """Sets the application_order of this POSTAccountTypeAllOf.

        The priority order to apply credit memos and/or unapplied payments to an invoice. Possible item values are: `CreditMemo`, `UnappliedPayment`.  **Note:**   - This field is valid only if the `applyCredit` field is set to `true`.   - If no value is specified for this field, the default priority order is used, [\"CreditMemo\", \"UnappliedPayment\"], to apply credit memos first and then apply unapplied payments.   - If only one item is specified, only the items of the spedified type are applied to invoices. For example, if the value is `[\"CreditMemo\"]`, only credit memos are used to apply to invoices.   # noqa: E501

        :param application_order: The application_order of this POSTAccountTypeAllOf.  # noqa: E501
        :type: list[str]
        """

        self._application_order = application_order

    @property
    def apply_credit(self):
        """Gets the apply_credit of this POSTAccountTypeAllOf.  # noqa: E501

        Whether to automatically apply credit memos or unapplied payments, or both to an invoice.  If the value is `true`, the credit memo or unapplied payment, or both will be automatically applied to the invoice. If no value is specified or the value is `false`, no action is taken.  **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :return: The apply_credit of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit

    @apply_credit.setter
    def apply_credit(self, apply_credit):
        """Sets the apply_credit of this POSTAccountTypeAllOf.

        Whether to automatically apply credit memos or unapplied payments, or both to an invoice.  If the value is `true`, the credit memo or unapplied payment, or both will be automatically applied to the invoice. If no value is specified or the value is `false`, no action is taken.  **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   # noqa: E501

        :param apply_credit: The apply_credit of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._apply_credit = apply_credit

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this POSTAccountTypeAllOf.  # noqa: E501

        Applies a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.  Prerequisite: `invoice` must be `true`.  To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.    # noqa: E501

        :return: The apply_credit_balance of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this POSTAccountTypeAllOf.

        Applies a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.  Prerequisite: `invoice` must be `true`.  To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.    # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def auto_pay(self):
        """Gets the auto_pay of this POSTAccountTypeAllOf.  # noqa: E501

        Whether future payments are to be automatically billed when they are due.   - If this field is set to `true`, you must specify either the `creditCard` field or the `hpmCreditCardPaymentMethodId` field, but not both. - If this field is set to `false`, you can specify neither the `creditCard` field nor the `hpmCreditCardPaymentMethodId` field.   # noqa: E501

        :return: The auto_pay of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this POSTAccountTypeAllOf.

        Whether future payments are to be automatically billed when they are due.   - If this field is set to `true`, you must specify either the `creditCard` field or the `hpmCreditCardPaymentMethodId` field, but not both. - If this field is set to `false`, you can specify neither the `creditCard` field nor the `hpmCreditCardPaymentMethodId` field.   # noqa: E501

        :param auto_pay: The auto_pay of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def batch(self):
        """Gets the batch of this POSTAccountTypeAllOf.  # noqa: E501

        The alias name given to a batch. A string of 50 characters or less.   # noqa: E501

        :return: The batch of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this POSTAccountTypeAllOf.

        The alias name given to a batch. A string of 50 characters or less.   # noqa: E501

        :param batch: The batch of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._batch = batch

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this POSTAccountTypeAllOf.  # noqa: E501

        The account's bill cycle day (BCD), when bill runs generate invoices for the account.  Specify any day of the month (1-31, where 31 = end-of-month), or 0 for auto-set.  Required if no subscription will be created.   Optional if a subscription is created and defaults to the day-of-the-month of the subscription's `contractEffectiveDate`.   # noqa: E501

        :return: The bill_cycle_day of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this POSTAccountTypeAllOf.

        The account's bill cycle day (BCD), when bill runs generate invoices for the account.  Specify any day of the month (1-31, where 31 = end-of-month), or 0 for auto-set.  Required if no subscription will be created.   Optional if a subscription is created and defaults to the day-of-the-month of the subscription's `contractEffectiveDate`.   # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this POSTAccountTypeAllOf.  # noqa: E501
        :type: int
        """

        self._bill_cycle_day = bill_cycle_day

    @property
    def bill_to_contact(self):
        """Gets the bill_to_contact of this POSTAccountTypeAllOf.  # noqa: E501


        :return: The bill_to_contact of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: POSTAccountTypeBillToContact
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """Sets the bill_to_contact of this POSTAccountTypeAllOf.


        :param bill_to_contact: The bill_to_contact of this POSTAccountTypeAllOf.  # noqa: E501
        :type: POSTAccountTypeBillToContact
        """
        if self.local_vars_configuration.client_side_validation and bill_to_contact is None:  # noqa: E501
            raise ValueError("Invalid value for `bill_to_contact`, must not be `None`")  # noqa: E501

        self._bill_to_contact = bill_to_contact

    @property
    def collect(self):
        """Gets the collect of this POSTAccountTypeAllOf.  # noqa: E501

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  Prerequisite: The `invoice` or `runBilling` field must be `true`.   **Note**: This field is only available if you set the `zuora-version` request header to `196.0` or later.   # noqa: E501

        :return: The collect of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._collect

    @collect.setter
    def collect(self, collect):
        """Sets the collect of this POSTAccountTypeAllOf.

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  Prerequisite: The `invoice` or `runBilling` field must be `true`.   **Note**: This field is only available if you set the `zuora-version` request header to `196.0` or later.   # noqa: E501

        :param collect: The collect of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._collect = collect

    @property
    def communication_profile_id(self):
        """Gets the communication_profile_id of this POSTAccountTypeAllOf.  # noqa: E501

        The ID of a communication profile.            # noqa: E501

        :return: The communication_profile_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._communication_profile_id

    @communication_profile_id.setter
    def communication_profile_id(self, communication_profile_id):
        """Sets the communication_profile_id of this POSTAccountTypeAllOf.

        The ID of a communication profile.            # noqa: E501

        :param communication_profile_id: The communication_profile_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._communication_profile_id = communication_profile_id

    @property
    def credit_card(self):
        """Gets the credit_card of this POSTAccountTypeAllOf.  # noqa: E501


        :return: The credit_card of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: POSTAccountTypeCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """Sets the credit_card of this POSTAccountTypeAllOf.


        :param credit_card: The credit_card of this POSTAccountTypeAllOf.  # noqa: E501
        :type: POSTAccountTypeCreditCard
        """

        self._credit_card = credit_card

    @property
    def credit_memo_template_id(self):
        """Gets the credit_memo_template_id of this POSTAccountTypeAllOf.  # noqa: E501

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the credit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.   # noqa: E501

        :return: The credit_memo_template_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_template_id

    @credit_memo_template_id.setter
    def credit_memo_template_id(self, credit_memo_template_id):
        """Sets the credit_memo_template_id of this POSTAccountTypeAllOf.

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the credit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.   # noqa: E501

        :param credit_memo_template_id: The credit_memo_template_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._credit_memo_template_id = credit_memo_template_id

    @property
    def crm_id(self):
        """Gets the crm_id of this POSTAccountTypeAllOf.  # noqa: E501

        CRM account ID for the account, up to 100 characters.   # noqa: E501

        :return: The crm_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._crm_id

    @crm_id.setter
    def crm_id(self, crm_id):
        """Sets the crm_id of this POSTAccountTypeAllOf.

        CRM account ID for the account, up to 100 characters.   # noqa: E501

        :param crm_id: The crm_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._crm_id = crm_id

    @property
    def currency(self):
        """Gets the currency of this POSTAccountTypeAllOf.  # noqa: E501

        A currency as defined in Billing Settings in the Zuora UI.  For payment method authorization, if the `paymentMethod` > `currencyCode` field is specified, `currencyCode` is used. Otherwise, this `currency` field is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.   # noqa: E501

        :return: The currency of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this POSTAccountTypeAllOf.

        A currency as defined in Billing Settings in the Zuora UI.  For payment method authorization, if the `paymentMethod` > `currencyCode` field is specified, `currencyCode` is used. Otherwise, this `currency` field is used for payment method authorization. If no currency is specified for the account, the default currency of the account is then used.   # noqa: E501

        :param currency: The currency of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def debit_memo_template_id(self):
        """Gets the debit_memo_template_id of this POSTAccountTypeAllOf.  # noqa: E501

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the debit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.   # noqa: E501

        :return: The debit_memo_template_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._debit_memo_template_id

    @debit_memo_template_id.setter
    def debit_memo_template_id(self, debit_memo_template_id):
        """Sets the debit_memo_template_id of this POSTAccountTypeAllOf.

        **Note:** This field is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  The unique ID of the debit memo template, configured in **Billing Settings** > **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.   # noqa: E501

        :param debit_memo_template_id: The debit_memo_template_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._debit_memo_template_id = debit_memo_template_id

    @property
    def document_date(self):
        """Gets the document_date of this POSTAccountTypeAllOf.  # noqa: E501

        The date of the billing document, in `yyyy-mm-dd` format. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  - If this field is specified, the specified date is used as the billing document date.  - If this field is not specified, the date specified in the `targetDate` is used as the billing document date.   # noqa: E501

        :return: The document_date of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._document_date

    @document_date.setter
    def document_date(self, document_date):
        """Sets the document_date of this POSTAccountTypeAllOf.

        The date of the billing document, in `yyyy-mm-dd` format. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  - If this field is specified, the specified date is used as the billing document date.  - If this field is not specified, the date specified in the `targetDate` is used as the billing document date.   # noqa: E501

        :param document_date: The document_date of this POSTAccountTypeAllOf.  # noqa: E501
        :type: date
        """

        self._document_date = document_date

    @property
    def hpm_credit_card_payment_method_id(self):
        """Gets the hpm_credit_card_payment_method_id of this POSTAccountTypeAllOf.  # noqa: E501

        The ID of the payment method associated with this account. The payment method specified for this field will be set as the default payment method of the account.  If the `autoPay` field is set to `true`, you must provide the credit card payment method ID for either this field or the `creditCard` field, but not both.  For the Credit Card Reference Transaction payment method, you can specify the payment method ID in this field or use the `paymentMethod` field to create a CC Reference Transaction payment method for an account.   # noqa: E501

        :return: The hpm_credit_card_payment_method_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hpm_credit_card_payment_method_id

    @hpm_credit_card_payment_method_id.setter
    def hpm_credit_card_payment_method_id(self, hpm_credit_card_payment_method_id):
        """Sets the hpm_credit_card_payment_method_id of this POSTAccountTypeAllOf.

        The ID of the payment method associated with this account. The payment method specified for this field will be set as the default payment method of the account.  If the `autoPay` field is set to `true`, you must provide the credit card payment method ID for either this field or the `creditCard` field, but not both.  For the Credit Card Reference Transaction payment method, you can specify the payment method ID in this field or use the `paymentMethod` field to create a CC Reference Transaction payment method for an account.   # noqa: E501

        :param hpm_credit_card_payment_method_id: The hpm_credit_card_payment_method_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._hpm_credit_card_payment_method_id = hpm_credit_card_payment_method_id

    @property
    def invoice(self):
        """Gets the invoice of this POSTAccountTypeAllOf.  # noqa: E501

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.   Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, an invoice is created. If the value is `false`, no action is taken.  **Note**: This field is only available if you set the `zuora-version` request header to `196.0` or `207.0`.   # noqa: E501

        :return: The invoice of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this POSTAccountTypeAllOf.

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.   Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, an invoice is created. If the value is `false`, no action is taken.  **Note**: This field is only available if you set the `zuora-version` request header to `196.0` or `207.0`.   # noqa: E501

        :param invoice: The invoice of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._invoice = invoice

    @property
    def invoice_collect(self):
        """Gets the invoice_collect of this POSTAccountTypeAllOf.  # noqa: E501

         **Note:** This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.   If this field is set to `true`, and a subscription is created, an invoice is generated at account creation time and payment is immediately collected using the account's default payment method.   **Note**: This field is only available if you set the `zuora-version` request header to `186.0`, `187.0`, `188.0`, or `189.0`.   # noqa: E501

        :return: The invoice_collect of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_collect

    @invoice_collect.setter
    def invoice_collect(self, invoice_collect):
        """Sets the invoice_collect of this POSTAccountTypeAllOf.

         **Note:** This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.   If this field is set to `true`, and a subscription is created, an invoice is generated at account creation time and payment is immediately collected using the account's default payment method.   **Note**: This field is only available if you set the `zuora-version` request header to `186.0`, `187.0`, `188.0`, or `189.0`.   # noqa: E501

        :param invoice_collect: The invoice_collect of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._invoice_collect = invoice_collect

    @property
    def invoice_delivery_prefs_email(self):
        """Gets the invoice_delivery_prefs_email of this POSTAccountTypeAllOf.  # noqa: E501

        Whether the customer wants to receive invoices through email.    # noqa: E501

        :return: The invoice_delivery_prefs_email of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_delivery_prefs_email

    @invoice_delivery_prefs_email.setter
    def invoice_delivery_prefs_email(self, invoice_delivery_prefs_email):
        """Sets the invoice_delivery_prefs_email of this POSTAccountTypeAllOf.

        Whether the customer wants to receive invoices through email.    # noqa: E501

        :param invoice_delivery_prefs_email: The invoice_delivery_prefs_email of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._invoice_delivery_prefs_email = invoice_delivery_prefs_email

    @property
    def invoice_delivery_prefs_print(self):
        """Gets the invoice_delivery_prefs_print of this POSTAccountTypeAllOf.  # noqa: E501

        Whether the customer wants to receive printed invoices, such as through postal mail.   # noqa: E501

        :return: The invoice_delivery_prefs_print of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_delivery_prefs_print

    @invoice_delivery_prefs_print.setter
    def invoice_delivery_prefs_print(self, invoice_delivery_prefs_print):
        """Sets the invoice_delivery_prefs_print of this POSTAccountTypeAllOf.

        Whether the customer wants to receive printed invoices, such as through postal mail.   # noqa: E501

        :param invoice_delivery_prefs_print: The invoice_delivery_prefs_print of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._invoice_delivery_prefs_print = invoice_delivery_prefs_print

    @property
    def invoice_target_date(self):
        """Gets the invoice_target_date of this POSTAccountTypeAllOf.  # noqa: E501

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.     Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in REST API minor version control. To use this field in the method, you can set the `zuora-version` parameter to the minor version number in the request header. Supported minor versions are `207.0` and earlier.    # noqa: E501

        :return: The invoice_target_date of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._invoice_target_date

    @invoice_target_date.setter
    def invoice_target_date(self, invoice_target_date):
        """Sets the invoice_target_date of this POSTAccountTypeAllOf.

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.     Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in REST API minor version control. To use this field in the method, you can set the `zuora-version` parameter to the minor version number in the request header. Supported minor versions are `207.0` and earlier.    # noqa: E501

        :param invoice_target_date: The invoice_target_date of this POSTAccountTypeAllOf.  # noqa: E501
        :type: date
        """

        self._invoice_target_date = invoice_target_date

    @property
    def invoice_template_id(self):
        """Gets the invoice_template_id of this POSTAccountTypeAllOf.  # noqa: E501

        Invoice template ID, configured in Billing Settings in the Zuora UI.   # noqa: E501

        :return: The invoice_template_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._invoice_template_id

    @invoice_template_id.setter
    def invoice_template_id(self, invoice_template_id):
        """Sets the invoice_template_id of this POSTAccountTypeAllOf.

        Invoice template ID, configured in Billing Settings in the Zuora UI.   # noqa: E501

        :param invoice_template_id: The invoice_template_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._invoice_template_id = invoice_template_id

    @property
    def name(self):
        """Gets the name of this POSTAccountTypeAllOf.  # noqa: E501

        Account name, up to 255 characters.   # noqa: E501

        :return: The name of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this POSTAccountTypeAllOf.

        Account name, up to 255 characters.   # noqa: E501

        :param name: The name of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this POSTAccountTypeAllOf.  # noqa: E501

        A string of up to 65,535 characters.  # noqa: E501

        :return: The notes of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this POSTAccountTypeAllOf.

        A string of up to 65,535 characters.  # noqa: E501

        :param notes: The notes of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def parent_id(self):
        """Gets the parent_id of this POSTAccountTypeAllOf.  # noqa: E501

        Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled.  # noqa: E501

        :return: The parent_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this POSTAccountTypeAllOf.

        Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled.  # noqa: E501

        :param parent_id: The parent_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def payment_gateway(self):
        """Gets the payment_gateway of this POSTAccountTypeAllOf.  # noqa: E501

        The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.   # noqa: E501

        :return: The payment_gateway of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        """Sets the payment_gateway of this POSTAccountTypeAllOf.

        The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.   # noqa: E501

        :param payment_gateway: The payment_gateway of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._payment_gateway = payment_gateway

    @property
    def payment_method(self):
        """Gets the payment_method of this POSTAccountTypeAllOf.  # noqa: E501


        :return: The payment_method of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: POSTAccountTypePaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this POSTAccountTypeAllOf.


        :param payment_method: The payment_method of this POSTAccountTypeAllOf.  # noqa: E501
        :type: POSTAccountTypePaymentMethod
        """

        self._payment_method = payment_method

    @property
    def payment_term(self):
        """Gets the payment_term of this POSTAccountTypeAllOf.  # noqa: E501

        Payment terms for this account. Possible values are: `Due Upon Receipt`, `Net 30`, `Net 60`, `Net 90`.   # noqa: E501

        :return: The payment_term of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this POSTAccountTypeAllOf.

        Payment terms for this account. Possible values are: `Due Upon Receipt`, `Net 30`, `Net 60`, `Net 90`.   # noqa: E501

        :param payment_term: The payment_term of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._payment_term = payment_term

    @property
    def run_billing(self):
        """Gets the run_billing of this POSTAccountTypeAllOf.  # noqa: E501

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/B_Credit_and_Debit_Memos/Rules_for_generating_invoices_and_credit_memos).    The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The run_billing of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._run_billing

    @run_billing.setter
    def run_billing(self, run_billing):
        """Sets the run_billing of this POSTAccountTypeAllOf.

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/B_Credit_and_Debit_Memos/Rules_for_generating_invoices_and_credit_memos).    The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param run_billing: The run_billing of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._run_billing = run_billing

    @property
    def sales_rep(self):
        """Gets the sales_rep of this POSTAccountTypeAllOf.  # noqa: E501

        The name of the sales representative associated with this account, if applicable. Maximum of 50 characters.  # noqa: E501

        :return: The sales_rep of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sales_rep

    @sales_rep.setter
    def sales_rep(self, sales_rep):
        """Sets the sales_rep of this POSTAccountTypeAllOf.

        The name of the sales representative associated with this account, if applicable. Maximum of 50 characters.  # noqa: E501

        :param sales_rep: The sales_rep of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._sales_rep = sales_rep

    @property
    def sequence_set_id(self):
        """Gets the sequence_set_id of this POSTAccountTypeAllOf.  # noqa: E501

        The ID of the billing document sequence set to assign to the customer account.   The billing documents to generate for this account will adopt the prefix and starting document number configured in the sequence set.  If a customer account has no assigned billing document sequence set, billing documents generated for this account adopt the prefix and starting document number from the default sequence set.   # noqa: E501

        :return: The sequence_set_id of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sequence_set_id

    @sequence_set_id.setter
    def sequence_set_id(self, sequence_set_id):
        """Sets the sequence_set_id of this POSTAccountTypeAllOf.

        The ID of the billing document sequence set to assign to the customer account.   The billing documents to generate for this account will adopt the prefix and starting document number configured in the sequence set.  If a customer account has no assigned billing document sequence set, billing documents generated for this account adopt the prefix and starting document number from the default sequence set.   # noqa: E501

        :param sequence_set_id: The sequence_set_id of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._sequence_set_id = sequence_set_id

    @property
    def sold_to_contact(self):
        """Gets the sold_to_contact of this POSTAccountTypeAllOf.  # noqa: E501


        :return: The sold_to_contact of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: POSTAccountTypeSoldToContact
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """Sets the sold_to_contact of this POSTAccountTypeAllOf.


        :param sold_to_contact: The sold_to_contact of this POSTAccountTypeAllOf.  # noqa: E501
        :type: POSTAccountTypeSoldToContact
        """

        self._sold_to_contact = sold_to_contact

    @property
    def sold_to_same_as_bill_to(self):
        """Gets the sold_to_same_as_bill_to of this POSTAccountTypeAllOf.  # noqa: E501

        Whether the sold-to contact and bill-to contact are the same entity.   The created account has the same bill-to contact and sold-to contact entity only when all the following conditions are met in the request body:  - This field is set to `true`.  - A bill-to contact is specified. - No sold-to contact is specified.   # noqa: E501

        :return: The sold_to_same_as_bill_to of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._sold_to_same_as_bill_to

    @sold_to_same_as_bill_to.setter
    def sold_to_same_as_bill_to(self, sold_to_same_as_bill_to):
        """Sets the sold_to_same_as_bill_to of this POSTAccountTypeAllOf.

        Whether the sold-to contact and bill-to contact are the same entity.   The created account has the same bill-to contact and sold-to contact entity only when all the following conditions are met in the request body:  - This field is set to `true`.  - A bill-to contact is specified. - No sold-to contact is specified.   # noqa: E501

        :param sold_to_same_as_bill_to: The sold_to_same_as_bill_to of this POSTAccountTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._sold_to_same_as_bill_to = sold_to_same_as_bill_to

    @property
    def subscription(self):
        """Gets the subscription of this POSTAccountTypeAllOf.  # noqa: E501


        :return: The subscription of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: POSTAccountTypeSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this POSTAccountTypeAllOf.


        :param subscription: The subscription of this POSTAccountTypeAllOf.  # noqa: E501
        :type: POSTAccountTypeSubscription
        """

        self._subscription = subscription

    @property
    def tagging(self):
        """Gets the tagging of this POSTAccountTypeAllOf.  # noqa: E501

          # noqa: E501

        :return: The tagging of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._tagging

    @tagging.setter
    def tagging(self, tagging):
        """Sets the tagging of this POSTAccountTypeAllOf.

          # noqa: E501

        :param tagging: The tagging of this POSTAccountTypeAllOf.  # noqa: E501
        :type: str
        """

        self._tagging = tagging

    @property
    def target_date(self):
        """Gets the target_date of this POSTAccountTypeAllOf.  # noqa: E501

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.  **Note:** The credit memo is only available only if you have the Invoice Settlement feature enabled.  This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The target_date of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this POSTAccountTypeAllOf.

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.  **Note:** The credit memo is only available only if you have the Invoice Settlement feature enabled.  This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param target_date: The target_date of this POSTAccountTypeAllOf.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def tax_info(self):
        """Gets the tax_info of this POSTAccountTypeAllOf.  # noqa: E501


        :return: The tax_info of this POSTAccountTypeAllOf.  # noqa: E501
        :rtype: POSTAccountTypeAllOfTaxInfo
        """
        return self._tax_info

    @tax_info.setter
    def tax_info(self, tax_info):
        """Sets the tax_info of this POSTAccountTypeAllOf.


        :param tax_info: The tax_info of this POSTAccountTypeAllOf.  # noqa: E501
        :type: POSTAccountTypeAllOfTaxInfo
        """

        self._tax_info = tax_info

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
        if not isinstance(other, POSTAccountTypeAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, POSTAccountTypeAllOf):
            return True

        return self.to_dict() != other.to_dict()
