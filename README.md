# ckanext-customizer

This CKAN extension provides a way to customize a CKAN implementation using environment variables that are not already supported by [default](http://docs.ckan.org/en/latest/maintaining/configuration.html#environment-variables) or by [ckanext-envvars](https://github.com/okfn/ckanext-envvars). The goal is to make production deployments a breeze.

## Features

- change name of terms: "organization" and "group" (will handle plurals, capitalizations, etc.) and add custom helper texts for the same
- remove social media buttons
- remove the language selection from footer

Please request a feature by creating an issue in this repository.


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | yes           |
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

5. Restart CKAN server. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Environment Variables:

| Name                                 | Required | Default  |
| ------------------------------------ | -------- | -------- |
| CUSTOMIZER_ORGANIZATION_NAME         | N        | organization      |
| CUSTOMIZER_ORGANIZATION_DESCRIPTION  | N        | CKAN Organisations are used to create, manage and publish collections of datasets. Users can have different roles within an Organisation, depending on their level of authorisation to create, edit and publish. |
| CUSTOMIZER_GROUP_NAME                | N        | group      |
| CUSTOMIZER_GROUP_DESCRIPTION         | N        | You can use CKAN Groups to create and manage collections of datasets. This could be to catalogue datasets for a particular project or team, or on a particular theme, or as a very simple way to help people find and search your own published datasets. |
| CUSTOMIZER_REMOVE_LANG_SELECTION     | N        | False    |
| CUSTOMIZER_REMOVE_SOCIALS            | N        | False    |

## Limitations

- "organization" and "group" terms will be changed only in English. So it is recommended to set env var CUSTOMIZER_REMOVE_LANG_SELECTION=True
- the paths "/organization" and "/group" remains unchanged

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

## References

- [CKAN repository](https://github.com/ckan/ckan)
- [Helm Chart for CKAN](https://github.com/keitaroinc/ckan-helm)