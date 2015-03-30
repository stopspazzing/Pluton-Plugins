__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'UsefulCommands'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
from UnityEngine import *


class UsefulCommands:
    def On_PluginInit(self):
        DataStore.Flush("markloc")
        DataStore.Flush("markset")

    def On_Command(self, cmd):
        suicidelist = ("die", "kill", "slay", "dead")
        locationlist = ("loc", "location")
        if cmd.cmd == "day" and cmd.User.Admin:
            World.Time = 8
        elif cmd.cmd == "night" and cmd.User.Admin:
            World.Time = 17
        elif cmd.cmd in suicidelist:
            cmd.User.Kill()
        elif cmd.cmd in locationlist:
            cmd.User.Message("You're at coordinates: " + str(cmd.User.Location))
        elif cmd.cmd == "mark":
            if cmd.quotedArgs[0] is None:
                markset = bool(DataStore.Get("markset", cmd.User.GameID))
                if not markset:
                    cmd.User.Message("Please \'/mark set\' first!")
                    return
                markloc = DataStore.Get("markloc", cmd.User.GameID)
                dist = Util.GetVectorsDistance(markloc, cmd.User.Location)
                cmd.User.Message("You are " + str(dist) + " from your mark.")
            elif cmd.quotedArgs[0] == "set":
                markset = bool(DataStore.Get("markset", cmd.User.GameID))
                if markset:
                    cmd.User.Message("Updated your Mark")
                markloc = cmd.User.Location
                cmd.User.Message("Location Marked")
                DataStore.Add("markloc", cmd.User.GameID, markloc)
                DataStore.Add("markset", cmd.User.GameID, True)