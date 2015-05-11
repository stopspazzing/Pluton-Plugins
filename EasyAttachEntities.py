__author__ = "Corrosion X"
__version__ = '1.0'
__name__ = 'EasyAttachEntities'
# Massive thanks to DreTaX for getting custom function imported from c# working
import clr
clr.AddReferenceByPartialName("Pluton")
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Assembly-CSharp")
import Pluton
import UnityEngine
from UnityEngine import Vector3
from UnityEngine import Quaternion
parts = ("l_upperarm", "r_upperarm", "head", "l_knee", "r_knee", "spine1", "spine2", "spine3", "spike4",
         "l_hand", "r_hand", "r_hip", "l_hip", "l_eye", "r_eye", "l_toe", "r_toe", "pelvis", "l_clavicle",
         "r_clavicle", "r_forearm", "l_forearm", "r_ulna", "l_ulna", "r_foot", "l_foot", "neck", "jaw")
try:
    import GameManager as importedclass
except ImportError:
    pass


class EasyAttachEntities:

    DefaultVector = None
    Quat = None

    def On_PluginInit(self):
        self.DefaultVector = Vector3(0, 0, 0)
        self.Quat = Quaternion(0, 0, 0, 1)
        Commands.Register("attach")\
            .setCallback("attach")\
            .setDescription("your description here")\
            .setUsage("The usage here")
        Commands.Register("attanimal")\
            .setCallback("attanimal")\
            .setDescription("your description here")\
            .setUsage("The usage here")
        Commands.Register("detach")\
            .setCallback("detach")\
            .setDescription("your description here")\
            .setUsage("The usage here")
        Commands.Register("test")\
            .setCallback("test")\
            .setDescription("your description here")\
            .setUsage("The usage here")

    def AttachToPlayer(self, Player, whatthing, towhere, Spawn01=False):
        e = Player.basePlayer
        people = importedclass.server.CreateEntity(whatthing, self.DefaultVector, self.Quat)
        if people:
            people.SetParent(e, towhere)
            people.Spawn(Spawn01)
        return people

    def AttachToAnimal(self, animal, whatthing, towhere, Spawn01=False):
        animals = importedclass.server.CreateEntity(whatthing, self.DefaultVector, self.Quat)
        if animals:
            animals.SetParent(animal, towhere)
            animals.Spawn(Spawn01)
        return animals

    def TimedExplosive(self, parent):
        explosive = importedclass.server.CreateEntity("items/timed.explosive.deployed", self.DefaultVector, self.Quat)
        if explosive:
            explosive.timerAmountMin = 3
            explosive.timerAmountMax = 4
            explosive.explosionRadius = 100
            ##explosive.damage = 2000
            explosive.SetParent(parent, "head")
            explosive.Spawn(True)
        return explosive

    def attach(self, args, player):
        quoted = Util.GetQuotedArgs(args)
        whatthing = quoted[0]
        towhere = quoted[1]
        attached = self.AttachToPlayer(player, whatthing, towhere, True)
        player.Message("Attached entity to your " + towhere + "!")
        DataStore.Add("attached", player.SteamID, attached)

    def attachanimal(self, args, player):
        quoted = Util.GetQuotedArgs(args)
        animal = quoted[0]
        whatthing = quoted[1]
        towhere = quoted[2]
        animals = World.SpawnAnimal(animal, player.Location)
        attached = self.AttachToAnimal(animals, whatthing, towhere, true)
        DataStore.Add("attachanimal", player.SteamID, attached)

    def detach(self, args, player):
        quoted = Util.GetQuotedArgs(args)
        removewhat = quoted[0]
        if len(removewhat) == 0:
            player.Message("Choices are: all, attach, attanimal; Please try again")
            return
        isattached = DataStore.Get("attached", player.SteamID)
        moreattached = DataStore.Get("attachanimal", player.SteamID)
        if isattached is not None or moreattached is not None:
            if removewhat == "all":
                Util.DestroyEntity(isattached)
                Util.DestroyEntity(moreattached)
                player.Message("Everything has been destroyed!")
            elif removewhat == "attach":
                Util.DestroyEntity(isattached)
                player.Message("Entities Attached Have Been Removed!")
            elif removewhat == "attanimal":
                Util.DestroyEntity(moreattached)
                player.Message("Attached Animals Removed!")
        else:
            player.Message("You dont have anything attached!")

    def test(self, unused, player):
        attached = self.AttachToPlayer(player, "weapons/melee/boneknife.weapon", "head", True)
        self.TimedExplosive(attached)
        DataStore.Add("attached", player.SteamID, attached)
        player.Message("Attached entity to your head!")