__author__ = 'Corrosion X'
__version__ = '0.5'
__name__ = 'EasyAnimalConfig'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton
import re
from UnityEngine import Random


class EasyAnimalConfig:
    def On_PluginInit(self):
        Plugin.CreateTimer("marked", 60000).Start()

    def On_PlayerConnected(self, player):
        player.Message("Animals take 50% less dmg, try not to kill too many...")

    def On_PlayerDisconnected(self, player):
        DataStore.Remove("marked4death", player.GameID)

    def On_PlayerDied(self, player):
        DataStore.Remove("marked4death", player.GameID)

    def On_PlayerGathering(self, ge):
        num = int(Random.Range(0, 10))
        hp = ge.Health
        player = ge.Gatherer
        if num == 5 and hp <= 0:
            player.Message("Oh noes! You found a hibernating bear!")
            World.SpawnAnimal("bear", player.Location)

    def On_NPCAttacked(self, npa):
        #baseplayer = npa.Attacker.ToPlayer()
        #player = Server.Players[baseplayer.userID]
        #npc = npa.Victim
        npa.DamageAmount /= 2
        #npc.Location = player.Location
        #npc.baseAnimal = player.Location
        #npc.baseAnimal.transform.position.Set(player.Location)
        #npc.baseAnimal.pos = player.Location

    def On_NPCKilled(self, nde):
        baseplayer = nde.Attacker.ToPlayer()
        player = Server.Players[baseplayer.userID]
        npc = nde.Victim
        npcname = npc.Name
        npcname = re.sub("\(Clone\)", "", npcname)
        player.Message("You have angered the " + npcname + " Gods!")
        kills = DataStore.Get("kills", player.GameID)
        if kills is None:
            kills = 2
        elif kills < 10:
            kills += 1
        elif kills >= 10:
            kills = 2
            DataStore.Add("marked4death", player.GameID, True)
            player.Message("You have been marked for death!")
        DataStore.Add("kills", player.GameID, kills)
        for c in xrange(0, kills):
            World.SpawnAnimal(npcname, npc.Location)
        return

    def markedCallback(self, unused):
        for id, pl in Server.Players.Keys:
            marked = DataStore.Get("marked4death", pl.GameID)
            if marked:
                n = 3
                pl.MessageFrom("Mr. Bear", "I hope you learn your lesson!")
                DataStore.Add("marked4death", player.GameID, False)
                for c in xrange(0, n):
                    World.SpawnAnimal("wolf", pl.Location)
                    World.SpawnAnimal("bear", pl.Location)
                return
        return