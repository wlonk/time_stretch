from fabric.api import local

def deploy():
    local('git push origin master')
    local('git push heroku master')
    local(
        'python time_stretch/manage.py collectstatic' \
        ' --settings=time_stretch.settings.production --noinput'
    )
