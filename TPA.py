import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
from UnityEngine import *
from System import *


class TPA:
    def On_PlayerConnected(self, p):
        p.MessageFrom("[TPA]", "Use '/tp player' and '/tpa' to accept tp requests!")

    def On_Command(self, cmd):
        if cmd.cmd == "tp" and len(cmd.cmd) == len("tp"):
            player = Server.FindPlayer(cmd.quotedArgs[0])
            if player is not None:
                DataStore.Add("tp", player.SteamID, cmd.User.SteamID)
                player.Message(String.Format("{0} wishes to teleport to you! Type /tpa to accept it.", cmd.User.Name))
                cmd.User.Message(String.Format("Teleport request send to {0}!", player))
                return
            else:
                cmd.User.Message(String.Format("Couldn't find player: {0}", cmd.quotedArgs[0]))
                return
        if cmd.cmd == "tpa" and len(cmd.cmd) == len("tpa"):
            playerSid = DataStore.Get("tp", cmd.User.SteamID)
            DataStore.Remove("tp", cmd.User.SteamID)
            if playerSid is not None:
                player = Server.FindPlayer(playerSid)
                if player is not None:
                    player.Teleport(cmd.User.Location)