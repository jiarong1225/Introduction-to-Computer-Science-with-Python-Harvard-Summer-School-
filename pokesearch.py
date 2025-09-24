# Valid traits for Pokemon
TRAITS = ["HP", "Attack", "Sp. Attack", "Sp. Defense", "Speed"]


def english_name(pokemon):
    """OPTIONAL:
    You can use this as a sorting key function for Pokemon"""
    return pokemon["name"]["english"]


def pokesearch(trait, minimum, maximum):
    import pokedex
    list_of_pokemon = []
    for pokemon in pokedex.data:
        if pokemon["base"][trait] >= minimum and pokemon["base"][trait] <= maximum:
            result_pokemon={pokemon["name"]["english"]:pokemon["base"][trait]}
            list_of_pokemon.append(result_pokemon)
    return list_of_pokemon

    """
    Returns a list of Pokemon data structures (dictionaries,
    as shown in the pset problem description) that
    have a value of trait between minimum and maximum
    """
    # Add your code here


def main():
    trait = "HP"
    minimum = 50
    maximum = 100
    list_of_pokemon = pokesearch(trait, minimum, maximum)
    for x in list_of_pokemon:
        for a,b in x.items():
            print(f"{a:<20} {b:>5}")
    # Add your solution to the problem that makes use of the above to
    # print out the results of your pokemon search.



if __name__ == "__main__":
    main()
