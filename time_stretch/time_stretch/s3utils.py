from storages.backends.s3boto import S3BotoStorage
from os import path

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')

from django.contrib.staticfiles.storage import CachedFilesMixin
from pipeline.storage import PipelineMixin

import urllib
import urlparse

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler
from django.conf import settings as dj_settings


# CachedFilesMixin doesn't play well with Boto and S3. It over-quotes things,
# causing erratic failures. So we subclass.
# (See http://stackoverflow.com/questions/11820566/inconsistent-
#    signaturedoesnotmatch-amazon-s3-with-django-pipeline-s3boto-and-st)
class PatchedCachedFilesMixin(CachedFilesMixin):
    def url(self, *a, **kw):
        s = super(PatchedCachedFilesMixin, self).url(*a, **kw)
        if isinstance(s, unicode):
            s = s.encode('utf-8', 'ignore')
        scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
        path = urllib.quote(path, '/%')
        qs = urllib.quote_plus(qs, ':&=')
        return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))

    def path(self, name):
        return self._normalize_name(name)


class S3PipelineStorage(
    PipelineMixin, PatchedCachedFilesMixin, S3BotoStorage
):

    def path(self, name):
        return self._normalize_name(name)


class LessCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith('.less')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        # The smart thing would be to make this take the directory fragments
        # from after the static root that pipeline supplies.
        # But I don't know the best way to do that at the moment.

        infile = dj_settings.STATICFILES_DIR+'/css/'+path.split(infile)[1]
        outfile = dj_settings.STATICFILES_DIR+'/css/'+path.split(outfile)[1]
        command = "%s %s %s %s" % (
            settings.PIPELINE_LESS_BINARY,
            settings.PIPELINE_LESS_ARGUMENTS,
            infile,
            outfile
        )
        print command
        return self.execute_command(command, cwd=dj_settings.STATICFILES_DIR)
