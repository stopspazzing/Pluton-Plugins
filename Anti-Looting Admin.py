__author__ = 'Corrosion X'
__name__ = 'AntiLooting Admin'
__version__ = '0.9'
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

    def On_LootingEntity(self, ple):
        if ple.