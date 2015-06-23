__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'Item Modifier'

import clr
clr.AddReferenceByPartialName("Pluton", "Assembly-CSharp")
import ItemDefinition, ItemManager, Pluton


class ItemModifier:
    def On_ServerInit(self):
        if not Plugin.IniExists("Items"):
            Plugin.CreateIni("Items")
            ini = Plugin.GetIni("Items")
            items = ItemManager.GetItemDefinitions()
            for item in items:
                ##ini.AddSetting("UID", item.shortname, str(item.uid))
                ini.AddSetting("StackSizes", item.shortname, str(item.stackable))
                ini.AddSetting("ConditionMax", item.shortname, str(item.condition.max))
                ini.AddSetting("Flags", item.shortname, str(item.flags))
                ##ini.AddSetting("Amount", item.shortname, str(item.amount))
                ##ini.AddSetting("LockTime", item.shortname, str(item.locktime))
                ##ini.AddSetting("RemoveTime", item.shortname, str(item.removetime))
                ##ini.AddSetting("InstanceData", item.shortname, str(item.instanceData))
                ##ini.AddSetting("IsBlueprint", item.shortname, str(item.isBlueprint))				
                ini.Save()
        ini = Plugin.GetIni("Items")
        for key in ini.EnumSection("StackSizes"):
            if ItemManager.FindItemDefinition(key) == None:
                Util.Log("Failed to set stack size for: " + key)
                continue
            ItemManager.FindItemDefinition(key).stackable = int(ini.GetSetting("StackSizes", key))
        for key in ini.EnumSection("ConditionMax"):
            if ItemManager.FindItemDefinition(key) == None:
                Util.Log("Failed to set Max Condition for: " + key)
                continue
            ItemManager.FindItemDefinition(key).condition.max = float(ini.GetSetting("ConditionMax", key))
        for key in ini.EnumSection("Flags"):
            if ItemManager.FindItemDefinition(key) == None:
                Util.Log("Failed to set Flags for: " + key)
                continue
            ##ItemManager.FindItemDefinition(key).flags = ItemDefinition.Flag.str(ini.GetSetting("Flags", key))
            if ItemManager.FindItemDefinition(key).flags == "1":
                ItemManager.FindItemDefinition(key).flags =  ItemDefinition.Flag.NoDropping