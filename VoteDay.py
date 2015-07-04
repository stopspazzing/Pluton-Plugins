__author__ = 'Corrosion X'
__version__ = '0.7'
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

    def voteday(self, unused, player):
        timerstarted = DataStore.Get("voteday", "timerstarted")
        cooldown = DataStore.Get("voteday", "cooldown")
        if not timerstarted:
            if 17.5 > World.Time < 5.5:
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
        DataStore.Add("voteday", "timerstarted", False)
        if DataStore.Get("voteday", "cooldown"):
            DataStore.Flush("voteday")
            return
        count = Server.Players.Count
        votes = DataStore.Count("voteday", "votes")
        if votes / count >= .51:
            Server.Broadcast("Vote for day Passed!")
            World.Time = 7
            DataStore.Flush("voteday")
        else:
            Server.Broadcast("Vote for day failed!")
            waittime = 600  #default waiting time before can start new vote
            Plugin.CreateTimer("votingtimer", waittime).Start()
            DataStore.Add("voteday", "cooldown", True)
