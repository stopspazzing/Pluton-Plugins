__author__ = 'Corrosion X'
__version__ = '0.5'
__name__ = 'EasyAnimalConfig'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class EasyAnimalConfig:
    def On_PluginInit(self):
        Plugin.CreateTimer("marked", 60000).Start()

    def On_PlayerConnected(self, player):
        player.Message("Animals take 50% less dmg, try not to kill too many...")

    def On_NPCAttacked(self, npa):
        baseplayer = npa.Attacker.ToPlayer()
        player = Server.Players[baseplayer.userID]
        npc = npa.Victim
        npa.DamageAmount /= 2
        #npc.Location = player.Location
        #npc.baseAnimal = player.Location
        #npc.baseAnimal.transform.position.Set(player.Location)
        npc.baseEntity.pos = player.Location
        player.Message("You have angered Mr. " + npc.Name)

    def On_NPCDeathEvent(self, nde):
        baseplayer = npa.Attacker.ToPlayer()
        player = Server.Players[baseplayer.userID]
        npc = nde.Victim
        kills = DataStore.Get("kills", player.GameID)
        if kills is None:
            kills = 2
        elif kills > 10:
            kills += 1
        else:
            kills = 2
            DataStore.Add("marked4death", player.GameID, True)
            player.Message("You have been marked for death!")
        DataStore.Add("kills", player.GameID, kills)
        for c in xrange(0, kills):
            World.SpawnAnimal(npc, npc.Location)
        return

    def On_PlayerDisconnected(self, pl):
        DataStore.Remove("kills", pl.SteamID)

    def markedCallback(self, timer):
        for pl in Server.Players:
            marked = DataStore.Get("marked4death", pl.GameID)
            if marked:
                n = 3
                pl.MessageFrom("Mr. Bear", "I hope you learn your lesson!")
                for c in xrange(0, n):
                    World.SpawnAnimal("wolf", pl.Location)
                    World.SpawnAnimal("bear", pl.Location)
                return
        return