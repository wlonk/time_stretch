from fabric.api import local


def deploy():
    local('git push origin master')
    local('git push heroku master')
    command = (
        'python time_stretch/manage.py collectstatic'
        ' --settings=time_stretch.settings.production --noinput'
    )
    local(command)


def push():
    local('git push origin master')
    local('git push heroku master')


def test():
    command = (
        'python time_stretch/manage.py test '
        '--settings=time_stretch.settings.test blog'
    )
    local(command)
