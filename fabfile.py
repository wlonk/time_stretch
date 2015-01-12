from fabric.api import local


def push():
    local('git push origin master')
    local('git push heroku master')


def collectstatic():

    # Django pipeline will try to use css on s3 if there are any there.
    # That's bad, because we actually want our local styles to be put there.
    # so there should never be anything there on push.

    command = "python -c {0}".format(
            """ \"""import boto
conn = boto.connect_s3()
bucket = conn.get_bucket('benw-personal-site')
contents = bucket.list('css/')
for x in contents:
    x.delete()\"""
    """)
    print command
    local(command)

    command = (
        'python time_stretch/manage.py collectstatic'
        ' -i bootstrap'
        ' --settings=time_stretch.settings.production --noinput'
    )
    local(command)


def deploy():
    push()
    collectstatic()


def test():
    command = (
        'python time_stretch/manage.py test '
        '--settings=time_stretch.settings.test blog'
    )
    local(command)
