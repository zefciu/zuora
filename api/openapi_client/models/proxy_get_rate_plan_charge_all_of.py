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


class ProxyGetRatePlanChargeAllOf(object):
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
        'accounting_code': 'str',
        'apply_discount_to': 'str',
        'bill_cycle_day': 'int',
        'bill_cycle_type': 'str',
        'billing_period': 'str',
        'billing_period_alignment': 'str',
        'billing_timing': 'str',
        'charge_model': 'str',
        'charge_number': 'str',
        'charge_type': 'str',
        'charged_through_date': 'date',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'dmrc': 'float',
        'dtcv': 'float',
        'description': 'str',
        'discount_level': 'str',
        'effective_end_date': 'date',
        'effective_start_date': 'date',
        'end_date_condition': 'str',
        'id': 'str',
        'is_last_segment': 'bool',
        'list_price_base': 'str',
        'mrr': 'float',
        'name': 'str',
        'number_of_periods': 'int',
        'original_id': 'str',
        'overage_calculation_option': 'str',
        'overage_unused_units_credit_option': 'str',
        'price_change_option': 'str',
        'price_increase_percentage': 'float',
        'processed_through_date': 'date',
        'quantity': 'float',
        'rate_plan_id': 'str',
        'rating_group': 'str',
        'rev_rec_code': 'str',
        'rev_rec_trigger_condition': 'str',
        'revenue_recognition_rule_name': 'str',
        'rollover_balance': 'float',
        'segment': 'int',
        'specific_billing_period': 'int',
        'specific_end_date': 'date',
        'tcv': 'float',
        'trigger_date': 'date',
        'trigger_event': 'str',
        'uom': 'str',
        'up_to_periods': 'int',
        'up_to_periods_type': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime',
        'version': 'int',
        'weekly_bill_cycle_day': 'str'
    }

    attribute_map = {
        'accounting_code': 'AccountingCode',
        'apply_discount_to': 'ApplyDiscountTo',
        'bill_cycle_day': 'BillCycleDay',
        'bill_cycle_type': 'BillCycleType',
        'billing_period': 'BillingPeriod',
        'billing_period_alignment': 'BillingPeriodAlignment',
        'billing_timing': 'BillingTiming',
        'charge_model': 'ChargeModel',
        'charge_number': 'ChargeNumber',
        'charge_type': 'ChargeType',
        'charged_through_date': 'ChargedThroughDate',
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'dmrc': 'DMRC',
        'dtcv': 'DTCV',
        'description': 'Description',
        'discount_level': 'DiscountLevel',
        'effective_end_date': 'EffectiveEndDate',
        'effective_start_date': 'EffectiveStartDate',
        'end_date_condition': 'EndDateCondition',
        'id': 'Id',
        'is_last_segment': 'IsLastSegment',
        'list_price_base': 'ListPriceBase',
        'mrr': 'MRR',
        'name': 'Name',
        'number_of_periods': 'NumberOfPeriods',
        'original_id': 'OriginalId',
        'overage_calculation_option': 'OverageCalculationOption',
        'overage_unused_units_credit_option': 'OverageUnusedUnitsCreditOption',
        'price_change_option': 'PriceChangeOption',
        'price_increase_percentage': 'PriceIncreasePercentage',
        'processed_through_date': 'ProcessedThroughDate',
        'quantity': 'Quantity',
        'rate_plan_id': 'RatePlanId',
        'rating_group': 'RatingGroup',
        'rev_rec_code': 'RevRecCode',
        'rev_rec_trigger_condition': 'RevRecTriggerCondition',
        'revenue_recognition_rule_name': 'RevenueRecognitionRuleName',
        'rollover_balance': 'RolloverBalance',
        'segment': 'Segment',
        'specific_billing_period': 'SpecificBillingPeriod',
        'specific_end_date': 'SpecificEndDate',
        'tcv': 'TCV',
        'trigger_date': 'TriggerDate',
        'trigger_event': 'TriggerEvent',
        'uom': 'UOM',
        'up_to_periods': 'UpToPeriods',
        'up_to_periods_type': 'UpToPeriodsType',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate',
        'version': 'Version',
        'weekly_bill_cycle_day': 'WeeklyBillCycleDay'
    }

    def __init__(self, accounting_code=None, apply_discount_to=None, bill_cycle_day=None, bill_cycle_type=None, billing_period=None, billing_period_alignment=None, billing_timing=None, charge_model=None, charge_number=None, charge_type=None, charged_through_date=None, created_by_id=None, created_date=None, dmrc=None, dtcv=None, description=None, discount_level=None, effective_end_date=None, effective_start_date=None, end_date_condition=None, id=None, is_last_segment=None, list_price_base=None, mrr=None, name=None, number_of_periods=None, original_id=None, overage_calculation_option=None, overage_unused_units_credit_option=None, price_change_option=None, price_increase_percentage=None, processed_through_date=None, quantity=None, rate_plan_id=None, rating_group=None, rev_rec_code=None, rev_rec_trigger_condition=None, revenue_recognition_rule_name=None, rollover_balance=None, segment=None, specific_billing_period=None, specific_end_date=None, tcv=None, trigger_date=None, trigger_event=None, uom=None, up_to_periods=None, up_to_periods_type=None, updated_by_id=None, updated_date=None, version=None, weekly_bill_cycle_day=None, local_vars_configuration=None):  # noqa: E501
        """ProxyGetRatePlanChargeAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accounting_code = None
        self._apply_discount_to = None
        self._bill_cycle_day = None
        self._bill_cycle_type = None
        self._billing_period = None
        self._billing_period_alignment = None
        self._billing_timing = None
        self._charge_model = None
        self._charge_number = None
        self._charge_type = None
        self._charged_through_date = None
        self._created_by_id = None
        self._created_date = None
        self._dmrc = None
        self._dtcv = None
        self._description = None
        self._discount_level = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._end_date_condition = None
        self._id = None
        self._is_last_segment = None
        self._list_price_base = None
        self._mrr = None
        self._name = None
        self._number_of_periods = None
        self._original_id = None
        self._overage_calculation_option = None
        self._overage_unused_units_credit_option = None
        self._price_change_option = None
        self._price_increase_percentage = None
        self._processed_through_date = None
        self._quantity = None
        self._rate_plan_id = None
        self._rating_group = None
        self._rev_rec_code = None
        self._rev_rec_trigger_condition = None
        self._revenue_recognition_rule_name = None
        self._rollover_balance = None
        self._segment = None
        self._specific_billing_period = None
        self._specific_end_date = None
        self._tcv = None
        self._trigger_date = None
        self._trigger_event = None
        self._uom = None
        self._up_to_periods = None
        self._up_to_periods_type = None
        self._updated_by_id = None
        self._updated_date = None
        self._version = None
        self._weekly_bill_cycle_day = None
        self.discriminator = None

        if accounting_code is not None:
            self.accounting_code = accounting_code
        if apply_discount_to is not None:
            self.apply_discount_to = apply_discount_to
        if bill_cycle_day is not None:
            self.bill_cycle_day = bill_cycle_day
        if bill_cycle_type is not None:
            self.bill_cycle_type = bill_cycle_type
        if billing_period is not None:
            self.billing_period = billing_period
        if billing_period_alignment is not None:
            self.billing_period_alignment = billing_period_alignment
        if billing_timing is not None:
            self.billing_timing = billing_timing
        if charge_model is not None:
            self.charge_model = charge_model
        if charge_number is not None:
            self.charge_number = charge_number
        if charge_type is not None:
            self.charge_type = charge_type
        if charged_through_date is not None:
            self.charged_through_date = charged_through_date
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if dmrc is not None:
            self.dmrc = dmrc
        if dtcv is not None:
            self.dtcv = dtcv
        if description is not None:
            self.description = description
        if discount_level is not None:
            self.discount_level = discount_level
        if effective_end_date is not None:
            self.effective_end_date = effective_end_date
        if effective_start_date is not None:
            self.effective_start_date = effective_start_date
        if end_date_condition is not None:
            self.end_date_condition = end_date_condition
        if id is not None:
            self.id = id
        if is_last_segment is not None:
            self.is_last_segment = is_last_segment
        if list_price_base is not None:
            self.list_price_base = list_price_base
        if mrr is not None:
            self.mrr = mrr
        if name is not None:
            self.name = name
        if number_of_periods is not None:
            self.number_of_periods = number_of_periods
        if original_id is not None:
            self.original_id = original_id
        if overage_calculation_option is not None:
            self.overage_calculation_option = overage_calculation_option
        if overage_unused_units_credit_option is not None:
            self.overage_unused_units_credit_option = overage_unused_units_credit_option
        if price_change_option is not None:
            self.price_change_option = price_change_option
        if price_increase_percentage is not None:
            self.price_increase_percentage = price_increase_percentage
        if processed_through_date is not None:
            self.processed_through_date = processed_through_date
        if quantity is not None:
            self.quantity = quantity
        if rate_plan_id is not None:
            self.rate_plan_id = rate_plan_id
        if rating_group is not None:
            self.rating_group = rating_group
        if rev_rec_code is not None:
            self.rev_rec_code = rev_rec_code
        if rev_rec_trigger_condition is not None:
            self.rev_rec_trigger_condition = rev_rec_trigger_condition
        if revenue_recognition_rule_name is not None:
            self.revenue_recognition_rule_name = revenue_recognition_rule_name
        if rollover_balance is not None:
            self.rollover_balance = rollover_balance
        if segment is not None:
            self.segment = segment
        if specific_billing_period is not None:
            self.specific_billing_period = specific_billing_period
        if specific_end_date is not None:
            self.specific_end_date = specific_end_date
        if tcv is not None:
            self.tcv = tcv
        if trigger_date is not None:
            self.trigger_date = trigger_date
        if trigger_event is not None:
            self.trigger_event = trigger_event
        if uom is not None:
            self.uom = uom
        if up_to_periods is not None:
            self.up_to_periods = up_to_periods
        if up_to_periods_type is not None:
            self.up_to_periods_type = up_to_periods_type
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date
        if version is not None:
            self.version = version
        if weekly_bill_cycle_day is not None:
            self.weekly_bill_cycle_day = weekly_bill_cycle_day

    @property
    def accounting_code(self):
        """Gets the accounting_code of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        The accounting code for the charge. Accounting codes group transactions that contain similar accounting attributes.  **Character limit**: 100  **Values**: inherited from `ProductRatePlanCharge.AccountingCode`  **Note**: This value changes if `ProductRatePlanCharge.AccountingCode` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.AccountingCode` is updated.   # noqa: E501

        :return: The accounting_code of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """Sets the accounting_code of this ProxyGetRatePlanChargeAllOf.

        The accounting code for the charge. Accounting codes group transactions that contain similar accounting attributes.  **Character limit**: 100  **Values**: inherited from `ProductRatePlanCharge.AccountingCode`  **Note**: This value changes if `ProductRatePlanCharge.AccountingCode` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.AccountingCode` is updated.   # noqa: E501

        :param accounting_code: The accounting_code of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def apply_discount_to(self):
        """Gets the apply_discount_to of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies the type of charges a specific discount applies to. **Character limit**: 21 **Values**: inherited from `ProductRatePlanCharge.ApplyDiscountTo`   # noqa: E501

        :return: The apply_discount_to of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._apply_discount_to

    @apply_discount_to.setter
    def apply_discount_to(self, apply_discount_to):
        """Sets the apply_discount_to of this ProxyGetRatePlanChargeAllOf.

         Specifies the type of charges a specific discount applies to. **Character limit**: 21 **Values**: inherited from `ProductRatePlanCharge.ApplyDiscountTo`   # noqa: E501

        :param apply_discount_to: The apply_discount_to of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._apply_discount_to = apply_discount_to

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Indicates the charge's billing cycle day (BCD), which is when bill runs generate invoices for charges associated with the product rate plan charge or the account. **Character limit**: 2 **Values**: inherited from `ProductRatePlanCharge.BillCycleDay`   # noqa: E501

        :return: The bill_cycle_day of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this ProxyGetRatePlanChargeAllOf.

         Indicates the charge's billing cycle day (BCD), which is when bill runs generate invoices for charges associated with the product rate plan charge or the account. **Character limit**: 2 **Values**: inherited from `ProductRatePlanCharge.BillCycleDay`   # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: int
        """

        self._bill_cycle_day = bill_cycle_day

    @property
    def bill_cycle_type(self):
        """Gets the bill_cycle_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies how to determine the billing day for the charge. **Character limit**: 20 **Values**: inherited from `ProductRatePlanCharge.BillCycleType` **Note:** You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment.   # noqa: E501

        :return: The bill_cycle_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bill_cycle_type

    @bill_cycle_type.setter
    def bill_cycle_type(self, bill_cycle_type):
        """Sets the bill_cycle_type of this ProxyGetRatePlanChargeAllOf.

         Specifies how to determine the billing day for the charge. **Character limit**: 20 **Values**: inherited from `ProductRatePlanCharge.BillCycleType` **Note:** You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment.   # noqa: E501

        :param bill_cycle_type: The bill_cycle_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._bill_cycle_type = bill_cycle_type

    @property
    def billing_period(self):
        """Gets the billing_period of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Allows billing period to be overridden on rate plan charge. ****Values**: **inherited from `ProductRatePlanCharge.BillingPeriod` **Note:** You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment.   # noqa: E501

        :return: The billing_period of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this ProxyGetRatePlanChargeAllOf.

         Allows billing period to be overridden on rate plan charge. ****Values**: **inherited from `ProductRatePlanCharge.BillingPeriod` **Note:** You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment.   # noqa: E501

        :param billing_period: The billing_period of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._billing_period = billing_period

    @property
    def billing_period_alignment(self):
        """Gets the billing_period_alignment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Aligns charges within the same subscription if multiple charges begin on different dates. **Character limit**: 24 **Values**: inherited from `ProductRatePlanCharge.BillingPeriodAlignment`   # noqa: E501

        :return: The billing_period_alignment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._billing_period_alignment

    @billing_period_alignment.setter
    def billing_period_alignment(self, billing_period_alignment):
        """Sets the billing_period_alignment of this ProxyGetRatePlanChargeAllOf.

         Aligns charges within the same subscription if multiple charges begin on different dates. **Character limit**: 24 **Values**: inherited from `ProductRatePlanCharge.BillingPeriodAlignment`   # noqa: E501

        :param billing_period_alignment: The billing_period_alignment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._billing_period_alignment = billing_period_alignment

    @property
    def billing_timing(self):
        """Gets the billing_timing of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The billing timing for the charge. You can choose to bill in advance or in arrears for recurring charge types. This field is not used in one-time or usage based charge types. **Character limit**: **Values**: one of the following:  - `In Advance` - `In Arrears` **Note:** You can override the value inherited from the Product Rate Plan Charge when a subscription has a recurring charge type.    # noqa: E501

        :return: The billing_timing of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._billing_timing

    @billing_timing.setter
    def billing_timing(self, billing_timing):
        """Sets the billing_timing of this ProxyGetRatePlanChargeAllOf.

         The billing timing for the charge. You can choose to bill in advance or in arrears for recurring charge types. This field is not used in one-time or usage based charge types. **Character limit**: **Values**: one of the following:  - `In Advance` - `In Arrears` **Note:** You can override the value inherited from the Product Rate Plan Charge when a subscription has a recurring charge type.    # noqa: E501

        :param billing_timing: The billing_timing of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._billing_timing = billing_timing

    @property
    def charge_model(self):
        """Gets the charge_model of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Determines how to evaluate charges. Charge models must be individually activated in the web-based UI. **Character limit**: 29 **Values**: inherited from `ProductRatePlanCharge.ChargeModel`   # noqa: E501

        :return: The charge_model of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        """Sets the charge_model of this ProxyGetRatePlanChargeAllOf.

         Determines how to evaluate charges. Charge models must be individually activated in the web-based UI. **Character limit**: 29 **Values**: inherited from `ProductRatePlanCharge.ChargeModel`   # noqa: E501

        :param charge_model: The charge_model of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._charge_model = charge_model

    @property
    def charge_number(self):
        """Gets the charge_number of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         A unique number that identifies the charge. This number is returned as a string. **Character limit**: 50 **Values**: one of the following:  - automatically generated if left null - a unique number of 50 characters or fewer   # noqa: E501

        :return: The charge_number of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this ProxyGetRatePlanChargeAllOf.

         A unique number that identifies the charge. This number is returned as a string. **Character limit**: 50 **Values**: one of the following:  - automatically generated if left null - a unique number of 50 characters or fewer   # noqa: E501

        :param charge_number: The charge_number of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def charge_type(self):
        """Gets the charge_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies the type of charge. **Character limit**: 9 **Values**: inherited from `ProductRatePlanCharge.ChargeType`   # noqa: E501

        :return: The charge_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this ProxyGetRatePlanChargeAllOf.

         Specifies the type of charge. **Character limit**: 9 **Values**: inherited from `ProductRatePlanCharge.ChargeType`   # noqa: E501

        :param charge_type: The charge_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def charged_through_date(self):
        """Gets the charged_through_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date through which a customer has been billed for the charge. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The charged_through_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._charged_through_date

    @charged_through_date.setter
    def charged_through_date(self, charged_through_date):
        """Sets the charged_through_date of this ProxyGetRatePlanChargeAllOf.

         The date through which a customer has been billed for the charge. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param charged_through_date: The charged_through_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: date
        """

        self._charged_through_date = charged_through_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        The ID of the Zuora user who created the `RatePlanCharge` object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetRatePlanChargeAllOf.

        The ID of the Zuora user who created the `RatePlanCharge` object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date when the `RatePlanCharge` object was created. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The created_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetRatePlanChargeAllOf.

         The date when the `RatePlanCharge` object was created. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def dmrc(self):
        """Gets the dmrc of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        A delta monthly recurring charge is the change in monthly recurring revenue caused by an amendment or a new subscription. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The dmrc of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._dmrc

    @dmrc.setter
    def dmrc(self, dmrc):
        """Sets the dmrc of this ProxyGetRatePlanChargeAllOf.

        A delta monthly recurring charge is the change in monthly recurring revenue caused by an amendment or a new subscription. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param dmrc: The dmrc of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._dmrc = dmrc

    @property
    def dtcv(self):
        """Gets the dtcv of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         After an Amendment, the change in the total contract value (TCV) amount for this charge, compared with its previous value. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The dtcv of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._dtcv

    @dtcv.setter
    def dtcv(self, dtcv):
        """Sets the dtcv of this ProxyGetRatePlanChargeAllOf.

         After an Amendment, the change in the total contract value (TCV) amount for this charge, compared with its previous value. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param dtcv: The dtcv of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._dtcv = dtcv

    @property
    def description(self):
        """Gets the description of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         A description of the charge. **Character limit**: 500 **Values**: inherited from `ProductRatePlanCharge.Description`   # noqa: E501

        :return: The description of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyGetRatePlanChargeAllOf.

         A description of the charge. **Character limit**: 500 **Values**: inherited from `ProductRatePlanCharge.Description`   # noqa: E501

        :param description: The description of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discount_level(self):
        """Gets the discount_level of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Specifies if the discount applies to just the product rate plan, the entire subscription, or to any activity in the account. **Character limit**: 12 **Values**: inherited from `ProductRatePlanCharge.DiscountLevel`   # noqa: E501

        :return: The discount_level of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._discount_level

    @discount_level.setter
    def discount_level(self, discount_level):
        """Sets the discount_level of this ProxyGetRatePlanChargeAllOf.

        Specifies if the discount applies to just the product rate plan, the entire subscription, or to any activity in the account. **Character limit**: 12 **Values**: inherited from `ProductRatePlanCharge.DiscountLevel`   # noqa: E501

        :param discount_level: The discount_level of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._discount_level = discount_level

    @property
    def effective_end_date(self):
        """Gets the effective_end_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date when the segmented charge ends or ended. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The effective_end_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, effective_end_date):
        """Sets the effective_end_date of this ProxyGetRatePlanChargeAllOf.

         The date when the segmented charge ends or ended. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param effective_end_date: The effective_end_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: date
        """

        self._effective_end_date = effective_end_date

    @property
    def effective_start_date(self):
        """Gets the effective_start_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date when the segmented charge starts or started. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The effective_start_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, effective_start_date):
        """Sets the effective_start_date of this ProxyGetRatePlanChargeAllOf.

         The date when the segmented charge starts or started. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param effective_start_date: The effective_start_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: date
        """

        self._effective_start_date = effective_start_date

    @property
    def end_date_condition(self):
        """Gets the end_date_condition of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Defines when the charge ends after the charge trigger date. This field can be updated when **Status** is `Draft`. **Values**: one of the following:  - `SubscriptionEnd`: The charge ends on the subscription end date after the charge trigger date. This is the default value. - `FixedPeriod`: The charge ends after a specified period based on the trigger date of the charge. If you set this field to `FixedPeriod`, you must specify the length of the period and a period type by defining the `UpToPeriods` and `UpToPeriodsType` fields. - `SpecificEndDate`: The specific date on which the charge ends. If you set this field to `SpecificEndDate`, you must specify the specific date by defining the `SpecificEndDate` field.  **Note**: If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.   # noqa: E501

        :return: The end_date_condition of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._end_date_condition

    @end_date_condition.setter
    def end_date_condition(self, end_date_condition):
        """Sets the end_date_condition of this ProxyGetRatePlanChargeAllOf.

         Defines when the charge ends after the charge trigger date. This field can be updated when **Status** is `Draft`. **Values**: one of the following:  - `SubscriptionEnd`: The charge ends on the subscription end date after the charge trigger date. This is the default value. - `FixedPeriod`: The charge ends after a specified period based on the trigger date of the charge. If you set this field to `FixedPeriod`, you must specify the length of the period and a period type by defining the `UpToPeriods` and `UpToPeriodsType` fields. - `SpecificEndDate`: The specific date on which the charge ends. If you set this field to `SpecificEndDate`, you must specify the specific date by defining the `SpecificEndDate` field.  **Note**: If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.   # noqa: E501

        :param end_date_condition: The end_date_condition of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._end_date_condition = end_date_condition

    @property
    def id(self):
        """Gets the id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetRatePlanChargeAllOf.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_last_segment(self):
        """Gets the is_last_segment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Indicates if the segment of the rate plan charge is the most recent segment. **Character limit**: 5 **Values**: automatically generated: `true`, `false`   # noqa: E501

        :return: The is_last_segment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_last_segment

    @is_last_segment.setter
    def is_last_segment(self, is_last_segment):
        """Sets the is_last_segment of this ProxyGetRatePlanChargeAllOf.

        Indicates if the segment of the rate plan charge is the most recent segment. **Character limit**: 5 **Values**: automatically generated: `true`, `false`   # noqa: E501

        :param is_last_segment: The is_last_segment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: bool
        """

        self._is_last_segment = is_last_segment

    @property
    def list_price_base(self):
        """Gets the list_price_base of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        The list price base for the product rate plan charge. **Values**: one of the following:  - `Per Month` - `Per Billing Period` - `Per Week`   # noqa: E501

        :return: The list_price_base of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._list_price_base

    @list_price_base.setter
    def list_price_base(self, list_price_base):
        """Sets the list_price_base of this ProxyGetRatePlanChargeAllOf.

        The list price base for the product rate plan charge. **Values**: one of the following:  - `Per Month` - `Per Billing Period` - `Per Week`   # noqa: E501

        :param list_price_base: The list_price_base of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._list_price_base = list_price_base

    @property
    def mrr(self):
        """Gets the mrr of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Monthly recurring revenue (MRR) is the amount of recurring charges in a given month. The MRR calculation doesn't include one-time charges nor usage charges. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The mrr of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._mrr

    @mrr.setter
    def mrr(self, mrr):
        """Sets the mrr of this ProxyGetRatePlanChargeAllOf.

        Monthly recurring revenue (MRR) is the amount of recurring charges in a given month. The MRR calculation doesn't include one-time charges nor usage charges. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param mrr: The mrr of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._mrr = mrr

    @property
    def name(self):
        """Gets the name of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        The name of the rate plan charge. **Character limit**: 100 **Values**: automatically generated   # noqa: E501

        :return: The name of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyGetRatePlanChargeAllOf.

        The name of the rate plan charge. **Character limit**: 100 **Values**: automatically generated   # noqa: E501

        :param name: The name of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_of_periods(self):
        """Gets the number_of_periods of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Specifies the number of periods to use when calculating charges in an overage smoothing charge model. **Character limit**: 5 **Values**: inherited from `ProductRatePlanCharge.NumberOfPeriod`   # noqa: E501

        :return: The number_of_periods of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._number_of_periods

    @number_of_periods.setter
    def number_of_periods(self, number_of_periods):
        """Sets the number_of_periods of this ProxyGetRatePlanChargeAllOf.

        Specifies the number of periods to use when calculating charges in an overage smoothing charge model. **Character limit**: 5 **Values**: inherited from `ProductRatePlanCharge.NumberOfPeriod`   # noqa: E501

        :param number_of_periods: The number_of_periods of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: int
        """

        self._number_of_periods = number_of_periods

    @property
    def original_id(self):
        """Gets the original_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        The original ID of the rate plan charge. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The original_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._original_id

    @original_id.setter
    def original_id(self, original_id):
        """Sets the original_id of this ProxyGetRatePlanChargeAllOf.

        The original ID of the rate plan charge. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param original_id: The original_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._original_id = original_id

    @property
    def overage_calculation_option(self):
        """Gets the overage_calculation_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Determines when to calculate overage charges. If the value of the SmoothingMode field is null (not specified and not inherited from ProductRatePlanCharge.SmoothingMode), the value of this field is ignored. **Character limit**: 20 **Values**: inherited from `ProductRatePlanCharge.OverageCalculationOption`   # noqa: E501

        :return: The overage_calculation_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._overage_calculation_option

    @overage_calculation_option.setter
    def overage_calculation_option(self, overage_calculation_option):
        """Sets the overage_calculation_option of this ProxyGetRatePlanChargeAllOf.

        Determines when to calculate overage charges. If the value of the SmoothingMode field is null (not specified and not inherited from ProductRatePlanCharge.SmoothingMode), the value of this field is ignored. **Character limit**: 20 **Values**: inherited from `ProductRatePlanCharge.OverageCalculationOption`   # noqa: E501

        :param overage_calculation_option: The overage_calculation_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._overage_calculation_option = overage_calculation_option

    @property
    def overage_unused_units_credit_option(self):
        """Gets the overage_unused_units_credit_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Determines whether to credit the customer with unused units of usage. **Character limit**: 20 **Values**: inherited from `ProductRatePlanCharge.OverageUnusedUnitsCreditOption`   # noqa: E501

        :return: The overage_unused_units_credit_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._overage_unused_units_credit_option

    @overage_unused_units_credit_option.setter
    def overage_unused_units_credit_option(self, overage_unused_units_credit_option):
        """Sets the overage_unused_units_credit_option of this ProxyGetRatePlanChargeAllOf.

         Determines whether to credit the customer with unused units of usage. **Character limit**: 20 **Values**: inherited from `ProductRatePlanCharge.OverageUnusedUnitsCreditOption`   # noqa: E501

        :param overage_unused_units_credit_option: The overage_unused_units_credit_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._overage_unused_units_credit_option = overage_unused_units_credit_option

    @property
    def price_change_option(self):
        """Gets the price_change_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Applies an automatic price change when a termed subscription is renewed. **Character limit**: **Values**: one of the following:  - `NoChange` (default) - `SpecificPercentageValue` - `UseLatestProductCatalogPricing`   # noqa: E501

        :return: The price_change_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._price_change_option

    @price_change_option.setter
    def price_change_option(self, price_change_option):
        """Sets the price_change_option of this ProxyGetRatePlanChargeAllOf.

         Applies an automatic price change when a termed subscription is renewed. **Character limit**: **Values**: one of the following:  - `NoChange` (default) - `SpecificPercentageValue` - `UseLatestProductCatalogPricing`   # noqa: E501

        :param price_change_option: The price_change_option of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._price_change_option = price_change_option

    @property
    def price_increase_percentage(self):
        """Gets the price_increase_percentage of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies the percentage to increase or decrease the price of renewed subscriptions. **Character limit**: 16 **Values**: a decimal value between -100 and 100   # noqa: E501

        :return: The price_increase_percentage of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._price_increase_percentage

    @price_increase_percentage.setter
    def price_increase_percentage(self, price_increase_percentage):
        """Sets the price_increase_percentage of this ProxyGetRatePlanChargeAllOf.

         Specifies the percentage to increase or decrease the price of renewed subscriptions. **Character limit**: 16 **Values**: a decimal value between -100 and 100   # noqa: E501

        :param price_increase_percentage: The price_increase_percentage of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._price_increase_percentage = price_increase_percentage

    @property
    def processed_through_date(self):
        """Gets the processed_through_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date until when charges have been processed. When billing in arrears, such as usage, this field value is the the same as the `ChargedThroughDate` value. This date is the earliest date when a charge can be amended. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The processed_through_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._processed_through_date

    @processed_through_date.setter
    def processed_through_date(self, processed_through_date):
        """Sets the processed_through_date of this ProxyGetRatePlanChargeAllOf.

         The date until when charges have been processed. When billing in arrears, such as usage, this field value is the the same as the `ChargedThroughDate` value. This date is the earliest date when a charge can be amended. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param processed_through_date: The processed_through_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: date
        """

        self._processed_through_date = processed_through_date

    @property
    def quantity(self):
        """Gets the quantity of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The default quantity of units, such as the number of authors in a hosted wiki service. Valid for all charge models except for Flat Fee pricing. **Character limit**: 16 **Values**: a valid quantity value   # noqa: E501

        :return: The quantity of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ProxyGetRatePlanChargeAllOf.

         The default quantity of units, such as the number of authors in a hosted wiki service. Valid for all charge models except for Flat Fee pricing. **Character limit**: 16 **Values**: a valid quantity value   # noqa: E501

        :param quantity: The quantity of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def rate_plan_id(self):
        """Gets the rate_plan_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The ID of the rate plan associated with the rate plan charge. **Character limit**: 32 **Values**: inherited from `RatePlan.Id`   # noqa: E501

        :return: The rate_plan_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_id

    @rate_plan_id.setter
    def rate_plan_id(self, rate_plan_id):
        """Sets the rate_plan_id of this ProxyGetRatePlanChargeAllOf.

         The ID of the rate plan associated with the rate plan charge. **Character limit**: 32 **Values**: inherited from `RatePlan.Id`   # noqa: E501

        :param rate_plan_id: The rate_plan_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._rate_plan_id = rate_plan_id

    @property
    def rating_group(self):
        """Gets the rating_group of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        A rating group based on which usage records are rated. Only applicable to Usage charges.  Possible values:  - `ByBillingPeriod`: The rating is based on all the usages in a billing period. - `ByUsageStartDate`: The rating is based on all the usages on the same usage start date.  - `ByUsageRecord`: The rating is based on each usage record. - `ByUsageUpload`: The rating is based on all the  usages in a uploaded usage file (`.xls` or `.csv`). - `ByGroupId`: The rating is based on all the usages in a custom group.  For more information, see [Usage rating by group](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Usage/Usage_Rating_by_Group).   # noqa: E501

        :return: The rating_group of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rating_group

    @rating_group.setter
    def rating_group(self, rating_group):
        """Sets the rating_group of this ProxyGetRatePlanChargeAllOf.

        A rating group based on which usage records are rated. Only applicable to Usage charges.  Possible values:  - `ByBillingPeriod`: The rating is based on all the usages in a billing period. - `ByUsageStartDate`: The rating is based on all the usages on the same usage start date.  - `ByUsageRecord`: The rating is based on each usage record. - `ByUsageUpload`: The rating is based on all the  usages in a uploaded usage file (`.xls` or `.csv`). - `ByGroupId`: The rating is based on all the usages in a custom group.  For more information, see [Usage rating by group](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/J_Billing_Operations/Usage/Usage_Rating_by_Group).   # noqa: E501

        :param rating_group: The rating_group of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["ByBillingPeriod", "ByUsageStartDate", "ByUsageRecord", "ByUsageUpload", "ByGroupId"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rating_group not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rating_group` ({0}), must be one of {1}"  # noqa: E501
                .format(rating_group, allowed_values)
            )

        self._rating_group = rating_group

    @property
    def rev_rec_code(self):
        """Gets the rev_rec_code of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Associates this product rate plan charge with a specific revenue recognition code.  **Character limit**: 70  **Values**: inherited from `ProductRatePlanCharge.RevRecCode` or a valid revenue recognition code  **Note**: Unless overridden, this value changes if `ProductRatePlanCharge.RevRecCode` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.RevRecCode` is updated.   # noqa: E501

        :return: The rev_rec_code of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_code

    @rev_rec_code.setter
    def rev_rec_code(self, rev_rec_code):
        """Sets the rev_rec_code of this ProxyGetRatePlanChargeAllOf.

         Associates this product rate plan charge with a specific revenue recognition code.  **Character limit**: 70  **Values**: inherited from `ProductRatePlanCharge.RevRecCode` or a valid revenue recognition code  **Note**: Unless overridden, this value changes if `ProductRatePlanCharge.RevRecCode` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.RevRecCode` is updated.   # noqa: E501

        :param rev_rec_code: The rev_rec_code of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._rev_rec_code = rev_rec_code

    @property
    def rev_rec_trigger_condition(self):
        """Gets the rev_rec_trigger_condition of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies when revenue recognition begins.  **Character limit**: 22  **Values**: inherited from `ProductRatePlanCharge.RevRecTriggerCondition` or one of the following:  -  `ContractEffectiveDate`  -  `ServiceActivationDate`  -  `CustomerAcceptanceDate`  Note: Unless overridden, this value changes if `ProductRatePlanCharge.RevRecTriggerCondition` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.RevRecTriggerCondition` is updated.   # noqa: E501

        :return: The rev_rec_trigger_condition of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_trigger_condition

    @rev_rec_trigger_condition.setter
    def rev_rec_trigger_condition(self, rev_rec_trigger_condition):
        """Sets the rev_rec_trigger_condition of this ProxyGetRatePlanChargeAllOf.

         Specifies when revenue recognition begins.  **Character limit**: 22  **Values**: inherited from `ProductRatePlanCharge.RevRecTriggerCondition` or one of the following:  -  `ContractEffectiveDate`  -  `ServiceActivationDate`  -  `CustomerAcceptanceDate`  Note: Unless overridden, this value changes if `ProductRatePlanCharge.RevRecTriggerCondition` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.RevRecTriggerCondition` is updated.   # noqa: E501

        :param rev_rec_trigger_condition: The rev_rec_trigger_condition of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._rev_rec_trigger_condition = rev_rec_trigger_condition

    @property
    def revenue_recognition_rule_name(self):
        """Gets the revenue_recognition_rule_name of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies the Revenue Recognition Rule that you want the Rate Plan Charge to use. This field can be updated when **Status** is `Draft`. By default, the Revenue Recognition Rule is inherited from the Product Rate Plan Charge. For Amend calls, you can use this field only for NewProduct amendments. For Update calls, you can use this field only to update subscriptions in draft status. Note that if you use this field to specify a Revenue Recognition Rule for the Rate Plan Charge, the rule will remain as specified even if you later change the rule used by the corresponding Product Rate Plan Charge.  **Character limit**: n/a  **Values**: inherited from `ProductRatePlanCharge.RevenueRecognitionRuleName` or the name of an active Revenue Recognition Rule  **Note**: Unless overridden, this value changes if `ProductRatePlanCharge.RevenueRecognitionRuleName` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.RevenueRecognitionRuleName` is updated.   # noqa: E501

        :return: The revenue_recognition_rule_name of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._revenue_recognition_rule_name

    @revenue_recognition_rule_name.setter
    def revenue_recognition_rule_name(self, revenue_recognition_rule_name):
        """Sets the revenue_recognition_rule_name of this ProxyGetRatePlanChargeAllOf.

         Specifies the Revenue Recognition Rule that you want the Rate Plan Charge to use. This field can be updated when **Status** is `Draft`. By default, the Revenue Recognition Rule is inherited from the Product Rate Plan Charge. For Amend calls, you can use this field only for NewProduct amendments. For Update calls, you can use this field only to update subscriptions in draft status. Note that if you use this field to specify a Revenue Recognition Rule for the Rate Plan Charge, the rule will remain as specified even if you later change the rule used by the corresponding Product Rate Plan Charge.  **Character limit**: n/a  **Values**: inherited from `ProductRatePlanCharge.RevenueRecognitionRuleName` or the name of an active Revenue Recognition Rule  **Note**: Unless overridden, this value changes if `ProductRatePlanCharge.RevenueRecognitionRuleName` is updated. The values of `UpdatedById` and `UpdatedDate` for the `RatePlanCharge` do not change when `ProductRatePlanCharge.RevenueRecognitionRuleName` is updated.   # noqa: E501

        :param revenue_recognition_rule_name: The revenue_recognition_rule_name of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._revenue_recognition_rule_name = revenue_recognition_rule_name

    @property
    def rollover_balance(self):
        """Gets the rollover_balance of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        Specifies the number of units of measure (UOM) rolled over from previous periods. The value of this field is the rollover balance for the corresponding account.  This field is applicable only to usage charges with overage models.  **Note**:  - You cannot query or filter this field with other fields in a single query. - To query or filter this field, you must specify and only specify the rate plan charge Id in the condition. - You cannot use this field in the query or filter condition.   # noqa: E501

        :return: The rollover_balance of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._rollover_balance

    @rollover_balance.setter
    def rollover_balance(self, rollover_balance):
        """Sets the rollover_balance of this ProxyGetRatePlanChargeAllOf.

        Specifies the number of units of measure (UOM) rolled over from previous periods. The value of this field is the rollover balance for the corresponding account.  This field is applicable only to usage charges with overage models.  **Note**:  - You cannot query or filter this field with other fields in a single query. - To query or filter this field, you must specify and only specify the rate plan charge Id in the condition. - You cannot use this field in the query or filter condition.   # noqa: E501

        :param rollover_balance: The rollover_balance of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._rollover_balance = rollover_balance

    @property
    def segment(self):
        """Gets the segment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The identifying number of the subscription rate plan segment. Segments are numbered sequentially, starting with 1. **Character limit**: 2 **Values**: automatically generated   # noqa: E501

        :return: The segment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this ProxyGetRatePlanChargeAllOf.

         The identifying number of the subscription rate plan segment. Segments are numbered sequentially, starting with 1. **Character limit**: 2 **Values**: automatically generated   # noqa: E501

        :param segment: The segment of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: int
        """

        self._segment = segment

    @property
    def specific_billing_period(self):
        """Gets the specific_billing_period of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Customizes the number of months or weeks for the charges billing period. This field is required if you set the value of the BillingPeriod field to `Specific Months` or `Specific Weeks`. **Character limit**: 5 **Values**: inherited from `ProductRatePlanCharge.BillingPeriod` **Note:** You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment.   # noqa: E501

        :return: The specific_billing_period of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._specific_billing_period

    @specific_billing_period.setter
    def specific_billing_period(self, specific_billing_period):
        """Sets the specific_billing_period of this ProxyGetRatePlanChargeAllOf.

         Customizes the number of months or weeks for the charges billing period. This field is required if you set the value of the BillingPeriod field to `Specific Months` or `Specific Weeks`. **Character limit**: 5 **Values**: inherited from `ProductRatePlanCharge.BillingPeriod` **Note:** You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment.   # noqa: E501

        :param specific_billing_period: The specific_billing_period of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: int
        """

        self._specific_billing_period = specific_billing_period

    @property
    def specific_end_date(self):
        """Gets the specific_end_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The specific date on which the charge ends, in `yyyy-mm-dd` format. **Character limit**: 29 **Note**:  - This field is only applicable when the `EndDateCondition` field is set to `SpecificEndDate`. - If the subscription ends before the specific end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the specific end date.   # noqa: E501

        :return: The specific_end_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._specific_end_date

    @specific_end_date.setter
    def specific_end_date(self, specific_end_date):
        """Sets the specific_end_date of this ProxyGetRatePlanChargeAllOf.

         The specific date on which the charge ends, in `yyyy-mm-dd` format. **Character limit**: 29 **Note**:  - This field is only applicable when the `EndDateCondition` field is set to `SpecificEndDate`. - If the subscription ends before the specific end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the specific end date.   # noqa: E501

        :param specific_end_date: The specific_end_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: date
        """

        self._specific_end_date = specific_end_date

    @property
    def tcv(self):
        """Gets the tcv of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The total contract value (TCV) is the value of a single rate plan charge in a subscription over the lifetime of the subscription. This value does not represent all charges on the subscription. The TCV includes recurring charges and one-time charges, but it doesn't include usage charge. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The tcv of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: float
        """
        return self._tcv

    @tcv.setter
    def tcv(self, tcv):
        """Sets the tcv of this ProxyGetRatePlanChargeAllOf.

         The total contract value (TCV) is the value of a single rate plan charge in a subscription over the lifetime of the subscription. This value does not represent all charges on the subscription. The TCV includes recurring charges and one-time charges, but it doesn't include usage charge. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param tcv: The tcv of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: float
        """

        self._tcv = tcv

    @property
    def trigger_date(self):
        """Gets the trigger_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date when the charge becomes effective and billing begins, in `yyyy-mm-dd` format. This field is required if the `TriggerEvent` field value is `SpecificDate`. **Character limit**: 29   # noqa: E501

        :return: The trigger_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: date
        """
        return self._trigger_date

    @trigger_date.setter
    def trigger_date(self, trigger_date):
        """Sets the trigger_date of this ProxyGetRatePlanChargeAllOf.

         The date when the charge becomes effective and billing begins, in `yyyy-mm-dd` format. This field is required if the `TriggerEvent` field value is `SpecificDate`. **Character limit**: 29   # noqa: E501

        :param trigger_date: The trigger_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: date
        """

        self._trigger_date = trigger_date

    @property
    def trigger_event(self):
        """Gets the trigger_event of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies when to start billing the customer for the charge. **Note: **This field can be passed through the Subscribe and Amend calls and will override the default value set on the Product Rate Plan Charge. **Character limit**: 18 **Values**: inherited from `ProductRatePlanCharge.TriggerEvent` and can be one of the following values:  - `ContractEffective` is the date when the subscription's contract goes into effect and the charge is ready to be billed. - `ServiceActivation` is when the services or products for a subscription have been activated and the customers have access. - `CustomerAcceptance` is when the customer accepts the services or products for a subscription. - `SpecificDate` is valid only on the RatePlanCharge.   # noqa: E501

        :return: The trigger_event of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._trigger_event

    @trigger_event.setter
    def trigger_event(self, trigger_event):
        """Sets the trigger_event of this ProxyGetRatePlanChargeAllOf.

         Specifies when to start billing the customer for the charge. **Note: **This field can be passed through the Subscribe and Amend calls and will override the default value set on the Product Rate Plan Charge. **Character limit**: 18 **Values**: inherited from `ProductRatePlanCharge.TriggerEvent` and can be one of the following values:  - `ContractEffective` is the date when the subscription's contract goes into effect and the charge is ready to be billed. - `ServiceActivation` is when the services or products for a subscription have been activated and the customers have access. - `CustomerAcceptance` is when the customer accepts the services or products for a subscription. - `SpecificDate` is valid only on the RatePlanCharge.   # noqa: E501

        :param trigger_event: The trigger_event of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._trigger_event = trigger_event

    @property
    def uom(self):
        """Gets the uom of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies the units to measure usage. **Character limit**: 25 **Values**: inherited from `ProductRatePlanCharge.UOM`   # noqa: E501

        :return: The uom of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """Sets the uom of this ProxyGetRatePlanChargeAllOf.

         Specifies the units to measure usage. **Character limit**: 25 **Values**: inherited from `ProductRatePlanCharge.UOM`   # noqa: E501

        :param uom: The uom of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._uom = uom

    @property
    def up_to_periods(self):
        """Gets the up_to_periods of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends. **Character limit**: 5 **Values**: inherited from `ProductRatePlanCharge.UpToPeriods` **Note**:  - You must use this field together with the `UpToPeriodsType` field to specify the time period. This field is only applicable only when the `EndDateCondition` field is set to `FixedPeriod`. - You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment. - Use this field to override the value in `ProductRatePlanCharge.UpToPeriod`. - If you override the value in this field, enter a whole number between 0 and 65535, exclusive. - If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.   # noqa: E501

        :return: The up_to_periods of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._up_to_periods

    @up_to_periods.setter
    def up_to_periods(self, up_to_periods):
        """Sets the up_to_periods of this ProxyGetRatePlanChargeAllOf.

         Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends. **Character limit**: 5 **Values**: inherited from `ProductRatePlanCharge.UpToPeriods` **Note**:  - You must use this field together with the `UpToPeriodsType` field to specify the time period. This field is only applicable only when the `EndDateCondition` field is set to `FixedPeriod`. - You can override the value inherited from the Product Rate Plan Charge, but only when creating a new subscription or a New Product amendment. - Use this field to override the value in `ProductRatePlanCharge.UpToPeriod`. - If you override the value in this field, enter a whole number between 0 and 65535, exclusive. - If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.   # noqa: E501

        :param up_to_periods: The up_to_periods of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: int
        """

        self._up_to_periods = up_to_periods

    @property
    def up_to_periods_type(self):
        """Gets the up_to_periods_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The period type used to define when the charge ends. This field can be updated when **Status** is `Draft`. **Values**: one of the following:  - `Billing Periods` (default) - `Days` - `Weeks` - `Months` - `Years` **Note**:  - You must use this field together with the `UpToPeriods` field to specify the time period. - This field is only applicable only when the `EndDateCondition` field is set to `FixedPeriod`.   # noqa: E501

        :return: The up_to_periods_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._up_to_periods_type

    @up_to_periods_type.setter
    def up_to_periods_type(self, up_to_periods_type):
        """Sets the up_to_periods_type of this ProxyGetRatePlanChargeAllOf.

         The period type used to define when the charge ends. This field can be updated when **Status** is `Draft`. **Values**: one of the following:  - `Billing Periods` (default) - `Days` - `Weeks` - `Months` - `Years` **Note**:  - You must use this field together with the `UpToPeriods` field to specify the time period. - This field is only applicable only when the `EndDateCondition` field is set to `FixedPeriod`.   # noqa: E501

        :param up_to_periods_type: The up_to_periods_type of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._up_to_periods_type = up_to_periods_type

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

        The ID of the last user to update the object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The updated_by_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetRatePlanChargeAllOf.

        The ID of the last user to update the object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The date when the object was last updated. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetRatePlanChargeAllOf.

         The date when the object was last updated. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    @property
    def version(self):
        """Gets the version of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         The version of the rate plan charge. Each time a charge is amended, Zuora creates a new version of the rate plan charge. **Character limit**: 5 **Values**: automatically generated   # noqa: E501

        :return: The version of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProxyGetRatePlanChargeAllOf.

         The version of the rate plan charge. Each time a charge is amended, Zuora creates a new version of the rate plan charge. **Character limit**: 5 **Values**: automatically generated   # noqa: E501

        :param version: The version of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def weekly_bill_cycle_day(self):
        """Gets the weekly_bill_cycle_day of this ProxyGetRatePlanChargeAllOf.  # noqa: E501

         Specifies which day of the week as the bill cycle day (BCD) for the charge. This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  **Values**: one of the following:  - `Sunday` - `Monday` - `Tuesday` - `Wednesday` - `Thursday` - `Friday` - `Saturday`   # noqa: E501

        :return: The weekly_bill_cycle_day of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._weekly_bill_cycle_day

    @weekly_bill_cycle_day.setter
    def weekly_bill_cycle_day(self, weekly_bill_cycle_day):
        """Sets the weekly_bill_cycle_day of this ProxyGetRatePlanChargeAllOf.

         Specifies which day of the week as the bill cycle day (BCD) for the charge. This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  **Values**: one of the following:  - `Sunday` - `Monday` - `Tuesday` - `Wednesday` - `Thursday` - `Friday` - `Saturday`   # noqa: E501

        :param weekly_bill_cycle_day: The weekly_bill_cycle_day of this ProxyGetRatePlanChargeAllOf.  # noqa: E501
        :type: str
        """

        self._weekly_bill_cycle_day = weekly_bill_cycle_day

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
        if not isinstance(other, ProxyGetRatePlanChargeAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProxyGetRatePlanChargeAllOf):
            return True

        return self.to_dict() != other.to_dict()
