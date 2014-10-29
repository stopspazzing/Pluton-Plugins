import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class Jail:
    def On_Command(self, cmd):
        jailed = DataStore.Get("jailed", cmd.User.GameID)
        if cmd.quotedArgs[0] > 0 and jailed:
            cmd.User.Message("You are in Jail, can't use commands you convict!")
            return

        if cmd.cmd == "jail" and cmd.User.Admin:
            jailedpl = Server.Players.Find(cmd.quotedArgs[0]).ToPlayer()
            if jailedpl is not None:
                DataStore.Add("remove", jailedpl.GameID, True)
                myX = jailedpl.X
                myY = jailedpl.Y
                myZ = jailedpl.Z
                self.bbuild(jailedpl, "build/generic_wall", myX-1.5, myY, myZ, 0)
                self.bbuild(jailedpl, "build/generic_wall", myX+1.5, myY, myZ, 0)
                self.bbuild(jailedpl, "build/generic_wall", myX, myY, myZ-1.5, 90)
                self.bbuild(jailedpl, "build/generic_wall", myX, myY, myZ+1.5, 90)
                self.bbuild(jailedpl, "build/generic_floor", myX, myY+3, myZ, 0)
                self.bbuild(jailedpl, "build/generic_floor", myX, myY, myZ, 0)

    def bbuild(self, fplayer, which, x, y, z, rot):
        block = World.SpawnMapEntity(which, x, y, z)
        block.health = 515
        block.deployerUserName = fplayer.Name
        block.deployerUserID = fplayer.GameID
        block.transform.Rotate(0, rot, 0)
        block.SendNetworkUpdate()

    def On_Chat(self, chat):
        jailed = DataStore.Get("jailed", chat.User.GameID)
        if chat.args > 0 and jailed:
            chat.User.Message("You are in Jail, can't use commands you convict!")
            return
