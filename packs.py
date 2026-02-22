from dataclasses import dataclass
from collections import Counter
from parts import Blades, Ratchets, Bits, LockChip, MainBlade, AssistBlade

@dataclass(frozen=True)
class Pack:
    name: str
    parts: Counter  # Part -> count

    def __hash__(self):
        # Only hash by name, which is unique
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Pack):
            return False
        return self.name == other.name

xtreme_battle_set = Pack(
    name="xtreme_battle_set",
    parts=Counter([
        Blades.DAGGER_DRAN,
        Blades.TUSK_MAMMOTH,
        Ratchets._4_60,
        Ratchets._3_60,
        Bits.RUSH,
        Bits.TAPER
    ])
)

soar_phoenix_single = Pack(
    name="soar_phoenix_single",
    parts=Counter([
        Blades.SOAR_PHOENIX,
        Ratchets._9_60,
        Bits.GEAR_FLAT
    ])
)

tail_viper_sword_dran_double = Pack(
    name="tail_viper_sword_dran_double",
    parts=Counter([
        Blades.TAIL_VIPER,
        Blades.SWORD_DRAN,
        Ratchets._5_80,
        Ratchets._3_60,
        Bits.ORB,
        Bits.FLAT
    ])
)

chain_incendio_arrow_wizard_double = Pack(
    name="chain_incendio_arrow_wizard_double",
    parts=Counter([
        Blades.CHAIN_INCENDIO,
        Blades.ARROW_WIZARD,
        Ratchets._5_60,
        Ratchets._4_60,
        Bits.HIGH_TAPER,
        Bits.NEEDLE
    ])
)

knife_shinobi_keel_shark_double = Pack(
    name="knife_shinobi_keel_shark_double",
    parts=Counter([
        Blades.KNIFE_SHINOBI,
        Blades.KEEL_SHARK,
        Ratchets._4_80,
        Ratchets._3_80,
        Bits.HIGH_NEEDLE,
        Bits.FLAT
    ])
)

sword_dran_single = Pack(
    name="sword_dran_single",
    parts=Counter([
        Blades.SWORD_DRAN,
        Ratchets._3_60,
        Bits.FLAT
    ])
)

scythe_incendio_single = Pack(
    name="scythe_incendio_single",
    parts=Counter([
        Blades.SCYTHE_INCENDIO,
        Ratchets._4_60,
        Bits.TAPER
    ])
)

arrow_wizard_single = Pack(
    name="arrow_wizard_single",
    parts=Counter([
        Blades.ARROW_WIZARD,
        Ratchets._4_80,
        Bits.BALL
    ])
)

helm_knight_single = Pack(
    name="helm_knight_single",
    parts=Counter([
        Blades.HELM_KNIGHT,
        Ratchets._3_80,
        Bits.NEEDLE
    ])
)

talon_ptera_single = Pack(
    name="talon_ptera_single",
    parts=Counter([
        Blades.TALON_PTERA,
        Ratchets._3_80,
        Bits.BALL
    ])
)

horn_rhino_single = Pack(
    name="horn_rhino_single",
    parts=Counter([
        Blades.HORN_RHINO,
        Ratchets._3_80,
        Bits.SPIKE
    ])
)

steel_samurai_single = Pack(
    name="steel_samurai_single",
    parts=Counter([
        Blades.STEEL_SAMURAI,
        Ratchets._4_80,
        Bits.TAPER
    ])
)

keel_shark_single = Pack(
    name="keel_shark_single",
    parts=Counter([
        Blades.KEEL_SHARK,
        Ratchets._3_60,
        Bits.LOW_FLAT
    ])
)

yell_kong_helm_knight_double = Pack(
    name="yell_kong_helm_knight_double",
    parts=Counter([
        Blades.YELL_KONG,
        Ratchets._3_60,
        Bits.GEAR_BALL,
        Blades.HELM_KNIGHT,
        Ratchets._5_80,
        Bits.TAPER
    ])
)

gale_wyvern_tail_viper_double = Pack(
    name="gale_wyvern_tail_viper_double",
    parts=Counter([
        Blades.GALE_WYVERN,
        Ratchets._5_80,
        Bits.GEAR_BALL,
        Blades.TAIL_VIPER,
        Ratchets._3_80,
        Bits.HIGH_NEEDLE
    ])
)

bite_croc_sting_unicorn_double = Pack(
    name="bite_croc_sting_unicorn_double",
    parts=Counter([
        Blades.BITE_CROC,
        Ratchets._3_60,
        Bits.LOW_FLAT,
        Blades.STING_UNICORN,
        Ratchets._4_60,
        Bits.POINT
    ])
)

