__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'EasyEntitySpawner'
# Special thanks to balu92, xEnt, and DreTaX
import clr
import sys
clr.AddReferenceByPartialName("Pluton", "UnityEngine")
import UnityEngine
import Pluton
from System import String
teamrocket = ("bear", "wolf", "boar", "stag", "chicken")
GlobalData["prefabs"] = World.GetPrefabNames()


class EasyEntitySpawner:

    prefabs = None

    def On_ServerInit(self):
        self.prefabs = World.GetPrefabNames()
        for prefab in self.prefabs:
            if "chicken" in prefab:
                UnityEngine.Debug.Log("chicken is: {}".format(prefab))
            if "wolf" in prefab:
                UnityEngine.Debug.Log("wolf is: {}".format(prefab))

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
        quoted = Util.GetQuotedArgs(args)
        entity = quoted[0]
        count = quoted[1]
        loc = player.Location
        if 0 > count > 10:
            player.Message("Valid quantities are: 1 - 10")
            return
        self.spawnit(entity, loc, count)

    def spawn(self, args, player):
        quoted = Util.GetQuotedArgs(args)
        entity = quoted[0]
        count = quoted[1]
        loc = player.Location
        lookpos = player.GetLookPoint()
        dist = Util.GetVectorsDistance(loc, lookpos)
        if 0 > count > 10:
            player.Message("Valid quantities are: 1 - 10")
            return
        if dist > 50.0:
            player.Message("Distance is too far from your current location. Please look where you want it to spawn")
            return
        else:
            loc = lookpos
            self.spawnit(entity, loc, count)

    def spawnhelp(self, args, player):
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
            msgtousr = ("-> EasyEntitySpawner by CorrosionX - Special thanks to balu92, xEnt, and DreTaX",
                        "To spawn entities, use \"/spawnhere entity\" or \"/spawn entity\"",
                        "For Lists:\"/spawnhelp entities\" or \"/spawnhelp animals\"")
            for msg in msgtousr:
                player.Message(msg)
            return

    def spawnit(self, entity, loc, count):
        num = 0
        if count is None:
            count = 1
        try:
            int(count)
        except ValueError:
            count = 1
        if entity not in teamrocket:
            if entity == "player":
                player = World.SpawnMapEntity("player/player", loc).ToPlayer()
                player.displayName = "[Pluton Bot]"
                player.EndSleeping()
            else:
                for prefab in GlobalData["prefab"]:
                    if str(entity) in prefab:
                        while num <= count:
                            World.SpawnMapEntity(prefab, loc)
                            num += 1
                return
        else:
            while num <= count:
                World.SpawnAnimal(entity, loc)
                num += 1
            return