__author__ = 'Corrosion X'
__version__ = '1.0'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
from Pluton import InvItem


class AutoKit:
    def On_Respawn(self, re):
        re.GiveDefault = False
        if re.Player.Admin:
            loadout = Server.LoadOuts["admin"]
        else:
            loadout = Server.LoadOuts["starter"]
        loadout.ToInv(re.Player.Inventory)