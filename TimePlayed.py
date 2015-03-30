__author__ = 'Corrosion X'
__name__ = 'TimePlayed'
__version__ = '0.2'
import clr
import sys
clr.AddReferenceByPartialName("Pluton", "UnityEngine")
import UnityEngine
import Pluton
from System import String
import datetime


class TimePlayed:
    def On_PluginInit(self):
        Commands.Register("timeonline")\
            .setCallback("timeonline")\
            .setDescription("Gives your time online stats.")\
            .setUsage("/timeonline")

    def On_PlayerDisconnected(self, player):
        playerid = player.GameID
        getstamp = Plugin.GetTimestamp()
        DataStore.Add("LastConnected", playerid, getstamp)
        timedsession = player.TimeOnline
        totaltime = DataStore.Get("TotalTimePlayed", playerid)
        if totaltime is None:
            totaltime = 0
        totaltime += timedsession
        DataStore.Add("TotalTimePlayed", playerid, totaltime)

    def timeonline(self, notused, player):
        playerid = player.GameID
        timeplayed = DataStore.Get("LastConnected", playerid)
        totaltime = DataStore.Get("TotalTimePlayed", playerid)
        timeplayed = datetime.datetime.fromtimestamp(timeplayed).strftime('%Y-%m-%d %H:%M:%S')
        if timeplayed and totaltime is not None:
            player.Message("Last Played:" + str(timeplayed))
            player.Message("Total Time Played:" + str(totaltime))
        else:
            player.Message("Your time hasn't been recorded yet.")