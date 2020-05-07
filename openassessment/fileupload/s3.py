from __future__ import absolute_import

import logging
import os
from django.conf import settings
from boto.s3.key import Key
from .exceptions import FileUploadInternalError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .backends.s3 import _connect_to_s3
from django.shortcuts import HttpResponse

@login_required()
@require_http_methods(["PUT"])
def s3_storage(request, key):
    """
    Upload files using s3 set_contents_from_file.
    """
    conn = _connect_to_s3()
    conn.auth_region_name = 'eu-frankfurt-1'
    file = open('unnamed.jpg', 'r+')
    filename = 'unnamed.jpg'
    try:
        size = os.fstat(file.fileno()).st_size
    except:
        file.seek(0, os.SEEK_END)
        size = file.tell()


    bucket = conn.get_bucket('opi_public_2')
    callback=None

    k = Key(bucket)
    k.key = filename

    sent = k.set_contents_from_file(file, reduced_redundancy=False, rewind=True)

    file.seek(0)

    if size == sent
        return HttpResponse()
    else
        return False


