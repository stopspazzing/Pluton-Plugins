__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'GatherRate'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class GatherRate:

    def On_PluginInit(self):
        ##makeconfig
        if not Plugin.IniExist("GatherRate"):
            ini == Plugin.CreateIni("GatherRate")
            ini.AddSetting("GatherRate", "Metal_Ore", 1)
            ini.AddSetting("GatherRate", "Sulfur_Ore", 1)
            ini.AddSetting("GatherRate", "Wood", 1)
            ini.AddSetting("GatherRate", "Stone", 1)
            ini.AddSetting("GatherRate", "Meat", 1)

    def On_Gathering(self, ge):
        ini == Plugin.GetIni("GatherRate")
        for key, value in ini.GetSetting("GatherRate", ge.Resource):
            if ge.Resource == key:
                ge.Amount *= value
