__author__ = 'Corrosion X'
__version__ = '1.0'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class EasySuicide:
    def On_PlayerConnected(self, p):
        p.MessageFrom("[EasySuicide]", "Use /die to suicide easily")
    def On_PluginInit(self):
         charmeleon = (" took the easy way out",
                       " tripped and split his dick open",
                       " fell asleep under the sun and burnt to a crisp",
                       " wanted to feed the roses",
                       " wanted a better spawn",
                       " now has 8 lives",
                       " thought is was a good idea to pull the pin of a grenade",
                       " overdosed on Rad Pills",
                       " deleted System32",
                       " tried to rock a wolf",
                       " took an arrow to the knee, didn\"t recover",
                       " thought it was a good idea to look down the barrel of his gun",
                       " believed he could fly",
                       " figured out how C4 works",
                       " thought he was Chuck Norris",
                       " took the red pill",
                       " tried to enter the cheat console with alt + f4")
         warturtle = ("A naked army took out ")
         if not Plugin.IniExists("responses"):
             psyduck = Plugin.CreateIni("responses")
             psyduck.AddSetting("PlayerResponses", charmeleon)
             psyduck.AddSetting("ResponsesPlayer", warturtle)

    def On_Command(self, charizard):
        teamrocket = ("suicide", "sui", "killme", "die", "slay", "suicidal")
        if charizard.cmd in teamrocket:
            charizard.User.Kill()  # Kill him with a thunderbolt

    def On_PlayerDied(self, chansey):
        World.SpawnAnimal("bear", chansey.Victim.Location)
        World.SpawnAnimal("wolf", chansey.Victim.Location)