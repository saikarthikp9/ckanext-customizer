import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from .cli import get_commands
import re
from .helpers import get_env_var

# accepts a word(noun) as an argument and returns the pluralized word 
def pluralize_word(word):
    # Check if the given word matches with the rules using the search() function in regex module and if conditional statement 
    if re.search('[sxz]$', word):
         # If it is true then substitute 'es' to the word passed to make it a plural using sub() function of regex module
         return re.sub('$', 'es', word)
    elif re.search('[^aeioudgkprt]h$', word):
        # If it is true then substitue 'es' to the end of the word passed.
        return re.sub('$', 'es', word)
    elif re.search('[aeiou]y$', word):
        # If it is true then substitute 'ies' with 'y' to the word passed to make it a plural using sub() function of regex module
        return re.sub('y$', 'ies', word)
    else:
        # Else just add 's' to the word passed.
        return word + 's'

CUSTOMIZER_GROUP_NAME = get_env_var("CUSTOMIZER_GROUP_NAME", "group").lower().capitalize()
CUSTOMIZER_GROUP_NAME_PLURAL = pluralize_word(CUSTOMIZER_GROUP_NAME)
def get_customizer_group_name_plural():
    return CUSTOMIZER_GROUP_NAME_PLURAL

CUSTOMIZER_ORGANIZATION_NAME = get_env_var("CUSTOMIZER_ORGANIZATION_NAME", "organization").lower().capitalize()
CUSTOMIZER_ORGANIZATION_NAME_PLURAL = pluralize_word(CUSTOMIZER_ORGANIZATION_NAME)
def get_customizer_organization_name_plural():
    return CUSTOMIZER_ORGANIZATION_NAME_PLURAL

CUSTOMIZER_ORGANIZATION_DESCRIPTION = get_env_var("CUSTOMIZER_ORGANIZATION_DESCRIPTION", "CKAN Organisations are used to create, manage and publish collections of datasets. Users can have different roles within an Organisation, depending on their level of authorisation to create, edit and publish.")
def get_customizer_organization_description():
    return CUSTOMIZER_ORGANIZATION_DESCRIPTION

CUSTOMIZER_GROUP_DESCRIPTION = get_env_var("CUSTOMIZER_GROUP_DESCRIPTION", "You can use CKAN Groups to create and manage collections of datasets. This could be to catalogue datasets for a particular project or team, or on a particular theme, or as a very simple way to help people find and search your own published datasets.")
def get_customizer_group_description():
    return CUSTOMIZER_GROUP_DESCRIPTION

CUSTOMIZER_REMOVE_LANG_SELECTION = (get_env_var("CUSTOMIZER_REMOVE_LANG_SELECTION", "False").lower().capitalize() == "True")
def get_customizer_remove_lang_selection():
    return CUSTOMIZER_REMOVE_LANG_SELECTION

CUSTOMIZER_REMOVE_SOCIALS = (get_env_var("CUSTOMIZER_REMOVE_SOCIALS", "False").lower().capitalize() == "True")
def get_customizer_remove_socials():
    return CUSTOMIZER_REMOVE_SOCIALS

class CustomizerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'customizer')

    # IClick
    def get_commands(self):
        return get_commands()

    # Template helper functions

    def get_helpers(self):
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            'customizer_group_name_plural': get_customizer_group_name_plural,
            'customizer_organization_name_plural': get_customizer_organization_name_plural,
            'customizer_organization_description': get_customizer_organization_description,
            'customizer_group_description': get_customizer_group_description,
            'customizer_remove_lang_selection': get_customizer_remove_lang_selection,
            'customizer_remove_socials': get_customizer_remove_socials,
        }