lance_knight_single = Pack(
    name="lance_knight_single",
    parts=Counter([
        Blades.LANCE_KNIGHT,
        Ratchets._4_80,
        Bits.HIGH_NEEDLE
    ])
)

claw_leon_single = Pack(
    name="claw_leon_single",
    parts=Counter([
        Blades.CLAW_LEON,
        Ratchets._5_60,
        Bits.POINT
    ])
)

roar_tyranno_single = Pack(
    name="roar_tyranno_single",
    parts=Counter([
        Blades.ROAR_TYRANNO,
        Ratchets._9_60,
        Bits.GEAR_FLAT
    ])
)

savage_bear_single = Pack(
    name="savage_bear_single",
    parts=Counter([
        Blades.SAVAGE_BEAR,
        Ratchets._3_60,
        Bits.SPIKE
    ])
)

scythe_incendio_yellow_single = Pack(
    name="scythe_incendio_yellow_single",
    parts=Counter([
        Blades.SCYTHE_INCENDIO,
        Ratchets._3_80,
        Bits.BALL
    ])
)

sting_unicorn_single = Pack(
    name="sting_unicorn_single",
    parts=Counter([
        Blades.STING_UNICORN,
        Ratchets._5_60,
        Bits.GEAR_POINT
    ])
)

beat_tyranno_knife_shinobi_double = Pack(
    name="beat_tyranno_knife_shinobi_double",
    parts=Counter([
        Blades.BEAT_TYRANNO,
        Ratchets._4_70,
        Bits.QUAKE,
        Blades.KNIFE_SHINOBI,
        Ratchets._4_80,
        Bits.HIGH_NEEDLE
    ])
)

gale_wyvern_sword_dran_double = Pack(
    name="gale_wyvern_sword_dran_double",
    parts=Counter([
        Blades.GALE_WYVERN,
        Ratchets._3_60,
        Bits.TAPER,
        Blades.SWORD_DRAN,
        Ratchets._3_80,
        Bits.BALL
    ])
)

cowl_sphinx_single = Pack(
    name="cowl_sphinx_single",
    parts=Counter([
        Blades.COWL_SPHINX,
        Ratchets._9_80,
        Bits.GEAR_NEEDLE
    ])
)

arrow_wizard_purple_single = Pack(
    name="arrow_wizard_purple_single",
    parts=Counter([
        Blades.ARROW_WIZARD,
        Ratchets._4_80,
        Bits.GEAR_BALL
    ])
)

buster_dran_single = Pack(
    name="buster_dran_single",
    parts=Counter([
        Blades.BUSTER_DRAN,
        Ratchets._1_60,
        Bits.ACCEL
    ])
)

wand_wizard_single = Pack(
    name="wand_wizard_single",
    parts=Counter([
        Blades.WAND_WIZARD,
        Ratchets._5_70,
        Bits.DISK_BALL
    ])
)

cobalt_dragoon_single = Pack(
    name="cobalt_dragoon_single",
    parts=Counter([
        Blades.COBALT_DRAGOON,
        Ratchets._2_60,
        Bits.CYCLONE
    ])
)

shadow_shinobi_single = Pack(
    name="shadow_shinobi_single",
    parts=Counter([
        Blades.SHADOW_SHINOBI,
        Ratchets._1_80,
        Bits.METAL_NEEDLE
    ])
)

wand_wizard_green_single = Pack(
    name="wand_wizard_green_single",
    parts=Counter([
        Blades.WAND_WIZARD,
        Ratchets._1_60,
        Bits.RUSH
    ])
)

hammer_incendio_single = Pack(
    name="hammer_incendio_single",
    parts=Counter([
        Blades.HAMMER_INCENDIO,
        Ratchets._3_70,
        Bits.HEXA
    ])
)

buster_dran_yellow_single = Pack(
    name="buster_dran_yellow_single",
    parts=Counter([
        Blades.BUSTER_DRAN,
        Ratchets._5_70,
        Bits.DISK_BALL
    ])
)

keel_shark_black_single = Pack(
    name="keel_shark_black_single",
    parts=Counter([
        Blades.KEEL_SHARK,
        Ratchets._1_60,
        Bits.QUAKE
    ])
)

yell_kong_single = Pack(
    name="yell_kong_single",
    parts=Counter([
        Blades.YELL_KONG,
        Ratchets._3_60,
        Bits.GEAR_BALL
    ])
)

obsidian_shell_single = Pack(
    name="obsidian_shell_single",
    parts=Counter([
        Blades.OBSIDIAN_SHELL,
        Ratchets._4_60,
        Bits.DOT
    ])
)

soar_phoenix_blue_single = Pack(
    name="soar_phoenix_blue_single",
    parts=Counter([
        Blades.SOAR_PHOENIX,
        Ratchets._5_80,
        Bits.HEXA
    ])
)

