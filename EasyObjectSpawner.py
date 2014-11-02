__author__ = 'Corrosion X'
__version__ = '1.0'
__name__ = 'EasyObjectSpawner'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
from UnityEngine import re


class EasyObjectSpawner:
    def On_PlayerConnected(self, pikachu):
        pikachu.Message("Spawn in Entities and Animals! Type /(animal) # or /entity # or /spawnhelp for more help")

    def On_Command(self, snorlax):
        pl = snorlax.User
        args = snorlax.args
        loc = pl.Location
        num = 0
        lookpos = pl.GetLookPoint()
        dist = Util.GetVectorsDistance(loc, lookpos)
        try:
            count = int(args[0])
        except ValueError:
            count = 0
        teamash = {"player": "player/player", "playercorpse": "npc/animals/player_corpse",
               "wolfcorpse": "npc/animals/wolf_corpse", "boarcorpse": "npc/animals/boar_corpse",
               "stagcorpse": "npc/animals/stag_corpse", "arrow": "items/arrow", "supplydrop": "items/supply_drop",
               "woodbox": "items/woodbox_deployed", "campfire": "items/campfire_deployed",
               "lantern": "items/lantern_deployed"}
        teamrocket = ("bear", "wolf", "boar", "stag")
        #gymbadges = ("l_arm", "r_arm", "l_leg", "r_leg", "l_hand", "r_hand")
        msgtousr = ("-> EasyObjectSpawner by CorrosionX - Special thanks to balu92 & xEnt",
                    "To spawn entities, use \"/animalname #\" or \"/entityname #\"",
                    "For Lists:\"/spawnhelp entities\" or \"/spawnhelp animals\"")
        if pl is not None:
            if snorlax.cmd == "spawnhelp":
                if len(args) == 0:
                    for msg in msgtousr:
                        pl.Message(msg)
                    return
                elif args == "entities":
                    pl.Message("Available Entities: ")
                    keys = re.sub('[[\]\']', '', str(teamash.keys()))
                    keys = keys.split(',')
                    keys = [",".join(keys[i:i+7]) for i in range(0, len(keys), 7)]
                    lengthofkeys = len(keys)
                    for i in xrange(-1, lengthofkeys):
                        i += 1
                        if i < lengthofkeys:
                            sentence = re.sub('[[\]\']', '', str(keys[i]))
                            pl.Message(sentence)
                    return
                elif args == "animals":
                    pl.Message("List of Current Animals:")
                    for a in teamrocket:
                        pl.Message(a)
                    return
            elif snorlax.cmd == "attach":
                World.AttachToPlayer(pl, snorlax.cmd.quotedArgs[0], snorlax.cmd.quotedArgs[1], True)
                #DataStore.Add("StoredEntities", DataStore.Count("StoredEntities"), spawnedentity)
            elif snorlax.cmd == "destroyall":
                for key, value in DataStore.GetTable("StoredEntities"):
                    Util.DestroyEntity(value)
                DataStore.Flush("StoredEntities")
                pl.Message("All Created Entities Destroyed")
            if 10 >= count > 0 and dist < 50.0:
                if snorlax.cmd in teamrocket:
                    while num is not count:
                        World.SpawnAnimal(snorlax.cmd, lookpos)
                        num += 1
                    return
                elif snorlax.cmd in teamash.keys():
                    if snorlax.cmd == "supplydrop":
                        count = 1
                    elif snorlax.cmd == "player":
                        player = World.SpawnMapEntity("player/player", lookpos).ToPlayer()
                        World.AttachToPlayer(player, "items/lantern_deployed", "head", True)
                        player.displayName = "[Pluton Bot]"
                        count = 1
                    while num is not count:
                        World.SpawnMapEntity(teamash[snorlax.cmd], lookpos)
                        num += 1
                    return
            elif dist > 50.0:
                pl.Message("Distance is too far from your current location. Please look where you want it to spawn")
                return
            elif count > 10:
                pl.Message("Please use 1 - 10, anything more would cause lag.")
                return