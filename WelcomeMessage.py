__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'WelcomeMessage'
import clr
import sys
clr.AddReferenceByPartialName("Pluton")
import Pluton


class WelcomeMessage:
    def On_PlayerConnected(self, p):
        p.Message("Welcome " + p.Name + "!")
        p.Message(str.format("This server is powered by Pluton[v{0}]!", Pluton.Bootstrap.Version))
        p.Message("Visit pluton-team.org for more information or to report bugs!")