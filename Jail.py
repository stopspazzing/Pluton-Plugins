import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class Jail:
    def On_PluginInit(self):
        Commands.Register("jail")\
            .setCallback("jailplayer")\
            .setDescription("Jail a player in a box")\
            .setUsage("jail john")

    def On_Command(self, cmd):
        jailed = DataStore.Get("jailed", cmd.User.GameID)
        if len(cmd.quotedArgs) > 0 and jailed:
            cmd.User.Message("You are in Jail, can't use commands you convict!")
            return

    def jailplayer(self, args, player):
        if player.Admin:
            jailedpl = self.CheckV(player, args[0])
            if jailedpl is not None:
                DataStore.Add("jailed", jailedpl.GameID, True)
                myX = jailedpl.X
                myY = jailedpl.Y
                myZ = jailedpl.Z
                self.bbuild(jailedpl, "build/wall", myX-1.5, myY, myZ, 0)
                self.bbuild(jailedpl, "build/wall", myX+1.5, myY, myZ, 0)
                self.bbuild(jailedpl, "build/wall", myX, myY, myZ-1.5, 90)
                self.bbuild(jailedpl, "build/wall", myX, myY, myZ+1.5, 90)
                self.bbuild(jailedpl, "build/floor", myX, myY+3, myZ, 0)
                self.bbuild(jailedpl, "build/floor", myX, myY, myZ, 0)

    def bbuild(self, fplayer, which, x, y, z, rot):
        block = World.SpawnMapEntity(which, x, y, z)
        block.health = 515
        block.deployerUserName = fplayer.Name
        block.deployerUserID = fplayer.GameID
        block.transform.Rotate(0, rot, 0)
        block.SendNetworkUpdate()

    def On_Chat(self, chat):
        jailed = DataStore.Get("jailed", chat.User.GameID)
        if len(chat.args) > 0 and jailed:
            chat.User.Message("You are in Jail, can't use commands you convict!")
            return

    def GetPlayerName(self, namee):
        name = namee.lower()
        for pl in Server.ActivePlayers:
            if pl.Name.lower() == name:
                return pl
        return None

    def CheckV(self, Player, args):
        systemname = "Jail"
        count = 0
        if hasattr(args, '__len__') and (not isinstance(args, str)):
            p = self.GetPlayerName(String.Join(" ", args))
            if p is not None:
                return p
            for pl in Server.ActivePlayers:
                for namePart in args:
                    if namePart.lower() in pl.Name.lower():
                        p = pl
                        count += 1
                        continue
        else:
            p = self.GetPlayerName(str(args))
            if p is not None:
                return p
            s = str(args).lower()
            for pl in Server.ActivePlayers:
                if s in pl.Name.lower():
                    p = pl
                    count += 1
                    continue
        if count == 0:
            Player.MessageFrom(systemname, "Couldn't find " + String.Join(" ", args) + "!")
            return None
        elif count == 1 and p is not None:
            return p
        else:
            Player.MessageFrom(systemname, "Found " + str(count) + " player with similar name. Use more correct name!")
            return None