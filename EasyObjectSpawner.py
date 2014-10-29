__author__ = 'Corrosion X'
__version__ = '1.2'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class EasyObjectSpawner:
    def On_PlayerConnected(self, p):
        p.Message("Spawn in Entities and Animals! Type /(animal) # or /entity # or /spawnhelp for more help")

    def On_Command(self, snorlax):
        teamash = ("player", "parachute", "supplydrop", "snowtree1", "snowtree2", "field", "cargoplane", "parachute",
                   "metalore", "stoneore", "woodpile", "sulfurore", "tree1", "tree2", "tree3", "tree4", "tree5",
                   "foresttree1", "foresttree2", "foresttree3", "foresttree4", "foresttree5", "fieldtree1",
                   "fieldtree2", "fieldtree3", "playercorpse", "bearcorpse", "wolfcorpse", "boarcorpse",
                   "stagcorpse", "arrow", "shotgunbullet", "riflebullet", "pistolbullet")
        teamrocket = ("bear", "wolf", "boar", "stag")
        loc = snorlax.User.Location
        num = 0
        # count = None
        try:
            count = int(snorlax.quotedArgs[0])
        except ValueError:
            count = 0
        if snorlax.cmd is not None:
            if snorlax.cmd in teamrocket:
                if snorlax.quotedArgs[0] == 0:
                    snorlax.User.Message("Use /animal # - Max number is 10")
                    return
                elif 10 >= count > 0:
                    while num is not count:
                        World.SpawnAnimal(snorlax.cmd, loc.x, loc.y, loc.z)
                        num += 1
                else:
                    snorlax.User.Message("Please use 1 - 10, anything more would cause lag.")
                    return
            elif snorlax.cmd in teamash:
                if snorlax.quotedArgs[0] == 0:
                    snorlax.User.Message("Use /Entity # - Max number is 10")
                #Random
                elif snorlax.cmd == "supplydrop":
                    raichu = "items/supply_drop"
                elif snorlax.cmd == "player":
                    player = World.SpawnMapEntity("player/player", loc.x, loc.y, loc.z).ToPlayer()
                    player.displayName = "[Pluton Bot]"
                    return
                # elif snorlax.cmd == "airdroponme":
                #    World.AirDropAtPlayer(snorlax.User)
                #    return
                #elif snorlax.cmd == "net_env":  # Doesn't spawn anything
                #    raichu = "system/net_env"
                elif snorlax.cmd == "cargoplane":
                    raichu = "events/cargo_plane"
                elif snorlax.cmd == "parachute":
                    raichu = "parachute"
                elif snorlax.cmd == "parachute":
                    raichu = "parachute"
                elif snorlax.cmd == "shotgunbullet":
                    raichu = "projectiles/shotgunbullet"
                elif snorlax.cmd == "riflebullet":
                    raichu = "projectiles/riflebullet"
                elif snorlax.cmd == "pistolbullet":
                    raichu = "projectiles/pistolbullet"
                elif snorlax.cmd == "arrow":
                    raichu = "items/arrow"
                #Resources wood/stone/metal/sulfur
                elif snorlax.cmd == "metalore":
                    raichu = "autospawn/resources/ores/resource_ore_metal"
                elif snorlax.cmd == "stoneore":
                    raichu = "autospawn/resources/ores/resource_ore_stone"
                elif snorlax.cmd == "woodpile":
                    raichu = "autospawn/resources/piles/resource_pile_wood"
                elif snorlax.cmd == "sulfurore":
                    raichu = "autospawn/resources/ores/resource_ore_sulfur"
                elif snorlax.cmd == "playercorpse":
                    raichu = "player/player_corpse"
                elif snorlax.cmd == "bearcorpse":
                    raichu = "npc/animals/bear_corpse"
                elif snorlax.cmd == "wolfcorpse":
                    raichu = "npc/animals/wolf_corpse"
                elif snorlax.cmd == "boarcorpse":
                    raichu = "npc/animals/boar_corpse"
                elif snorlax.cmd == "stagcorpse":
                    raichu = "npc/animals/stag_corpse"
                #Trees
                elif snorlax.cmd == "snowtree1":
                    raichu = "autospawn/Tree-G-Snow-1"
                elif snorlax.cmd == "snowtree2":
                    raichu = "autospawn/Tree-F-Snow-1"
                elif snorlax.cmd == "tree1":
                    raichu = "autospawn/Tree-G-1"
                elif snorlax.cmd == "tree2":
                    raichu = "autospawn/Tree-F-1"
                elif snorlax.cmd == "tree3":
                    raichu = "autospawn/TreeE2-1"
                elif snorlax.cmd == "tree4":
                    raichu = "autospawn/Tree-G-1"
                elif snorlax.cmd == "tree5":
                    raichu = "autospawn/Tree-C-1"
                elif snorlax.cmd == "foresttree1":
                    raichu = "autospawn/forest_4_tree_1"
                elif snorlax.cmd == "foresttree2":
                    raichu = "autospawn/forest_4_tree_4"
                elif snorlax.cmd == "foresttree3":
                    raichu = "autospawn/forest_4_tree_2"
                elif snorlax.cmd == "foresttree4":
                    raichu = "autospawn/forest_4_tree_3"
                elif snorlax.cmd == "foresttree5":
                    raichu = "autospawn/forest_4_tree_5"
                elif snorlax.cmd == "fieldtree1":
                    raichu = "autospawn/Fields-North-1"
                elif snorlax.cmd == "fieldtree2":
                    raichu = "autospawn/Fields-Mid-1"
                elif snorlax.cmd == "fieldtree3":
                    raichu = "autospawn/Tree-A-1"
                if 10 >= count > 0:
                    while num is not count and raichu is not None:
                        World.SpawnMapEntity(raichu, loc.x, loc.y, loc.z)
                        num += 1
                else:
                    snorlax.User.Message("Please use 1 - 10, anything more would cause lag.")
                    return
            elif snorlax.cmd == "spawnhelp":
                if snorlax.quotedArgs[0] == "entities":
                    snorlax.User.Message("List of Current Entities:")
                    for e in teamash:
                        snorlax.User.Message(e)
                elif snorlax.quotedArgs[0] == "animals":
                    snorlax.User.Message("List of Current Animals:")
                    for a in teamrocket:
                        snorlax.User.Message(a)
                    return
                else:
                    msgtousr = ("->Entity Spawner by CorrosionX - Special thanks to balu92 & xEnt",
                                "To spawn entities, use \"/animalname #\" or \"/entityname #\"",
                                "For Lists:\"/spawnerhelp entities\" or \"/spawnerhelp animals\"")
                    for msg in msgtousr:
                        snorlax.User.Message(msg)
                    return
            elif snorlax.cmd == "test":
                World.AttachParachute(snorlax.User)
                return