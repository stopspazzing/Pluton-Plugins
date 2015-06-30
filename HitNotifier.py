__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'HitNotifier'
import clr
import sys
clr.AddReferenceByPartialName("Pluton", "UnityEngine", "Assembly-CSharp")
import UnityEngine
import Pluton
##import Effect
from UnityEngine import Vector3


class HitNotifier:

    DefaultVector = None

    def On_PlayerHurt(self, he):
        ##self.DefaultVector = Vector3(0, 0, 0)
        victim = he.Victim
        attacker = he.Attacker
        if attacker is None:
            return
        if victim.ToPlayer() and attacker.ToPlayer():
            attacker.Message("<size=18><color=red>Hit</color></size>")
            ##Effect.server.Run("fx/gestures/eat_chewy_meat", attacker, 0, self.DefaultVector, self.DefaultVector)