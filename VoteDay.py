__author__ = 'Corrosion X'
__version__ = '1.0.1'
__name__ = 'VoteDay'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class VoteDay:

    votes = 0
    GetConfig = Plugin.GetIni("VoteDay")

    def On_PluginInit(self):
        self.votingclearCallback(None)
        Commands.Register("voteday")\
            .setCallback("voteday")\
            .setDescription("Initiate vote for day")\
            .setUsage("use during night to start a vote for day")
        ConfigFile = Plugin.CreateIni("VoteDay")
        ConfigFile.AddSetting("Config", ";; Votes Required is a percent ;;")
        ConfigFile.AddSetting("Config", "votesrequired", "51")
        ConfigFile.AddSetting("Config", ";; Vote Timer - in milliseconds ;;")
        ConfigFile.AddSetting("Config", "votetimer", "60000")
        ConfigFile.AddSetting("Config", ";; Vote Timer - in milliseconds ;;")
        ConfigFile.AddSetting("Config", "cooldown", "60000")
        ConfigFile.Save()

    def voteday(self, unused, player):
        timerstarted = DataStore.Get("voteday", "timerstarted")
        cooldown = DataStore.Get("voteday", "cooldown")
        if cooldown:
            player.Message("You must wait longer to start another vote!")
            return
        if not timerstarted or None:
            if 17.5 < World.Time or World.Time < 5.5:
                vtimer = int(self.GetConfig.GetSetting("Config", "votetimer", "60000"))
                Server.Broadcast("A vote for day has been started by " + player.Name + " Use /voteday to cast your vote.")
                Plugin.CreateTimer("votingtimer", vtimer).Start()
                DataStore.Add("voteday", "timerstarted", True)
                DataStore.Add("voteday", player.SteamID, True)
                self.votes += 1
            else:
                player.Message("You have to wait until night before starting a vote.")
        else:
            if DataStore.ContainsKey("voteday", player.SteamID):
                player.Message("You already voted!")
                return
            else:
                self.votes += 1
                DateStore.Add("voteday", player.SteamID, True)
                player.Message("You're vote was added!")
                result = self.domath()
                result *= 100
                Server.Broadcast("Current votes for day:" + str(result) + "%")

    def votingtimerCallback(self, unused):
        DataStore.Add("voteday", "timerstarted", False)
        if DataStore.Get("voteday", "cooldown"):
            return
        result = self.domath() * 100
        percent = int(self.GetConfig.GetSetting("Config", "votepercent", "51"))
        if result >= percent:
            Server.Broadcast("Vote for day Passed!")
            World.Time = 7
            self.votingclearCallback(None)
        else:
            Server.Broadcast("Vote for day failed!")
            waittime = int(self.GetConfig.GetSetting("Config", "cooldown", "60000"))
            Plugin.CreateTimer("votingclear", waittime).Start()
            DataStore.Add("voteday", "cooldown", True)

    def votingclearCallback(self, unused):
        self.votes = 0
        DataStore.Flush("voteday")
        Plugin.KillTimers()

    def domath(self):
        votes = self.votes
        count = Server.Players.Count
        result = votes / count
        return result