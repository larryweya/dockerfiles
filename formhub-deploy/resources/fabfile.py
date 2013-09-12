from fabric.api import local

def update(branch='ziggy'):
    local('cd /formhub && git checkout {branch}'.format(branch=branch))
    local('cd /formhub && git pull origin {branch}'.format(branch=branch))
    local('pip install numpy --use-mirrors')
    local('pip install -r formhub/requirements.pip')

