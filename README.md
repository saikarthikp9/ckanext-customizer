[![Tests](https://github.com/saikarthikp9/ckanext-customizer/workflows/Tests/badge.svg?branch=main)](https://github.com/saikarthikp9/ckanext-customizer/actions)

# ckanext-customizer

This CKAN extension provides a way to customize CKAN components (mostly visual) using environment variables. This makes production deployments a breeze.

## Features

- change name of terms (english only): "organization" and "group"
- add custom helper texts for organization and group
- (optional) remove social media
- (optional) remove the language selection

**TODO:** include some screenshots or embedding a video!


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | yes           |

## Installation

To install ckanext-customizer:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

        git clone https://github.com/saikarthikp9/ckanext-customizer.git
        cd ckanext-customizer
        pip install -e .
        pip install -r requirements.txt

3. Add `customizer` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Run the customizer-i18n-branding command

        ckan -c /etc/ckan/default/ckan.ini customizer-i18n-branding

4. Restart CKAN server. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Environment Variables:

| Name                                 | Required | Default  |
| ------------------------------------ | -------- | -------- |
| CUSTOMIZER_ORGANIZATION_NAME         | Y        | N/A      |
| CUSTOMIZER_ORGANIZATION_DESCRIPTION  | Y        | N/A      |
| CUSTOMIZER_GROUP_NAME                | Y        | N/A      |
| CUSTOMIZER_GROUP_DESCRIPTION         | Y        | N/A      |
| CUSTOMIZER_REMOVE_LANG_SELECTION     | N        | False    |
| CUSTOMIZER_REMOVE_SOCIALS            | N        | False    |


## Developer installation

To install ckanext-customizer for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/saikarthikp9/ckanext-customizer.git
    cd ckanext-customizer
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-customizer

If ckanext-customizer should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
