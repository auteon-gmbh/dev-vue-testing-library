const isUploadEnabled = (oldClientListing) => {
  if (oldClientListing != null) {
    textBoxEbayItemId.text = oldClientListing.ServerId
  }
  buttonUploadArticle.isEnabled = true
}