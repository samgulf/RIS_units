import pandas as pd

class ris_unit:
    """
    Contains a Rome Imperium Surrectum unit type 
    Assumes data structures as per: https://www.twcenter.net/forums/showthread.php?111344-The-Complete-EDU-Guide
    """
    def __init__(self, input_string:str) -> None:
        data = {}
        regions = []

        # There can be multiple lines with regions and ethnicities, so capture them all
        ethnicities = []
        for line in input_string.splitlines():
            line = line.replace(",","")
            line = line.split()
            if type(line) is list and len(line) > 1:
                if line[0][0:9] == 'ethnicity':
                    #print(line)
                    if line[2] not in regions:
                        regions.append(line[2])
                    if line[1] not in ethnicities:
                        ethnicities.append(line[1])
                else:
                    data[line[0]] = line[1:]

        self.type = " ".join(data["type"])
        self.category = data["category"][0]
        self.unit_class = data["class"][0]
        self.hp = int(data["stat_health"][0])
        self.attack = int(data["stat_pri"][0])
        self.sec_attack = int(data["stat_sec"][0])
        self.charge = int(data["stat_pri"][1])
        self.def_skill = int(data["stat_pri_armour"][1])
        self.armour = int(data["stat_pri_armour"][0])
        self.shield = int(data["stat_pri_armour"][2])
        self.missile_range = int(data["stat_pri"][3])
        self.missile_ammo = int(data["stat_pri"][4])
        self.recruit_cost = int(data["stat_cost"][1])
        self.upkeep_cost = int(data["stat_cost"][2])
        self.attributes =  ", ".join(data["attributes"])

        # The formations are either Square, Horde, or Square + Something (with the Something in space 6)
        # We don't really care about Square or Horde, so just take whatever is in 6
        try:
            self.formations = data["formation"][6]
        except:
            self.formations = ""

        self.weapon_type = data["stat_pri"][5]
        self.weapon_attr = ", ".join(data["stat_pri_attr"])  
        self.hp_extra = int(data["stat_health"][1])    
        self.sec_charge = int(data["stat_sec"][1])
        self.sec_weapon_type = data["stat_sec"][5]
        self.sec_weapon_attr = ", ".join(data["stat_sec_attr"])       
        self.sec_armour = int(data["stat_sec_armour"][0])
        self.sec_def_skill = int(data["stat_sec_armour"][1])
        self.heat = int(data["stat_heat"][0])
        self.scrub_mdf = int(data["stat_ground"][0])
        self.sand_mdf = int(data["stat_ground"][1])
        self.forest_mdf = int(data["stat_ground"][2])
        self.snow_mdf = int(data["stat_ground"][3])
        self.morale = int(data["stat_mental"][0])
        self.discipline = data["stat_mental"][1]
        self.training = data["stat_mental"][2]
        self.charge_distance = int(data["stat_charge_dist"][0])
        self.recruit_turns = int(data["stat_cost"][0])
        self.weapon_upgrade_cost = int(data["stat_cost"][3])
        self.armour_upgrade_cost = int(data["stat_cost"][4])
        self.custom_battle_cost = int(data["stat_cost"][5])

        # Flag AoR units
        if data["type"][0] == "aor":
            self.aor = True
        else:
            self.aor = False

        # For AoR units the ownership is set to all, but the ethinicities break this down into specific factions
        if data["ownership"] == ["all"] and len(ethnicities) > 0:
            ethnicities.sort()
            self.ownership = ", ".join(ethnicities)
        else:
            data["ownership"].sort()
            self.ownership = ", ".join(data["ownership"])

        # There shouldn't be multiple regions for a unit - if there are, flag that because the code needs updating
        if len(regions) > 0:
            self.region = regions[0]
        else:
            self.region = ""
        if len(regions) > 1:
            print(self.type)
            print(regions)
        
        self.dictionary = data["dictionary"][0]

    def add_name(self, name:str) -> None:
        self.name = name.strip()

    def add_short_desc(self, short_desc:str) -> None:
        self.short_desc = short_desc

    def add_long_desc(self, long_desc:str) ->None:
        self.long_desc = long_desc

    def to_series(self):
        return pd.Series(vars(self))