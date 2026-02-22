from parts import Blades, Ratchets, Bits, LockChip, MainBlade, AssistBlade
import packs
import owned
from solver import optimal_pack_selection

all_parts = set().union(
    Blades,
    Ratchets,
    Bits,
    LockChip,
    MainBlade,
    AssistBlade
)

all_parts_names = set()
for part in all_parts:
    all_parts_names.add(part.name)

print(f'All parts are unique: {len(all_parts) == len(all_parts_names)}')

all_packs = [
    packs.xtreme_battle_set,
    packs.soar_phoenix_single,
    packs.tail_viper_sword_dran_double,
    packs.chain_incendio_arrow_wizard_double,
    packs.knife_shinobi_keel_shark_double,
    packs.sword_dran_single,
    packs.scythe_incendio_single,
    packs.arrow_wizard_single,
    packs.helm_knight_single,
    packs.talon_ptera_single,
    packs.horn_rhino_single,
    packs.steel_samurai_single,
    packs.keel_shark_single,
    packs.yell_kong_helm_knight_double,
    packs.gale_wyvern_tail_viper_double,
    packs.bite_croc_sting_unicorn_double,
    packs.lance_knight_single,
    packs.claw_leon_single,
    packs.roar_tyranno_single,
    packs.savage_bear_single,
    packs.scythe_incendio_yellow_single,
    packs.sting_unicorn_single,
    packs.beat_tyranno_knife_shinobi_double,
    packs.gale_wyvern_sword_dran_double,
    packs.cowl_sphinx_single,
    packs.arrow_wizard_purple_single,
    packs.buster_dran_single,
    packs.wand_wizard_single,
    packs.cobalt_dragoon_single,
    packs.shadow_shinobi_single,
    packs.wand_wizard_green_single,
    packs.hammer_incendio_single,
    packs.buster_dran_yellow_single,
    packs.keel_shark_black_single,
    packs.yell_kong_single,
    packs.obsidian_shell_single,
    packs.soar_phoenix_blue_single,
    packs.pearl_tiger_gill_shark_double,
    packs.cowl_sphinx_crest_leon_double,
    packs.scarlet_garuda_single,
    packs.sterling_wolf_single,
    packs.tide_whale_single,
    packs.dagger_dran_single,
    packs.dark_perseus_single,
    packs.arc_wizard_single,
    packs.reaper_incendio_single,
    packs.courage_dran_single,
    packs.drop_attack_battle_set,
    packs.chain_incendio_circle_ghost_double,
    packs.sword_dran_tackle_goat_double,
    packs.fox_brush_single,
    packs.wriggle_kraken_single,
    packs.fort_hornet_single,
    packs.antler_stag_single,
    packs.rock_golem_single,
    packs.shelter_drake_single,
    packs.lance_knight_yellow_single,
    packs.arrow_wizard_orange_single,
    packs.xtreme_expansion_pack,
    packs.yggdrasil_team_pack,
    packs.hack_viking_circle_ghost_double,
    packs.calibur_samurai_obisidian_shell_double,
    packs.ridge_triceratops_single,
    packs.shelter_drake_yellow_single,
    packs.feather_phoenix_single,
    packs.rudder_phoenix_single,
    packs.stun_medusa_single,
    packs.scale_shark_single,
    packs.fang_leon_single,
    packs.reaper_rhino_single,
    packs.flame_cerberus_single
]

all_packs_set = set()
for pack in all_packs:
    all_packs_set.add(pack.name)

print(f'All packs are unique: {len(all_packs) == len(all_packs_set)}')

my_parts = set().union(
    owned.my_blades,
    owned.my_ratchets,
    owned.my_bits,
    owned.my_lockchips,
    owned.my_mainblades,
    owned.my_assistblades
)

# --- Run optimized solver ---
print("\n=== Running optimized pack solver ===")
solution = optimal_pack_selection(
    all_parts=all_parts,
    owned_parts=my_parts,
    packs=all_packs,
)

# --- Output results ---
if not solution:
    print("\nNo solution found.")
else:
    print("\nOptimal packs:")
    for pack in solution:
        print("-", pack.name)

    # --- Duplicate calculation ---
    seen = set(my_parts)
    duplicates = 0

    for pack in solution:
        for part in pack.parts.elements():
            if part in seen:
                duplicates += 1
            else:
                seen.add(part)

    print("Minimum duplicates:", duplicates)

"""
Remaining missing parts after reduction: 36
Remaining packs to search: 46
"""