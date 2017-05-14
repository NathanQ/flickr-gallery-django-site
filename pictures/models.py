from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import JSONField
from django.utils.safestring import mark_safe


class Flickr_Account(models.Model):
    flickr_id = models.CharField(
        max_length = 50,
        help_text=mark_safe('The Flickr id is the Flickr album owner and is used by the app to find information about the photosets. To determine your ID, visit your Flickr profile page and look for it at the end of the URL. For example, "www.flickr.com/photos/<strong>12341234@N12</strong>/"'))
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        help_text="The name is whatever you'd like to refer to the Flickr account owner as.")

    def __unicode__(self):
        return self.flickr_id


class Set(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        help_text="The name will be displayed as a heading in the photoset page and used to list the photosets.")
    set_id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text=mark_safe('The set id is what photo set to display. To find this, open the Flickr photo set and copy the last string of characters in the end of the URL. For example, https://www.flickr.com/photos/146011281@N02/albums/<strong style="color: red">72157676287467202</strong>'))
    flickr_set_owner = models.OneToOneField(
        Flickr_Account,
        null=False,
        blank=False,
        help_text=mark_safe('The flickr set owner is the Flickr album owner. To determine your ID, visit your Flickr profile page and look for it at the end of the URL. For example, "www.flickr.com/photos/<strong>12341234@N12</strong>/"'))
    featured_image = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=mark_safe('The featured image is the image which will be displayed in the list of photosets and be listed as the first one in the photoset.<br>To find it, click the image in the photoset and copy the characters before "/in/album". For example, https://www.flickr.com/photos/146011281@N02/<strong style="color:red">30965802203</strong>/in/album-72157676287467202/'))
    slug = models.SlugField(
        slugify('url'),
        null=False,
        blank=False,
        help_text=mark_safe('The slug is the url where the photoset will reside on the site and needs to be written in lower case with a dash. For example, "air-guitar" will be found on the site at yoursite.com/set/air-guitar/."'))
    photoset_urls = JSONField(
        null=True,
        blank=True,
        help_text="The photoset urls are generated when you save. These values are Flickr's stored optimized medium and large images for web to display on the site. If you update the Flickr gallery, return here and save again to see the changes reflected on the site.")

    def __unicode__(self):
        return self.name