pearl_tiger_gill_shark_double = Pack(
    name="pearl_tiger_gill_shark_double",
    parts=Counter([
        Blades.PEARL_TIGER,
        Ratchets._3_60,
        Bits.UNITE,
        Blades.GILL_SHARK,
        Ratchets._4_70,
        Bits.ORB
    ])
)

cowl_sphinx_crest_leon_double = Pack(
    name="cowl_sphinx_crest_leon_double",
    parts=Counter([
        Blades.COWL_SPHINX,
        Ratchets._1_80,
        Bits.GEAR_FLAT,
        Blades.CREST_LEON,
        Ratchets._7_60,
        Bits.GEAR_NEEDLE
    ])
)

scarlet_garuda_single = Pack(
    name="scarlet_garuda_single",
    parts=Counter([
        Blades.SCARLET_GARUDA,
        Ratchets._4_70,
        Bits.TRANS_POINT
    ])
)

sterling_wolf_single = Pack(
    name="sterling_wolf_single",
    parts=Counter([
        Blades.STERLING_WOLF,
        Ratchets._3_80,
        Bits.FREE_BALL
    ])
)

tide_whale_single = Pack(
    name="tide_whale_single",
    parts=Counter([
        Blades.TIDE_WHALE,
        Ratchets._5_80,
        Bits.ELEVATE
    ])
)

dagger_dran_single = Pack(
    name="dagger_dran_single",
    parts=Counter([
        Blades.DAGGER_DRAN,
        Ratchets._4_70,
        Bits.QUAKE
    ])
)

dark_perseus_single = Pack(
    name="dark_perseus_single",
    parts=Counter([
        LockChip.PERSEUS,
        MainBlade.DARK,
        AssistBlade.BUMPER,
        Ratchets._6_80,
        Bits.WEDGE
    ])
)

arc_wizard_single = Pack(
    name="arc_wizard_single",
    parts=Counter([
        LockChip.WIZARD,
        MainBlade.ARC,
        AssistBlade.ROUND,
        Ratchets._4_55,
        Bits.LOW_ORB
    ])
)

reaper_incendio_single = Pack(
    name="reaper_incendio_single",
    parts=Counter([
        LockChip.INCENDIO,
        MainBlade.REAPER,
        AssistBlade.TURN,
        Ratchets._4_70,
        Bits.KICK
    ])
)

courage_dran_single = Pack(
    name="courage_dran_single",
    parts=Counter([
        LockChip.DRAN,
        MainBlade.COURAGE,
        AssistBlade.SLASH,
        Ratchets._6_60,
        Bits.VORTEX
    ])
)

drop_attack_battle_set = Pack(
    name="drop_attack_battle_set",
    parts=Counter([
        Blades.IMPACT_DRAKE,
        Ratchets._9_60,
        Bits.LOW_RUSH,
        Blades.HOVER_WYVERN,
        Ratchets._3_85,
        Bits.NEEDLE
    ])
)

chain_incendio_circle_ghost_double = Pack(
    name="chain_incendio_circle_ghost_double",
    parts=Counter([
        Blades.CHAIN_INCENDIO,
        Ratchets._5_60,
        Bits.HIGH_TAPER,
        Blades.CIRCLE_GHOST,
        Ratchets._0_80,
        Bits.GEAR_BALL
    ])
)

sword_dran_tackle_goat_double = Pack(
    name="sword_dran_tackle_goat_double",
    parts=Counter([
        Blades.SWORD_DRAN,
        Ratchets._3_60,
        Bits.FLAT,
        Blades.TACKLE_GOAT,
        Ratchets._2_70,
        Bits.NEEDLE
    ])
)

fox_brush_single = Pack(
    name="fox_brush_single",
    parts=Counter([
        LockChip.FOX,
        MainBlade.BRUSH,
        AssistBlade.JAGGY,
        Ratchets._9_70,
        Bits.GEAR_RUSH
    ])
)

wriggle_kraken_single = Pack(
    name="wriggle_kraken_single",
    parts=Counter([
        LockChip.KRAKEN,
        MainBlade.WRIGGLE,
        AssistBlade.SLASH,
        Ratchets._3_85,
        Bits.ORB
    ])
)

fort_hornet_single = Pack(
    name="fort_hornet_single",
    parts=Counter([
        LockChip.HORNET,
        MainBlade.FORT,
        AssistBlade.ROUND,
        Ratchets._7_60,
        Bits.TAPER
    ])
)

antler_stag_single = Pack(
    name="antler_stag_single",
    parts=Counter([
        LockChip.STAG,
        MainBlade.ANTLER,
        AssistBlade.BUMPER,
        Ratchets._2_60,
        Bits.HIGH_NEEDLE
    ])
)

