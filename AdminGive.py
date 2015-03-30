__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'AdminGive'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
import System
from System import *


class AdminGive:
    def On_PluginInit(self):
        Commands.Register("give")\
            .setCallback("giveitem")\
            .setDescription("Give a player an item")\
            .setUsage("give john hatchet 2")

    def giveitem(self, args, player):
        itemID = Pluton.InvItem.GetItemID(args[1])
        amount = int(args[2])
        if player.Admin:
            playerr = self.CheckV(player, args[0])
            if playerr is None:
                return
            else:
                #try:
                #   amount = int(amount)
                #except ValueError:
                #    amount = 1
                playerr.Inventory.Add(itemID, amount)
                playerr.Message("You have been given " + str(amount) + itemID)
                player.Message("You have given " + name + str(amount) + itemID)

    def GetPlayerName(self, namee):
        name = namee.lower()
        for pl in Server.ActivePlayers:
            if pl.Name.lower() == name:
                return pl
        return None

    def CheckV(self, Player, args):
        systemname = "AdminGive"
        count = 0
        if hasattr(args, '__len__') and (not isinstance(args, str)):
            p = self.GetPlayerName(String.Join(" ", args))
            if p is not None:
                return p
            for pl in Server.ActivePlayers:
                for namePart in args:
                    if namePart.lower() in pl.Name.lower():
                        p = pl
                        count += 1
                        continue
        else:
            p = self.GetPlayerName(str(args))
            if p is not None:
                return p
            s = str(args).lower()
            for pl in Server.ActivePlayers:
                if s in pl.Name.lower():
                    p = pl
                    count += 1
                    continue
        if count == 0:
            Player.MessageFrom(systemname, "Couldn't find " + String.Join(" ", args) + "!")
            return None
        elif count == 1 and p is not None:
            return p
        else:
            Player.MessageFrom(systemname, "Found " + str(count) + " player with similar name. Use more correct name!")
            return None