# AmendRequestPreviewOptions

Use the `PreviewOptions` container to preview an amendment before committing its changes to a subscription.  You can use a preview to provide a quote of the new charges to a customer before the customer commits to the amended subscription.  For example, make an Amend call with an Amendment object that removes an existing rate plan,  another Amendment object that adds a new rate plan, and turn on the preview options. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_preview_mode** | **bool** |  Determines whether to create an amendment or display a preview of the change. | [optional] 
**include_existing_draft_invoice_items** | **bool** |  Specifies whether to include draft invoice items in amendment previews. | [optional] 
**number_of_periods** | **int** |  Indicates the number of invoice periods to show in a preview. | [optional] 
**preview_through_term_end** | **bool** |  Request to preview the charge through the end of the subscription term. | [optional] 
**preview_type** | **str** |  The type of preview you will receive from a preview request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


