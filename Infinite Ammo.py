__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'InfiniteAmmo'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class InfiniteAmmo:

    def On_WeaponFired(self, wf):
        if wf.Item not wf.Broken:
            wf.Ammo = wf.origAmmo

    def On_WeaponThrown(self, wt):
        if wt.Item == Grenade:
