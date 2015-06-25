__author__ = 'Corrosion X'
__version__ = '0.9'
__name__ = 'VoteDay'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class VoteDay:
    def On_PluginInit(self):
        Commands.Register("voteday")\
            .setCallback("voteday")\
            .setDescription("Initiate vote for day")\
            .setUsage("/voteday during night time")

    def votedayCallback(self, player, unused):
        timerstarted = DataStore.Get("voteday", "timerstarted")
        cooldown = DataStore.Get("voteday", "cooldown")
        if not timerstarted:
            if 17.5 < World.Time < 5.5:
                Server.Broadcast("A vote for day has been started by " + player + " Use /voteday to cast your vote.")
                Plugin.CreateTimer("votingtimer", 60).Start()
                DataStore.Add("voteday", "timerstarted", True)
            else:
                player.Message("You have to wait until night before starting a vote.")
        elif not cooldown:
            if DataStore.ContainsKey("voteday", player.SteamID):
                player.Message("You already voted!")
            else:
                DataStore.Add("voteday", "votes", player.SteamID)
                player.Message("You're vote was added!")
        else:
            player.Message("You must wait until next night to start another vote")

    def votingtimer(self):
        i = None
        if DataStore.Get("voteday", "cooldown"):
            DataStore.Flush("voteday")
            return
        count = Server.Players.Count
        for i in DataStore.Get("voteday", "votes"):
            votes += 1
        if votes / count >= .51:
            Server.Broadcast("Vote for day Passed!")
            World.Time = 6
            DataStore.Flush("voteday")
        else:
            Server.Broadcast("Vote for day failed!")
            ##set time till wait till next night
            time = World.Time
            #find difference between current time and morning aka 6
            waittime = 60 ##temp time
            Plugin.CreateTimer("votingtimer", waittime).Start()
            DataStore.Add("voteday", "timerstarted", False)
            DataStore.Add("voteday", "cooldown", True)
