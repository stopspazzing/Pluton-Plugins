__author__ = 'Corrosion X'
__version__ = '0.8.1'
__name__ = 'ReservedSlots'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class ReservedSlots:
    def On_PluginInit(self):
        if not Plugin.IniExists("ReserveSlots"):
            setini = Plugin.CreateIni("ReserveSlots")
            setini.AddSetting("ReserveSlots", "slots" "2")
            ##setini.AddSetting("Reserved", "id", "7843920103240234")
            setini.Save()
        Command.Register("reserveslots")\
            .setCallback("rslots")\
            .setDestription("Allows an admin to add and remove players from reserve slots.")\
            .setUsage("/reserveslots add/remove steamid")

    def On_ClientAuth(self, ae):
        cnt = self.domath()
        ini = Plugin.GetIni("Reserved")
        if cnt or ini.ContainsSetting("id", ae.GameID):
            return
        else:
            ae.Reject("You have been kicked due to reserve slots.")
            Debug.Log("Player " + ae.Name + " : " + ae.GameID + " was rejected due to reserve slots.")

    def domath(self):
        cplayers = Server.ActivePlayers.Count
        ini = Plugin.GetIni("Settings")
        rslots = ini.GetSetting("reservedslots")
        maxpl = ConVar.Server.maxplayers
        check = maxpl - rslots
        if check >= cplayers:
            return True
        else:
            return False

    def rslots(self, args, player):
        if not player.Admin:
            return
        if len(args) <= 2:
            player.Message("Please use /reserveslots add/remove steamid")
        elif args[0] is "remove" or "add":
            if len(args[1]) == 17:
                ini = Plugin.GetIni("Settings")
                if args[0] == "add":
                    ini.AddSetting("id", args[1])
                if args[0] == "remove":
                    if ini.ContainsSetting("id", args[1]):
                        ini.DeleteSetting("id", args[1])
            else:
                player.Message("Please provide a valid steamID")