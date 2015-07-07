__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'RollTheDice'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
import re
from UnityEngine import Random


class RollTheDice:

    def On_PluginInit(self):
        Commands.Register("rtd")\
            .setCallback("rtd")\
            .setDescription("Have something random happen to you")\
            .setUsage("/rtd")

    def rtd(self, args, player):
        cooldown = DataStore.Get("cooldown", player.GameID)
        if cooldown:
            player.Message("You have to wait longer before rolling dice again!")
        else:
            self.randomevents(player)
            mydict = Plugin.CreateDict()
            DataStore.Add("cooldown", player.GameID, True)
            mydict["gid"] = player.GameID
            Plugin.CreateParallelTimer("cooldown", 60000, dict).Start()

    def cooldownCallback(self, timer):
        mydict = timer.Args
        gid = mydict["gid"]
        DataStore.Remove("cooldown", gid)
        timer.Kill()

    def randomevents(self, player):
        num = int(Random.Range(1, 20))
        if num == 1:
            ##cleaninv
        elif num == 2:
            ##kickplayer
        elif num == 3:
            ##give random item
        elif num == 4:
            ##forcesleep
        elif num == 5:
            ##teleportupinair
        elif num == 6:
            ##hurtrandomamount
        elif num == 7:
            ##freezeinplace
        elif num == 8:
            ##dosomethingelse