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
        if not timerstarted:
            if 17.5 < World.Time < 5.5:
                Server.Broadcast("A vote for day has been started by " + player + " Use /voteday to cast your vote.")
                self.startvote()
            else:
                player.message("You have to wait until night before starting a vote.")

        else:

    def startvote(self):
        timer start here

        count votes here