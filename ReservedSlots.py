__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'ReservedSlots'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class ReservedSlots:

    def On_PluginInit(self):
        if not Plugin.IniExists("ReservedSlots"):
            setini = Plugin.CreateIni("ReservedSlots")
            setini.AddSetting("Settings", "ReserveSlots", "2")
            setini.Save()
        Commands.Register("rslots")\
            .setCallback("rslots")\
            .setDescription("Allows an admin to add and remove players from reserve slots.")\
            .setUsage("/rslots add/remove steamid")

    def On_ClientAuth(self, ae):
        cnt = self.domath()
        ini = Plugin.GetIni("ReservedSlots")
        if cnt or ini.ContainsSetting("Reserved", str(ae.GameID)):
            return
        else:
            ae.Reject("You have been kicked due to reserve slots.")
            ##Debug.Log("Player " + ae.Name + " : " + ae.GameID + " was rejected due to reserve slots.")

    def domath(self):
        cplayers = Server.ActivePlayers.Count
        ini = Plugin.GetIni("ReservedSlots")
        rslots = ini.GetSetting("Settings", "Reservedslots", "4")
        maxpl = Server.MaxPlayers
        check = maxpl - int(rslots)
        if check > cplayers:
            return True
        else:
            return False

    def rslots(self, args, player):
        quoted = Util.GetQuotedArgs(args)
        player.Message(str(Server.MaxPlayers))
        if not player.Admin:
            return
        if len(quoted) < 2:
            player.Message("Please use /reserveslots add/remove steamid")
        elif quoted[0] is "remove" or "add":
            if len(quoted[1]) == 17:
                ini = Plugin.GetIni("ReserveSlots")
                if quoted[0] == "add":
                    ini.AddSetting("Reserved", quoted[1])
                if quoted[0] == "remove":
                    if ini.ContainsSetting("Reserved", quoted[1]):
                        ini.DeleteSetting("Reserved", quoted[1])
            else:
                player.Message("Please provide a valid steamID")