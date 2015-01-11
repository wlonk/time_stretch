from fabric.api import local


def push():
    local('git push origin master')
    local('git push heroku master')


def collectstatic():
    command = (
        'python time_stretch/manage.py collectstatic'
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
