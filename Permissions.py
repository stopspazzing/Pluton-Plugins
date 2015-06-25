__author__ = 'Corrosion X'
__version__ = '0.1'
__name__ = 'Permissions'
import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
import Pluton


class Permissions:
    def On_PluginInit(self):
        ##create perm. file if doesnt exist or load it if does
        if not Plugin.IniExists("Permissions"):
            setini = Plugin.CreateIni("Permissions")
            setini.Save()
        Commands.Register("permission")\
            .setCallback("permission")\
            .setDescription("Allow admin to add and remove permissions")\
            .setUsage("/permission add username permission")
        ##register commands for adding permissions

    def On_PlayerConnected(self, player):
        ##check what perms they have from perm file if not give them "default"
        ##For admins override all, for moderators have defined set amount

    def On_CommandPermission(self, cpe):
        player = cpe.player
        if player is not player.Admin:
            playerid = player.SteamID
            name = player.Name
            command = cpe.command
            ini = Plugin.GetIni("Permissions")
            ini2 = Plugin.GetIni("Settings")
            debug = bool(ini2.GetSetting("Settings", Debug))
            ##setting = ini.GetSetting(playerid, "Permissions")
            setting = ini.GetSetting(PluginName(), command)
            if setting is None or playerid not in setting:
                BlockCommand("You Don't Have Permissions For That!")
                if not debug:
                    Util.Log(name + " with steamid " + playerid + " attempted to executed command " + command +
                             " from plugin " + plugin.Name)
            elif debug:
                Util.Log(name + " with steamid " + playerid + " executed command " + command + " from plugin " +
                         plugin.Name)
            ##Check when player executes command if they have permissions to do so else prevent

    def permissionsCallback(self, player, args):
        if not player.isAdmin:
            player.Message("Only admins can modify permissions!")
            return
        if len(args) == 0:
            player.Message("Use /permission add/remove username permission")
            return
        quoted = Util.GetQuotedArgs(args)

