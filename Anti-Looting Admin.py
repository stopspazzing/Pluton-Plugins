__author__ = 'Corrosion X'
__name__ = 'AntiLooting Admin'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class AntiLootingAdmins:
    def On_LootingPlayer(self, ple):
        if ple.Target.Admin:
            ple.pLoot.Clear()