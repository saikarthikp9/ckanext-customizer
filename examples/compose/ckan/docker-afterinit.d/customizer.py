import subprocess
import os

ckan_ini = os.environ.get('CKAN_INI', '/srv/app/production.ini')

def customizer_apply():
    print('Start customizer_apply...')
    command = ['ckan', '-c', ckan_ini, 'customizer-i18n-branding']
    subprocess.call(command)
    print('Made customizer_apply i18n changes')


if __name__ == '__main__':
    maintenance = os.environ.get('MAINTENANCE_MODE', '').lower() == 'true'
    if maintenance:
        print('[prerun] Maintenance mode, skipping setup...')
    else:
        customizer_apply()
