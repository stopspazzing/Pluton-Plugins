__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'AdminDoor'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class AdminDoor:

    def On_PluginInit(self):
        Commands.Register("admindoor")\
            .setCallback("admindoor")\
            .setDescription("Allow admins to open any door when activated")\
            .setUsage("/admindoor (on/off)")

    def On_DoorUse(self, de):
        activated = DataStore.Get("admindoor", de.Player.SteamID)
        if de.Player.Admin:
            de.IgnoreLock = activated

    def admindoor(self, unused, player):
        activated = DataStore.Get("admindoor", player.SteamID)
        if not activated:
            player.Message("<color=yellow>AdminDoor</color> <color=green>Activated</color>!")
            DataStore.Add("admindoor", player.SteamID, True)
        else:
            player.Message("<color=yellow>AdminDoor</color> <color=red>Deactivated</color>!")
            DataStore.Add("admindoor", player.SteamID, False)

    def On_PlayerConnected(self, pe):
        if pe.Admin:
            DataStore.Add("admindoor", pe.SteamID, False)