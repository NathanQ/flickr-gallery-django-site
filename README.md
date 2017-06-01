class SetAdmin(admin.ModelAdmin): class Meta: model = Set fields = '**all**'

```
def save_model(self, request, obj, form, change):
    '''
    the razzle dazzle of this method is it calls to Flickr to get a
    photoset's Medium and Large stored image's source url. One of Flickr's
    services is to generate several sizes of web-usable images in addition
    to the one a Flickr user uploads.

    ## Methods

    1 To get the re-sized images source file url(s) from Flickr's api:
        1 match Flickr's authentication and authentication handler requirement
        2 get the re-sized images source urls.

    2 To keep the templates simple, the Set's featured image dictionary object
    of the list of images will be moved to first in the list.
        1 find the respective object in the list by looking for the partial
        string in the 1st(arbitrary) value in a key-value pair and move the
        respective dictionary to the beginning

    3 Save the list to Set.photoset_urls.
    '''

    # 1.1
    flickr_api.set_keys(
        api_key = settings.FLICKR_API_KEY,
        api_secret = settings.FLICKR_API_SECRET
    )
    flickr_api.set_auth_handler('flickr_credentials.dat')

    #1.2
    obj.photoset_urls = []
    photos = flickr_api.Photoset(id = obj.set_id).getPhotos()
    import ipdb; ipdb.set_trace()
    for photo in photos:
        try:
            dikt = {
                small: photo.getPhotoFile(size_label='Medium'),
                large: photo.getPhotoFile(size_label='Large')
            }
            obj.photoset_urls.append(dikt.copy())

        except Exception, e:
            small = 'oops'

    #2.1
    if obj.featured_image is not None:
        for i, elem in enumerate(obj.photoset_urls):
            if obj.featured_image in elem['small']:
                obj.photoset_urls.insert(0, obj.photoset_urls.pop(i))

    super(SetAdmin, self).save_model(request, obj, form, change)
```
