# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class SideBarTempGraph(octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.TemplatePlugin):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict()

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return dict(js=["js/sidebartempgraph.js"],css=["css/sidebartempgraph.css"])

    ##~~ Softwareupdate hook

    def get_update_information(self):
        return dict(
            sidebartempgraph=dict(
                displayName="Sidebar Temp Graph",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="jneilliii",
                repo="OctoPrint-SideBarTempGraph",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/jneilliii/OctoPrint-SideBarTempGraph/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Sidebar Temp Graph"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = SideBarTempGraph()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
