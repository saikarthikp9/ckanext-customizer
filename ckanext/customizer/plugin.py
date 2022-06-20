import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from .cli import get_commands
import os
import re

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

def get_customizer_group_name_plural():
    word = os.getenv("CUSTOMIZER_GROUP_NAME").lower().capitalize()
    return pluralize_word(word)

def get_customizer_organization_name_plural():
    word = os.getenv("CUSTOMIZER_ORGANIZATION_NAME").lower().capitalize()
    return pluralize_word(word)

def get_customizer_organization_description():
    return os.getenv("CUSTOMIZER_ORGANIZATION_DESCRIPTION")

def get_customizer_group_description():
    return os.getenv("CUSTOMIZER_GROUP_DESCRIPTION")

class CustomizerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'customizer')

    # IClick
    def get_commands(self):
        return get_commands()

    # Template helper functions

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            'customizer_group_name_plural': get_customizer_group_name_plural,
            'customizer_organization_name_plural': get_customizer_organization_name_plural,
            'customizer_organization_description': get_customizer_organization_description,
            'customizer_group_description': get_customizer_group_description,
        }
