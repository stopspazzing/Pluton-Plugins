__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'EasyEntitySpawner'
# Special thanks to balu92, xEnt, and DreTaX
import clr
import sys
clr.AddReferenceByPartialName("Pluton", "UnityEngine")
import UnityEngine
import Pluton
import re
teamrocket = ("bear", "wolf", "boar", "stag", "chicken")
parts = ("l_upperarm", "r_upperarm", "head", "l_knee", "r_knee", "spine1", "spine2", "spine3", "spike4",
         "l_hand", "r_hand", "r_hip", "l_hip", "l_eye", "r_eye", "l_toe", "r_toe", "pelvis", "l_clavicle",
         "r_clavicle", "r_forearm", "l_forearm", "r_ulna", "l_ulna", "r_foot", "l_foot", "neck", "jaw")
teamash = World.GetPrefabNames()


class EasyEntitySpawner:
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
        Commands.Register("attachp")\
            .setCallback("attachplayer")\
            .setDescription("Attach an entity to a bodypart.")\
            .setUsage("attach entity bodypart")
        Commands.Register("detachall")\
            .setCallback("detachall")\
            .setDescription("Detach all entities from body.")\
            .setUsage("detach #/last/all")

    def On_PlayerConnected(self, pikachu):
        pikachu.Message("Spawn in Entities and Animals! Type /spawnhelp for more help")

    def spawnhere(self, args, player):
        loc = player.Location
        entity = args
        self.spawnit(entity, loc)

    def spawn(self, args, player):
        loc = player.Location
        lookpos = player.GetLookPoint()
        dist = Util.GetVectorsDistance(loc, lookpos)
        entity = args
        if dist > 50.0:
            player.Message("Distance is too far from your current location. Please look where you want it to spawn")
            return
        else:
            loc = lookpos
            self.spawnit(entity, loc)

    def spawnhelp(self, args, player):
        if len(args) == 0:
            msgtousr = ("-> EasyEntitySpawner by CorrosionX - Special thanks to balu92, xEnt, and DreTaX",
                        "To spawn entities, use \"/animalname #\" or \"/entityname #\"",
                        "For Lists:\"/spawnhelp entities\" or \"/spawnhelp animals\"")
            for msg in msgtousr:
                player.Message(msg)
            return
        elif args[0] == "animals":
            player.Message("List of Current Animals:")
            for a in teamrocket:
                player.Message(a)
            return
        elif args[0] == "entities":
            player.Message("Available Entities: Too long to list")
            #  player.Message(prefab)
            return

    def attachplayer(self, args, player):
        attached = DataStore.Get("AttachedEntities", player.GameID)
        if attached is not None:
            player.Message("You already have an object attached to you!")
            return
        else:
            attached = World.AttachToPlayer(player, args[0], args[1], True)
            #attached += 1
            DataStore.Add("AttachedEntities", player.GameID, attached)

    def detachall(self, args, player):
        attached = DataStore.Get("AttachedEntities", player.GameID)
        attached2 = DataStore.Get("EntitiesWithAttachments", player.GameID, attached)
        if args[0] == "all":
            for stored in attached:
                Util.DestroyEntity(stored)
            for stored in attached2:
                Util.DestroyEntity(stored)
            DataStore.Flush("AttachedEntities", player.GameID)
            player.Message("All Created Entities Destroyed")
        #if args[0] == "last":
        #    remove last
        #if args[0] == "first":
        #    remove first
        #if args[0] == "":

    def attachanimal(self, args, player):
        attached = DataStore.Get("EntitiesWithAttachments", player.GameID)
        if attached is not None:
            player.Message("You already have an animal with attachments!")
            return
        else:
            animal = World.SpawnAnimal(args[0], player.Location)
            attached = World.AttachToEntity(animal, args[1], args[2], True)
            #attached += 1
            DataStore.Add("EntitiesWithAttachments", player.GameID, attached)

    def spawnit(self, entity, loc):
        #num = 0
        if entity in teamash:
            if entity == "player":
                player = World.SpawnMapEntity("player/player", loc).ToPlayer()
                player.displayName = "[Pluton Bot]"
            else:
                #  n = [x for x in teamash if entity in x]
                for each in teamash:
                    if entity in each:
                        #while num is not count:
                        World.SpawnMapEntity(each, loc)
                        break
                return
        elif entity in teamrocket:
            #num = 0
            #while num is not count:
            World.SpawnAnimal(entity, loc)
            #    num += 1
            #return