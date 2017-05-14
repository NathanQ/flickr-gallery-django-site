# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 17:10
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flickr_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flickr_id', models.CharField(help_text='The Flickr id is the Flickr album owner and is used by the app to find information about the photosets. To determine your ID, visit your Flickr profile page and look for it at the end of the URL. For example, "www.flickr.com/photos/<strong>12341234@N12</strong>/"', max_length=50)),
                ('name', models.CharField(help_text="The name is whatever you'd like to refer to the Flickr account owner as.", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name will be displayed as a heading in the photoset page and used to list the photosets.', max_length=200)),
                ('set_id', models.CharField(help_text='The set id is what photo set to display. To find this, open the Flickr photo set and copy the last string of characters in the end of the URL. For example, https://www.flickr.com/photos/146011281@N02/albums/<strong style="color: red">72157676287467202</strong>', max_length=100)),
                ('featured_image', models.CharField(blank=True, help_text='The featured image is the image which will be displayed in the list of photosets and be listed as the first one in the photoset.<br>To find it, click the image in the photoset and copy the characters before "/in/album". For example, https://www.flickr.com/photos/146011281@N02/<strong style="color:red">30965802203</strong>/in/album-72157676287467202/', max_length=200, null=True)),
                ('slug', models.SlugField(help_text='The slug is the url where the photoset will reside on the site and needs to be written in lower case with a dash. For example, "air-guitar" will be found on the site at yoursite.com/set/air-guitar/."', verbose_name='url')),
                ('photoset_urls', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text="The photoset urls are generated when you save. These values are Flickr's stored optimized medium and large images for web to display on the site. If you update the Flickr gallery, return here and save again to see the changes reflected on the site.", null=True)),
                ('flickr_set_owner', models.OneToOneField(help_text='The flickr set owner is the Flickr album owner. To determine your ID, visit your Flickr profile page and look for it at the end of the URL. For example, "www.flickr.com/photos/<strong>12341234@N12</strong>/"', on_delete=django.db.models.deletion.CASCADE, to='pictures.Flickr_Account')),
            ],
        ),
    ]
