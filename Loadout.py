__name__ = 'Loadout'
import clr
import sys
clr.AddReferenceByPartialName("Pluton", "UnityEngine")
import UnityEngine
import Pluton
import re


class Loadout:
    def On_Respawn(self, respawn):
        respawn.GiveDefault = False
        loadout = None
        if respawn.Player.Admin:
            loadout = Server.LoadOuts["admin"]
        else:
            loadout = Server.LoadOuts["starter"]
        if loadout is not None:
            loadout.ToInv(respawn.Player.Inventory)