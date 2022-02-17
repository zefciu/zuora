# CreatePaymentTypeAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account that the payment is created for.  | [optional] 
**account_number** | **str** | The number of the customer account that the payment is created for, such as &#x60;A00000001&#x60;.  You can specify either &#x60;accountNumber&#x60; or &#x60;accountId&#x60; for a customer account. If both of them are specified, they must refer to the same customer account.  | [optional] 
**amount** | **float** | The total amount of the payment.  | 
**auth_transaction_id** | **str** | The authorization transaction ID from the payment gateway. Use this field for electronic payments, such as credit cards.  When you create a payment for capturing the authorized funds, it is highly recommended to pass in the gatewayOrderId that you used when authorizing the funds by using the [Create authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CreateAuthorization) operation, together with the &#x60;authTransactionId&#x60; field.  The following payment gateways support this field:   - Adyen Integration v2.0   - CyberSource 1.28   - CyberSource 1.97   - CyberSource 2.0   - Chase Paymentech Orbital   - Ingenico ePayments   - SlimPay   - Verifi Global Payment Gateway   - WePay Payment Gateway Integration  | [optional] 
**comment** | **str** | Additional information related to the payment.  | [optional] 
**currency** | **str** | When Standalone Payment is not enabled, the &#x60;currency&#x60; of the payment must be the same as the payment currency defined in the customer account settings through Zuora UI.  When Standalone Payment is enabled and &#x60;standalone&#x60; is &#x60;true&#x60;, the &#x60;currency&#x60; of the standalone payment can be different from the payment currency defined in the customer account settings. The amount will not be summed up to the account balance or key metrics regardless of currency.  | 
**debit_memos** | [**list[PaymentDebitMemoApplicationCreateRequestType]**](PaymentDebitMemoApplicationCreateRequestType.md) | Container for debit memos. The maximum number of debit memos is 1,000.  | [optional] 
**effective_date** | **date** | The date when the payment takes effect, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**finance_information** | [**CreatePaymentTypeAllOfFinanceInformation**](CreatePaymentTypeAllOfFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the payment. The ID must be a valid gateway instance ID and this gateway must support the specific payment method.   - When creating electronic payments, this field is required.  - When creating external payments, this field is optional.  | [optional] 
**gateway_options** | [**CreatePaymentTypeAllOfGatewayOptions**](CreatePaymentTypeAllOfGatewayOptions.md) |  | [optional] 
**gateway_order_id** | **str** | A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created. If not specified, the payment number will be passed in instead.  Gateways check duplicates on the gateway order ID to ensure that the merchant do not accidentally enter the same transaction twice. This ID can also be used to do reconciliation and tie the payment to a natural key in external systems. The source of this ID varies by merchant. Some merchants use their shopping cart order IDs, and others use something different. Merchants use this ID to track transactions in their eCommerce systems.  When you create a payment for capturing the authorized funds, it is highly recommended to pass in the gatewayOrderId that you used when authorizing the funds by using the [Create authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CreateAuthorization) operation, together with the &#x60;authTransactionId&#x60; field.  | [optional] 
**invoices** | [**list[PaymentInvoiceApplicationCreateRequestType]**](PaymentInvoiceApplicationCreateRequestType.md) | Container for invoices. The maximum number of invoices is 1,000.  | [optional] 
**mit_transaction_source** | **str** | Payment transaction source used to differentiate the transaction source in Stored Credential Transaction framework.   - &#x60;C_Unscheduled&#x60;: Cardholder-initiated transaction (CIT) that does not occur on scheduled or regularly occurring dates.   - &#x60;M_Recurring&#x60;: Merchant-initiated transaction (MIT) that occurs at regular intervals.   - &#x60;M_Unscheduled&#x60;: Merchant-initiated transaction (MIT) that does not occur on scheduled or regularly occurring dates.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the payment.   If no payment method ID is specified in the request body, the default payment method for the customer account is used automatically. If the default payment method is different from the type of payments that you want to create, an error occurs.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi. | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi. | [optional] 
**standalone** | **bool** | This field is only available if support for standalone payments is enabled.  Specify &#x60;true&#x60; to create a standalone payment that will be processed in Zuora through Zuora gateway integration but will be settled outside of Zuora.  When &#x60;standalone&#x60; is set to &#x60;true&#x60;:   - &#x60;accountId&#x60;, &#x60;amount&#x60;, &#x60;currency&#x60;, and &#x60;type&#x60; are required.    - &#x60;type&#x60; must be &#x60;Electronic&#x60;.   - &#x60;currency&#x60; of the payment can be different from the payment currency in the customer account settings.   - The amount will not be summed up into the account balance and key metrics regardless of the payment currency.   - No settlement data will be created.   - Either the applied amount or the unapplied amount of the payment is zero.   - The standalone payment cannot be applied, unapplied, or transferred.  Specify &#x60;false&#x60; to create an ordinary payment that will be created, processed, and settled in Zuora. The &#x60;currency&#x60; of an ordinary payment must be the same as the currency in the customer account settings.  | [optional] [default to False]
**type** | **str** | The type of the payment.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

