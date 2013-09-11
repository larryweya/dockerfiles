from fabric.api import local

def update(branch='master'):
    local('cd /uwsgi-quick-app && git checkout {branch}'.format(branch=branch))
    local('cd /uwsgi-quick-app && git pull origin {branch}'.format(branch=branch))
