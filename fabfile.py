from fabric.api import local


def deploy():
    local('git push origin master')
    local('git push heroku master')
    local(
        'python time_stretch/manage.py collectstatic',
        ' --settings=time_stretch.settings.production --noinput'
    )


def push():
    local('git push origin master')
    local('git push heroku master')


def test():
    command = (
        'python time_stretch/manage.py test '
        '--settings=time_stretch.settings.test blog'
    )
    local(command)
