import subprocess
import os

ckan_ini = os.environ.get('CKAN_INI', '/srv/app/production.ini')

def update_plugins_from_envvars():
    print('Start update_plugins_from_envvars...')

    CKAN__PLUGINS = os.environ.get('CKAN__PLUGINS')

    command = ["ckan", "config-tool", f"{ckan_ini}", f"ckan.plugins = {CKAN__PLUGINS}"]
    subprocess.call(command)

    print('updated ckan plugins from env vars')


if __name__ == '__main__':

    maintenance = os.environ.get('MAINTENANCE_MODE', '').lower() == 'true'

    if maintenance:
        print('[prerun] Maintenance mode, skipping setup...')
    else:
        update_plugins_from_envvars()
