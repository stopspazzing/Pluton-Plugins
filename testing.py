import re
check = "arrow"
string = ("player/player", "npc/animals/player_corpse", "npc/animals/wolf_corpse",
            "npc/animals/boar_corpse", "npc/animals/bear_corpse", "npc/animals/stag_corpse",
            "items/arrow", "items/supply_drop", "items/woodbox_deployed", "items/campfire_deployed",
            "items/lantern_deployed", "build/generic_foundation_triangle", "build/generic_wall",
            "build/generic_foundation_steps", "build/generic_floor", "build/generic_stairs",
            "build/generic_window", "build/generic_wooden_hinged_door", "build/generic_door",
            "build/generic_foundation", "autospawn/resources/forest4/forest_4_tree_1",
            "autospawn/resources/forest4/forest_4_tree_3", "autospawn/resources/forest4/forest_4_tree_4",
            "autospawn/resources/forest3/tree-c-1", "autospawn/resources/forest3/tree-g-1",
            "autospawn/resources/fields1/tree-a-1", "autospawn/resources/forest5/treee2-1",
            "autospawn/resources/forest6/tree-g-1", "autospawn/resources/forest4/forest_4_tree_2",
            "autospawn/resources/fields2/fields-mid-1", "autospawn/resources/forest7/tree-g-snow-1",
            "autospawn/resources/forest6/tree-f-1", "autospawn/resources/forest7/tree-f-snow-1",
            "autospawn/resources/fields3/fields-north-1", "autospawn/resource/forestedge7/tree-g-snow-1",
            "autospawn/resource/forestedge6/tree-g-1", "autospawn/resource/forestedge4/treee2-1",
            "autospawn/resource/forestedge4/fields-mid-2", "autospawn/resource/forestedge1/tree-a-1",
            "autospawn/resource/fields3/fields-north-1", "autospawn/resource/fields2/fields-mid-1",
            "autospawn/resource/fields1/tree-a-1", "autospawn/resource/ores/resource_ore_stone",
            "autospawn/resource/ores/resource_ore_sulfur", "autospawn/resource/ores/resource_ore_metal",
            "autospawn/resource/piles/resource_pile_wood", "autospawn/resource/forest7/tree-f-snow-1",
            "autospawn/resource/forest6/tree-f-1", "autospawn/resource/forest4/treee-1",
            "autospawn/resource/forest1/tree-c-1", "weapons/melee/hatchet_wm",
            "weapons/shotgun/waterpipe_wm", "weapons/melee/boneknife_wm", "weapons/smg/thompson_wm",
            "weapons/tool/hammer_wm", "weapons/rifle/bolt_wm")


for each in string:
    if check in each:
        print each
        break

    #keys = re.findall(r'[^/]+$', each)
    #sentence = re.sub('[[\]_\-\']', '', str(keys))
    #print sentence