rock_golem_single = Pack(
    name="rock_golem_single",
    parts=Counter([
        Blades.ROCK_GOLEM,
        Ratchets._1_60,
        Bits.UNDER_NEEDLE
    ])
)

shelter_drake_single = Pack(
    name="shelter_drake_single",
    parts=Counter([
        Blades.SHELTER_DRAKE,
        Ratchets._7_80,
        Bits.GEAR_POINT
    ])
)

lance_knight_yellow_single = Pack(
    name="lance_knight_yellow_single",
    parts=Counter([
        Blades.LANCE_KNIGHT,
        Ratchets._3_60,
        Bits.LOW_FLAT
    ])
)

arrow_wizard_orange_single = Pack(
    name="arrow_wizard_orange_single",
    parts=Counter([
        Blades.ARROW_WIZARD,
        Ratchets._4_80,
        Bits.ORB
    ])
)

xtreme_expansion_pack = Pack(
    name="xtreme_expansion_pack",
    parts=Counter([
        Blades.MAIL_KNIGHT,
        Ratchets._3_85,
        Bits.BOUND_SPIKE,
        Blades.CIRCLE_GHOST,
        Ratchets._7_70,
        Ratchets._9_65,
        Bits.RUBBER_ACCEL,
        Bits.BALL,
        Blades.HAMMER_INCENDIO,
        Ratchets._4_55,
        Bits.POINT,
        Bits.METAL_NEEDLE
    ])
)

yggdrasil_team_pack = Pack(
    name="yggdrasil_team_pack",
    parts=Counter([
        Blades.COWL_SPHINX,
        Ratchets._9_80,
        Bits.GEAR_NEEDLE,
        Blades.RUDDER_PHOENIX,
        Ratchets._9_70,
        Bits.GLIDE,
        Blades.STING_UNICORN,
        Ratchets._5_60,
        Bits.GEAR_POINT
    ])
)

hack_viking_circle_ghost_double = Pack(
    name="hack_viking_circle_ghost_double",
    parts=Counter([
        Blades.HACK_VIKING,
        Ratchets._4_55,
        Bits.ORB,
        Blades.CIRCLE_GHOST,
        Ratchets._4_60,
        Bits.LOW_RUSH
    ])
)

calibur_samurai_obisidian_shell_double = Pack(
    name="calibur_samurai_obisidian_shell_double",
    parts=Counter([
        Blades.CALIBUR_SAMURAI,
        Ratchets._6_70,
        Bits.MERGE,
        Blades.OBSIDIAN_SHELL,
        Ratchets._3_85,
        Bits.SPIKE
    ])
)

ridge_triceratops_single = Pack(
    name="ridge_triceratops_single",
    parts=Counter([
        Blades.RIDGE_TRICERATOPS,
        Ratchets._9_80,
        Bits.GEAR_NEEDLE
    ])
)

shelter_drake_yellow_single = Pack(
    name="shelter_drake_yellow_single",
    parts=Counter([
        Blades.SHELTER_DRAKE,
        Ratchets._5_70,
        Bits.ORB
    ])
)

feather_phoenix_single = Pack(
    name="feather_phoenix_single",
    parts=Counter([
        Blades.FEATHER_PHOENIX,
        Ratchets._2_60,
        Bits.NEEDLE
    ])
)

rudder_phoenix_single = Pack(
    name="rudder_phoenix_single",
    parts=Counter([
        Blades.RUDDER_PHOENIX,
        Ratchets._4_70,
        Bits.LOW_FLAT
    ])
)

stun_medusa_single = Pack(
    name="stun_medusa_single",
    parts=Counter([
        Blades.STUN_MEDUSA,
        Ratchets._9_60,
        Bits.GEAR_BALL
    ])
)

scale_shark_single = Pack(
    name="scale_shark_single",
    parts=Counter([
        Blades.SCALE_SHARK,
        Ratchets._4_50,
        Bits.UNDER_FLAT
    ])
)

fang_leon_single = Pack(
    name="fang_leon_single",
    parts=Counter([
        LockChip.LEON,
        MainBlade.FANG,
        AssistBlade.TURN,
        Ratchets._4_60,
        Bits.UNITE
    ])
)

reaper_rhino_single = Pack(
    name="reaper_rhino_single",
    parts=Counter([
        LockChip.RHINO,
        MainBlade.REAPER,
        AssistBlade.CHARGE,
        Ratchets._4_55,
        Bits.DOT
    ])
)

flame_cerberus_single = Pack(
    name="flame_cerberus_single",
    parts=Counter([
        LockChip.CERBERUS,
        MainBlade.FLAME,
        AssistBlade.WHEEL,
        Ratchets._5_80,
        Bits.WALL_BALL
    ])
)

