# coding=utf-8
from djangodav.db.resources import BaseDBDavResource, NameLookupDBDavMixIn

from .models import CollectionModel, ObjectModel


class CalDavResource(NameLookupDBDavMixIn, BaseDBDavResource):
    collection_model = CollectionModel
    object_model = ObjectModel
