__author__ = 'Corrosion X'
__version__ = "1.0.3"
# With major help from balu92
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
 
 
class EasyRemove:
    def On_PluginInit(self):
        DataStore.Flush("Remove")

    def On_BuildingPartAttacked(self, attacked):
        player = attacked.Attacker.ToPlayer()
        if player is not None and Server.Players[player.userID].Admin:
            gid = player.userID
            if DataStore.Get("remove", gid) is not None:
                Util.DestroyEntity(attacked.Victim.buildingBlock)

    def On_Command(self, cmd):
        if cmd.cmd == "remove" and cmd.User.Admin:
            isdestroying = DataStore.Get("remove", cmd.User.GameID)
            if isdestroying is not None:
                DataStore.Remove("remove", cmd.User.GameID)
                cmd.User.Message("Remove De-Activated!")
            else:
                DataStore.Add("remove", cmd.User.GameID, True)
                mydict = Plugin.CreateDict()
                mydict["gid"] = cmd.User.GameID
                Plugin.CreateParallelTimer("removerDeactivator", 60000, mydict).Start()
                cmd.User.Message("Remove Activated!")

    def removerDeactivatorCallback(self, timer):
        mydict = timer.Args
        gid = mydict["gid"]
        DataStore.Remove("remove", gid)
        player = Server.Players[gid]
        player.Message("Remove De-Activated!")
        timer.Kill()

    def On_PlayerDisconnected(self, pl):
        DataStore.Remove("remove", pl.GameID)