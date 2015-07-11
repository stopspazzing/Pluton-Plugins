__author__ = 'Corrosion X'
__version__ = '1.0'
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
        self.votingclear(None)
        Commands.Register("voteday")\
            .setCallback("voteday")\
            .setDescription("Initiate vote for day")\
            .setUsage("use during night to start a vote for day")

    def voteday(self, unused, player):
        timerstarted = DataStore.Get("voteday", "timerstarted")
        cooldown = DataStore.Get("voteday", "cooldown")
        if cooldown:
            player.Message("You must wait longer to start another vote!")
            return
        if not timerstarted or None:
            if 17.5 > World.Time < 5.5:
                Server.Broadcast("A vote for day has been started by " + player.Name + " Use /voteday to cast your vote.")
                Plugin.CreateTimer("votingtimer", 60000).Start()
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
        Server.Broadcast("Timer finished")
        DataStore.Add("voteday", "timerstarted", False)
        if DataStore.Get("voteday", "cooldown"):
            return
        result = self.domath()
        if result >= .51:
            Server.Broadcast("Vote for day Passed!")
            World.Time = 7
            self.votingclear(None)
        else:
            Server.Broadcast("Vote for day failed!")
            waittime = 60000  # default waiting time before can start new vote
            Plugin.CreateTimer("votingclear", waittime).Start()
            DataStore.Add("voteday", "cooldown", True)

    def votingclear(self, unused):
        self.votes = 0
        DataStore.Flush("voteday")
        Plugin.KillTimers()

    def domath(self):
        votes = self.votes
        count = Server.Players.Count
        result = votes / count
        return result