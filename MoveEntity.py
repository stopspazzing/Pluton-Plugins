__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'MoveEntity'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class MoveEntity:
    def On_Command(self, cmd):
        pl = cmd.User
        if cmd.cmd == "grab" and pl.Admin:
            cangrab = self.grabcheck()
            look = self.lookcheck()
            if look == cangrab:
                Plugin.CreateParallelTimer("grabbing", 500, mydict).Start()

    def grabcheck(self):
        grab = DataStore.Get("SpawnedEntities", pl.GameID,)

    def grabbingCallBack(self, timer):
        user = timer.args
