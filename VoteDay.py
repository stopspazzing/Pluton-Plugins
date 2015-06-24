__author__ = 'Corrosion X'
__version__ = '0.1'
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
        if not timerstarted:
            if 17.5 < World.Time < 5.5:
                Server.Broadcast("A vote for day has been started by " + player + " Use /voteday to cast your vote.")
                Plugin.CreateTimer("votingfinished", 60).Start()
                DataStore.Add("voteday", "timerstarted", True)
            else:
                player.message("You have to wait until night before starting a vote.")

        else:
            votes = DataStore.Get("voteday", "votes")
            if player.GameID not in votes:
                DataStore.Add("voteday", "votes", player.GameID)
            else:
                player.message("You already voted!")

    def votingfinished(self):
        count = Server.Players.Count
        votes = len(DataStore.Get("votday", "votes"))
        if votes / count >= .51:
            Server.Broadcast("Vote for day Passed!")
            World.Time = 6
        else:
            Server.Broadcast("Vote for day Failed!")
            ##set time till wait till next night