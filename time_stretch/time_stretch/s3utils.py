from storages.backends.s3boto import S3BotoStorage
# from pipeline.storage import GZIPMixin

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')

from django.contrib.staticfiles.storage import CachedFilesMixin
from pipeline.storage import PipelineMixin

import urllib
import urlparse

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


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
        command = "%s %s %s %s" % (
            settings.PIPELINE_LESS_BINARY,
            settings.PIPELINE_LESS_ARGUMENTS,
            infile,
            outfile
        )
        print command
        return self.execute_command(command, cwd=settings.STATICFILES_DIR)
