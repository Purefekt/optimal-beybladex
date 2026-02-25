from itertools import combinations
from collections import defaultdict


# -----------------------------
# Stage 1: Forced packs
# -----------------------------
def reduce_forced_packs(missing_parts, packs):
    forced = []
    forced_by = defaultdict(set)  # pack -> {forcing parts}
    remaining_packs = list(packs)
    missing = set(missing_parts)

    while True:
        part_to_packs = defaultdict(list)

        # Build reverse index
        for pack in remaining_packs:
            pack_parts = set(pack.parts.elements())
            for part in pack_parts & missing:
                part_to_packs[part].append(pack)

        newly_forced = []

        # Find uniquely covered parts
        for part, pack_list in part_to_packs.items():
            if len(pack_list) == 1:
                pack = pack_list[0]
                newly_forced.append((pack, part))

        if not newly_forced:
            break

        for pack, part in newly_forced:
            forced_by[pack].add(part)

            if pack not in forced:
                forced.append(pack)
                pack_parts = set(pack.parts.elements())
                missing -= pack_parts

        # Remove forced packs
        remaining_packs = [p for p in remaining_packs if p not in forced]

    return forced, forced_by, remaining_packs, missing


# -----------------------------
# Main solver
# -----------------------------
def optimal_pack_selection(all_parts, owned_parts, packs):
    missing = set(all_parts) - set(owned_parts)

    # 🔹 Stage 0: Remove unbuyable parts
    available_parts = set()
    for pack in packs:
        available_parts |= set(pack.parts.elements())

    unbuyable = missing - available_parts

    if unbuyable:
        print("\nUnbuyable parts (not in any available pack):")
        for part in sorted(unbuyable, key=lambda p: p.name):
            print(f"- {part.name}")

        # Remove from search space
        missing -= unbuyable

    if not missing:
        print("\nNo purchasable missing parts remain.")
        return []

    # 🔹 Stage 1: Forced reduction
    forced_packs, forced_by, remaining_packs, missing = reduce_forced_packs(
        missing, packs
    )

    print("\nMandatory packs (forced by unique parts):")
    if forced_packs:
        for pack in forced_packs:
            parts = sorted(p.name for p in forced_by[pack])
            print(f"- {pack.name}")
            print(f"  forced by: {', '.join(parts)}")
    else:
        print("None")

    # 🔹 Stage 1b: Remove redundant packs
    covered_by_forced = set()
    for pack in forced_packs:
        covered_by_forced |= set(pack.parts.elements())

    remaining_packs = [
        p for p in remaining_packs
        if not set(p.parts.elements()).issubset(covered_by_forced)
    ]

    print(f"\nRemaining missing parts after reduction: {len(missing)}")
    print(f"Remaining packs to search: {len(remaining_packs)}")

    if not missing:
        return forced_packs

    best_combo = None
    best_duplicates = float("inf")

    # 🔹 Stage 2: Exponential search
    for r in range(1, len(remaining_packs) + 1):
        for combo in combinations(remaining_packs, r):
            covered = set(covered_by_forced)
            total_parts = sum(len(p.parts) for p in forced_packs)

            for pack in combo:
                pack_parts = set(pack.parts.elements())
                covered |= pack_parts
                total_parts += len(pack_parts)

            if missing <= covered:
                duplicates = total_parts - len(covered)

                if duplicates < best_duplicates:
                    best_duplicates = duplicates
                    best_combo = combo

    if best_combo is None:
        print("\n⚠️ Could not cover all remaining missing parts.")
        return forced_packs

    return forced_packs + list(best_combo)