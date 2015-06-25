__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'Item Modifier'
import clr
clr.AddReferenceByPartialName("Pluton")
clr.AddReferenceByPartialName("Assembly-CSharp")
import ItemDefinition
import ItemManager
import Pluton
itemkey = ItemManager.FindItemDefinition


class ItemModifier:

    global itemkey

    def On_ServerInit(self):
        if not Plugin.IniExists("Items"):
            Plugin.CreateIni("Items")
            ini = Plugin.GetIni("Items")
            itemdef = ItemManager.GetItemDefinitions()
            for item in itemdef:
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
            if itemkey(key) is None:
                Util.Log("Failed to set stack size for: " + key)
                continue
            itemkey.stackable = int(ini.GetSetting("StackSizes", key))
        for key in ini.EnumSection("ConditionMax"):
            if itemkey(key) is None:
                Util.Log("Failed to set Max Condition for: " + key)
                continue
            itemkey(key).condition.max = float(ini.GetSetting("ConditionMax", key))
        for key in ini.EnumSection("Flags"):
            if itemkey(key) is None:
                Util.Log("Failed to set Flags for: " + key)
                continue
            ##itemkey(key).flags = ItemDefinition.Flag.str(ini.GetSetting("Flags", key))
            if itemkey(key).flags == "1":
                itemkey(key).flags =  ItemDefinition.Flag.NoDropping