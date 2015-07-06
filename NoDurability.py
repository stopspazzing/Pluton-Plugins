__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'NoDurability'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class NoDurability:
    def On_LoseCondition(self, lc):
        if lc.Item not None or Broken:
        lc.Item.Condition = lc.Item.origCondition