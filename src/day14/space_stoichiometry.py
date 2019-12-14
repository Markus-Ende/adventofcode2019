import math


def produce_fuel(reactions, initial_material=None, amount_of_fuel=1):
    ore_consumed = 0

    def produce_material_recursive(material_tuple, material):
        nonlocal ore_consumed
        (name, amount) = material_tuple
        # exit condition: consume ORE
        if (name == "ORE"):
            # print("consumed", amount, name)
            ore_consumed += amount
            return material
        # exit condition: material already available
        if (material[name] >= amount):
            material[name] -= amount
            # print("consumed", amount, name, material)
            return material

        reaction_input = reactions[name]["input"]
        reaction_output_amount = reactions[name]["output_amount"]

        # else: missing material needs to be produced
        amount_missing = amount - material[name]
        amount_of_reactions_needed = int(
            math.ceil(amount_missing / reaction_output_amount))

        for _ in range(0, amount_of_reactions_needed):
            for input_tuple in reaction_input:
                # print("starting production for", input_tuple, material)
                material = produce_material_recursive(
                    input_tuple, material)

            material[name] += reaction_output_amount

        material[name] -= amount
        return material

    if (initial_material == None):
        initial_material = {target: 0 for target in reactions}
    final_materials = produce_material_recursive(
        ("FUEL", amount_of_fuel), initial_material)
    # print("created fuel", final_materials)
    return (ore_consumed, final_materials)


def parse_reactions(input):
    def parse_material_spec(s):
        (out_amount, out_material) = s.split(" ")
        return (out_material, int(out_amount))

    reactions = {}
    reaction_strings = [l.strip() for l in input.split("\n")]
    for r in reaction_strings:
        (r_in, r_out) = r.split(" => ")
        (out_material, out_amount) = parse_material_spec(r_out)
        reactions[out_material] = {
            "output_amount": out_amount,
            "input": [parse_material_spec(s) for s in r_in.split(", ")]
        }
    return reactions


# TODO: find an efficient way to calculate this
#       because this takes some hours to finish 😆️
def check_fuel_production_with_trillion_ore(reactions):
    fuel_produced = 0
    totalore_consumed = 0

    material = None
    while(True):
        (consumed_ore, material_rest) = produce_fuel(reactions, material)
        if (totalore_consumed + consumed_ore > 1000000000000):
            break
        material = material_rest
        totalore_consumed += consumed_ore
        fuel_produced += 1
        # print(fuel_produced)

    return fuel_produced
