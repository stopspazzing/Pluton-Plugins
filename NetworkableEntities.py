__author__ = 'stopspazzing'
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Assembly-CSharp")
import BaseNetworkable
import UnityEngine

class NetworkableEntities:
    def On_PluginInit(self):
        networkables = UnityEngine.Resources.FindObjectsOfTypeAll[BaseNetworkable]()
        for networkable in networkables:
            mydict[str(networkable)] += networkable