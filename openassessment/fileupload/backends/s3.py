from __future__ import absolute_import

import logging
import os
from django.conf import settings

import boto

from ..exceptions import FileUploadInternalError
from .base import BaseBackend

logger = logging.getLogger("openassessment.fileupload.api")


class Backend(BaseBackend):

    def get_upload_url(self, key, content_type, file, file_name):
        bucket_name, key_name = self._retrieve_parameters(key)
        try:
            os.environ['S3_USE_SIGV4'] = 'True'
            conn = _connect_to_s3()
            conn.auth_region_name = 'eu-frankfurt-1'
            #f = NamedTemporaryFile()
            try:
                size = os.fstat(file.fileno()).st_size
            except:
                file.seek(0, os.SEEK_END)
                size = file.tell()
            bucket = conn.get_bucket(bucket_name)
            callback=None

            k = boto.s3.key(bucket)
            k.key = file_name

            sent = k.set_contents_from_file(file, reduced_redundancy=False, rewind=True)

            file.seek(0)

            if size == sent:
                return True
            return False
            #return '/openassessment/fileupload/s3/upload'
        except Exception as ex:
            logger.exception(
                u"An internal exception occurred while generating an upload URL."
            )
            raise FileUploadInternalError(ex)

    def get_download_url(self, key):
        bucket_name, key_name = self._retrieve_parameters(key)
        try:
            os.environ['S3_USE_SIGV4'] = 'True'
            conn = _connect_to_s3()
            conn.auth_region_name = 'eu-frankfurt-1'
            bucket = conn.get_bucket(bucket_name)
            s3_key = bucket.get_key(key_name)
            return s3_key.generate_url(expires_in=self.DOWNLOAD_URL_TIMEOUT) if s3_key else ""
        except Exception as ex:
            logger.exception(
                u"An internal exception occurred while generating a download URL."
            )
            raise FileUploadInternalError(ex)

    def remove_file(self, key):
        bucket_name, key_name = self._retrieve_parameters(key)
        os.environ['S3_USE_SIGV4'] = 'True'
        conn = _connect_to_s3()
        conn.auth_region_name = 'eu-frankfurt-1'
        bucket = conn.get_bucket(bucket_name)
        s3_key = bucket.get_key(key_name)
        if s3_key:
            bucket.delete_key(s3_key)
            return True
        else:
            return False


def _connect_to_s3():
    """Connect to s3

    Creates a connection to s3 for file URLs.

    """
    # Try to get the AWS credentials from settings if they are available
    # If not, these will default to `None`, and boto will try to use
    # environment vars or configuration files instead.
    aws_access_key_id = getattr(settings, 'AWS_ACCESS_KEY_ID', None)
    aws_secret_access_key = getattr(settings, 'AWS_SECRET_ACCESS_KEY', None)

    return boto.connect_s3(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        host='opiopc.compat.objectstorage.eu-frankfurt-1.oraclecloud.com'
    )
