__author__ = 'CorrosionX'
__version__ = '1.3'
__name__ = 'EasyAirdrops'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
from UnityEngine import Random


class EasyAirdrops:
    def On_PluginInit(self):
        if not Plugin.IniExists("EasyAirdrops"):
            setini = Plugin.CreateIni("EasyAirdrops")
            setini.AddSetting("Settings", "PlayersRequired", "3")  # Default
            setini.AddSetting("Settings", "DropFrequency", "3600")  # In Seconds! 1 hour
            setini.AddSetting("Settings", "DropDuring", "anytime")  # (default) - Can be day/night/anytime
            setini.AddSetting("Settings", "DropOnPlayer", "True")  # Drop On A Player?
            setini.Save()
        else:
             # If config exists, make sure each setting is set, else add what is missing
            ini = self.easyairdropsini()
            if ini.GetSetting("Settings", "PlayersRequired") is None:
                ini.AddSetting("Settings", "PlayersRequired", "3")  # Default
            if ini.GetSetting("Settings", "DropFrequency") is None:
                ini.AddSetting("Settings", "DropFrequency", "3600")  # In Seconds! 1 hour
            if ini.GetSetting("Settings", "DropDuring") is None:
                ini.AddSetting("Settings", "DropDuring", "anytime")
            if ini.GetSetting("Settings", "DropOnPlayer") is None:
                ini.AddSetting("Settings", "DropOnPlayer", "True")
            ini.Save()
        ini = self.easyairdropsini()
        try:
            drop_time = int(ini.GetSetting("Settings", "DropFrequency"))*1000
        except ValueError:
            drop_time = 3600000  # Default time if number not set/invalid.
        Plugin.CreateTimer("airdroptimer", drop_time).Start()

    def airdroptimerCallback(self, unused):
        ini = self.easyairdropsini()
        players = self.playercount()
        if players:
            drop_during = str(ini.GetSetting("Settings", "DropDuring"))
            if drop_during == "night":
                if 17.5 < World.Time < 5.5:
                    self.dropit()
                else:
                    return
            elif drop_during == "day":
                if 17.5 > World.Time > 5.5:
                    self.dropit()
                else:
                    return
            else:
                self.dropit()

    def easyairdropsini(self):
        return Plugin.GetIni("EasyAirdrops")

    def playercount(self):
        ini = self.easyairdropsini()
        count = Server.Players.Count
        try:
            req_players = int(ini.GetSetting("Settings", "PlayersRequired"))
        except ValueError:
            req_players = 3  # Default time if number not set/invalid.
        if req_players <= count:
            return True
        else:
            return False

    def dropit(self):
        ini = self.easyairdropsini()
        rplayer = bool(ini.GetSetting("Settings", "DropOnPlayer"))
        num = int(Random.Range(0, Server.ActivePlayers.Count))
        rplay = Server.ActivePlayers[num]
        if rplayer:
            World.AirDropAtPlayer(rplay)
            # Use commented out code if you dont want to hear or see the airdrop
            #World.SpawnMapEntity("items/supply_drop", rplay.X, rplay.Y + 500, rplay.Z)
            #Server.Broadcast("Airdrop on player " + str(rplay.Name))
        else:
            World.AirDrop()
            # Use commented out code if you dont want to hear or see the airdrop
            #rplay.X += float(Random.Range(-1000, 1000))
            #rplay.Z += float(Random.Range(-1000, 1000))
            #if -4000 < rplay.X < 4000 and -4000 < rplay.Z < 4000:
            #    World.SpawnMapEntity("items/supply_drop", rplay.X, 1000, rplay.Z)
            #    Server.Broadcast("Airdrop is on its way @ " + str(loc.X) + str(loc.Z))