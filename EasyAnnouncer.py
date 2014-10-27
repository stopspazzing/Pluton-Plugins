__author__ = 'CorrosionX'
__version__ = '1.0'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class EasyAnnouncer:
    def On_PluginInit(self):
        Plugin.CreateTimer("Announcer", 360000).Start()

    def AnnouncerCallback(self):
        Server.Broadcast("[Server]", "Every hour, this server updates Pluton & Rust, compiles it, and restarts"
                                     " automatically.")