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
        DataStore.Flush("marked4death")

    def On_PlayerConnected(self, player):
        player.Message("Animals take 200% less dmg, try not to kill too many...")

    def On_PlayerDisconnected(self, player):
        DataStore.Remove("marked4death", player.GameID)

    def On_PlayerDied(self, pde):
        DataStore.Remove("marked4death", pde.Victim.GameID)

    def On_PlayerGathering(self, ge):
        num = int(Random.Range(0, 10))
        hp = ge.Health
        player = ge.Gatherer
        if hp <= 1 and num == 5:
            player.Message("Oh noes! You found a hibernating bear!")
            World.SpawnAnimal("bear", player.Location)

    def On_NPCAttacked(self, npa):
        #baseplayer = npa.Attacker.ToPlayer()
        #player = Server.Players[baseplayer.userID]
        #npc = npa.Victim
        npa.DamageAmount /= 200
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
        kills = DataStore.Get("kills", player.GameID)
        marked = bool(DataStore.Get("marked4death", player.GameID))
        timer = int(Random.Range(30, 180))
        #player.Message("timer set")
        if not marked:
            #player.Message("You have angered the " + npcname + " Gods!")
            if kills is None:
                kills = 1
            elif kills < 10:
                kills += 1
            elif kills >= 10:
                kills = 1
                DataStore.Add("marked4death", player.GameID, True)
                pldict = Plugin.CreateDict()
                pldict["uid"] = player.GameID
                time = int(timer)*1000
                Plugin.CreateParallelTimer("marked", time, pldict).Start()
                player.Message("You have been marked for death!")
        DataStore.Add("kills", player.GameID, kills)
        for c in xrange(0, kills):
            World.SpawnAnimal(npcname, npc.Location)
            return

    def markedCallback(self, timer):
        pldict = timer.Args
        userid = pldict["uid"]
        n = 3
        DataStore.Remove("marked4death", userid)
        player = Server.Players[userid]
        player.MessageFrom("Animal Gods", "I hope you learn your lesson!")
        for c in xrange(0, n):
            World.SpawnAnimal("wolf", player.Location)
            World.SpawnAnimal("bear", player.Location)
            return
        timer.Kill()