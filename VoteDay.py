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

    votes = 0

    def On_PluginInit(self):
        Commands.Register("voteday")\
            .setCallback("voteday")\
            .setDescription("Initiate vote for day")\
            .setUsage("/voteday during night time")

    def voteday(self, unused, player):
        global votes
        timerstarted = DataStore.Get("voteday", "timerstarted")
        cooldown = DataStore.Get("voteday", "cooldown")
        if not timerstarted or None:
            if 17.5 > World.Time < 5.5:
                Server.Broadcast("A vote for day has been started by " + player.Name + " Use /voteday to cast your vote.")
                Plugin.CreateTimer("votingtimer", 60).Start()
                DataStore.Add("voteday", "timerstarted", True)
            else:
                player.Message("You have to wait until night before starting a vote.")
        elif not cooldown:
            if DataStore.ContainsKey("voteday", player.SteamID):
                player.Message("You already voted!")
            else:
                votes += 1
                player.Message("You're vote was added!")
        else:
            player.Message("You must wait until next night to start another vote")

    def votingtimer(self, timer):
        DataStore.Add("voteday", "timerstarted", False)
        if DataStore.Get("voteday", "cooldown"):
            return
        global votes
        count = Server.Players.Count
        int(votes)
        if votes / count >= .51:
            Server.Broadcast("Vote for day Passed!")
            World.Time = 7
            self.votingclear(None)
        else:
            Server.Broadcast("Vote for day failed!")
            waittime = 600  #default waiting time before can start new vote
            Plugin.CreateTimer("votingclear", waittime).Start()
            DataStore.Add("voteday", "cooldown", True)

    def votingclear(self, timer):
        global votes
        votes = 0
        DataStore.Flush("voteday")