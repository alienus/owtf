"""
Plugin for probing mssql
"""
from owtf.managers.resource import get_resources
from owtf.plugin.plugin_helper import plugin_helper


DESCRIPTION = " MsSql Probing "


def run(PluginInfo):
    resource = get_resources('BruteMsSqlProbeMethods')
    return plugin_helper.CommandDump('Test Command', 'Output', resource, PluginInfo, [])
