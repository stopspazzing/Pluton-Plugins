__author__ = 'Corrosion X'
__version__ = '0.9.1'
__name__ = 'EasyEntitySpawner'
# Special thanks to balu92, xEnt, and DreTaX
import clr
import sys
clr.AddReferenceByPartialName("Pluton", "UnityEngine")
import UnityEngine
import Pluton
from System import String


class EasyEntitySpawner:

    teamrocket = ("bear", "wolf", "boar", "stag", "chicken", "horse")
    networkable = None

    def On_ServerInit(self):
        mydict = Plugin.CreateDict()
        networkables = UnityEngine.Resources.FindObjectsOfTypeAll[BaseNetworkable]()
        for network in networkables:
            mydict[str(self.networkable)] += network

    def On_PluginInit(self):
        Commands.Register("spawnhere")\
            .setCallback("spawnhere")\
            .setDescription("Spawn an entity at your location.")\
            .setUsage("spawnhere campfire")
        Commands.Register("spawn")\
            .setCallback("spawn")\
            .setDescription("Spawn an entity where you are looking.")\
            .setUsage("spawn campfire")
        Commands.Register("spawnhelp")\
            .setCallback("spawnhelp")\
            .setDescription("your description here")\
            .setUsage("The usage here")

    def On_PlayerConnected(self, pikachu):
        pikachu.Message("Spawn in Entities and Animals! Type /spawnhelp for more help")

    def spawnhere(self, args, player):
        if len(args) == 0:
            player.Message("Please see /spawnhelp for proper use!")
            return
        quoted = Util.GetQuotedArgs(args)
        entity = quoted[0]
        try:
            count = int(quoted[1])
        except ValueError:
            count = 1
        loc = player.Location
        if 0 > count > 10:
            player.Message("Valid quantities are: 1 - 10")
            return
        self.spawnit(entity, loc, count)

    def spawn(self, args, player):
        if len(args) == 0:
            player.Message("Please see /spawnhelp for proper use!")
            return
        quoted = Util.GetQuotedArgs(args)
        entity = quoted[0]
        try:
            count = int(quoted[1])
        except ValueError:
            count = 1
        loc = player.Location
        lookpos = player.GetLookPoint()
        dist = Util.GetVectorsDistance(loc, lookpos)
        if 0 > count > 10:
            player.Message("Valid quantities are: 1 - 10")
            return
        elif dist > 50.0:
            player.Message("Distance is too far from your current location. Please look where you want it to spawn")
            return
        else:
            loc = lookpos
            self.spawnit(entity, loc, count)

    def spawnhelp(self, args, player):
        if len(args) == 0:
            msgtousr = ("-> EasyEntitySpawner by CorrosionX - Special thanks to balu92, xEnt, and DreTaX",
                        "To spawn entities, use \"/spawnhere entity\" or \"/spawn entity\"",
                        "For Lists:\"/spawnhelp entities\" or \"/spawnhelp animals\"")
            for msg in msgtousr:
                player.Message(msg)
            return
        quoted = Util.GetQuotedArgs(args)
        if quoted[0] == "animals":
            player.Message("List of Current Animals:")
            for a in teamrocket:
                player.Message(a)
            return
        elif quoted[0] == "entities":
            player.Message("Available Entities: Too long to list. Use F1 -> Entity List - Partial Matches Allowed")
            #  player.Message(prefab)
        else:
            player.Message("Not A Valid Option")

    def spawnit(self, entity, loc, count):
        count = int(count)
        entity = str(entity)
        if entity not in self.teamrocket:
            if entity == "player":
                player = World.SpawnMapEntity("player/player", loc).ToPlayer()
                player.displayName = "[Pluton Bot]"
                player.EndSleeping()
            else:
                for a in self.networkables:
                    if entity in a:
                        for x in range(0, count):
                            World.SpawnMapEntity(a, loc)
                    else:
                        return
                return
        else:
            for x in range(0, count):
                World.SpawnAnimal(entity, loc)