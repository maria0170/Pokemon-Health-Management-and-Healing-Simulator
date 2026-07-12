import math  
import constants  
  
from constants import (  
    POTION_HEAL,  
    SUPER_POTION_HEAL,  
    POTION_COST,  
    SUPER_POTION_COST,  
    ANTIDOTE_BASE_COST,  
    REVIVE_COST_PER_HEALTH,  
    REVIVE_COST_CAP  
)  
  
  
# This function is already done for you. Use this as an example!  
def get_pokemon_name(pokemon: str) -> str:  
    """Return the name of the pokemon if the string is non-empty; 
    otherwise return the empty string. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> get_pokemon_name('Eevee 50/80 (No poison)') 
    'Eevee' 
    >>> get_pokemon_name('Pikachu 75/75 (Poisoned)') 
    'Pikachu' 
    >>> get_pokemon_name('') 
    '' 
 
    """  
  
    if pokemon == "":  
        return ""  
    index = pokemon.find(' ')  
    return pokemon[:index]  
  
  
# Implement all the remaining functions here below  
  
def get_pokemon_health(pokemon: str) -> int:  
    """ Return the health of the pokemon, if the input is a non-empty name 
    return the int corresponding to the pokemon name. If the input is empty 
    return -1. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> get_pokemon_health('Pikachu 75/75 (Poisoned)') 
    75 
    >>> get_pokemon_health('Eevee 50/80 (No poison)') 
    50 
    >>> get_pokemon_health('') 
    -1 
 
    """  
  
    if pokemon == '':  
        return -1  
  
    slash = pokemon.find('/')  
    before_slash = pokemon[:slash]  
    first_space = before_slash.find(' ')  
    health_num = before_slash[first_space:slash]  
  
    return int(health_num)  
  
  
def get_pokemon_max_health(pokemon: str) -> int:  
    """ Reutrn the maximun health of the pokemon in an int form 
    if the input is non-empty. If the input is empty return -1. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> get_pokemon_max_health('Snorlax 0/700 (Poisoned)') 
    700 
    >>> get_pokemon_max_health('') 
    -1 
    >>> get_pokemon_max_health('Pikachu 0/75 (Poisoned)') 
    75 
 
    """  
    if pokemon == '':  
        return -1  
  
    slash = pokemon.find('/')  
    after_slash = pokemon[slash + 1:]  
    second_space = after_slash.find(' ')  
    max_health = after_slash[:second_space]  
  
    return int(max_health)  
  
  
def get_pokemon_poisoned(pokemon: str) -> bool:  
    """ Return whether each pokemon is posioned (True) or not (False) if the 
    input is non-empty, Otherwise, return Flase. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> get_pokemon_poisoned('Pikachu 5/75 (No poison)') 
    False 
    >>> get_pokemon_poisoned('') 
    False 
    >>> get_pokemon_poisoned('Charizard 110/200 (Poisoned)') 
    True 
 
    """  
    if pokemon == '':  
        return False  
    return '(Poisoned)' in pokemon  
  
  
def num_super_potions(pokemon: str) -> int:  
    """Return the number of super potions needed to heal the pokemon, if the 
    input is empty return 0. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> num_super_potions('Snorlax 0/700 (Poisoned)') 
    14 
    >>> num_super_potions('') 
    0 
    >>> num_super_potions('Pikachu 75/75 (No poison)') 
    0 
    >>> num_super_potions('Charizard 110/200 (Poisoned)') 
    1 
 
    """  
    if pokemon == '':  
        return 0  
    if get_pokemon_max_health(pokemon) == get_pokemon_health(pokemon):  
        return 0  
    return int((get_pokemon_max_health(pokemon) - get_pokemon_health  
                (pokemon)) / SUPER_POTION_HEAL)  
  
  
def num_potions(pokemon: str) -> int:  
    """Return the number of potions needed to heal the pokemon, if the input 
    is empty return 0 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> num_potions('') 
    0 
    >>> num_potions('Charizard 110/200 (Poisoned)') 
    4 
    >>> num_potions('Eevee 80/80 (Poisoned)') 
    0 
 
    """  
    if pokemon == '':  
        return 0  
    if get_pokemon_max_health(pokemon) == get_pokemon_health(pokemon):  
        return 0  
    return int((get_pokemon_max_health(pokemon) - get_pokemon_health  
                (pokemon)) / POTION_HEAL)  
  
  
def use_antidote(pokemon: str) -> bool:  
    """Return True if and only if the pokemon is poisoned. If the input 
    is empty, return False. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> use_antidote('Pikachu 75/75 (No poison)') 
    False 
    >>> use_antidote('') 
    False 
    >>> use_antidote('Eevee 80/80 (Poisoned)') 
    True 
    """  
    if pokemon == '':  
        return False  
    return get_pokemon_poisoned(pokemon)  
  
  
def use_revive(pokemon: str) -> bool:  
    """Return True if and only if the pokemon is at 0 health. If the input is 
    empty, return False. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> use_revive('Pikachu 0/75 (Poisoned)') 
    True 
    >>> use_revive('') 
    False 
    >>> use_revive('Pikachu 5/75 (No poison)') 
    False 
 
    """  
    return get_pokemon_health(pokemon) == 0  
  
  
def heal_pokemon(pokemon: str, potion_num: int, super_potions_num: int,  
                 antidote: bool, revive: bool) -> str:  
    """Return an updated viersion of the pokemon string after healing with 
    potion_num, super_potions_num, antidote, and revive. If the pokemon has 0 
    health and revive is not used then the health remains at 0. If the pokemon 
    is healthy, return the same string. If the pokemon string is empty, 
    return an empty string. 
 
    Precondition: pokemon is the string of pokemon features as 
    seen in pokemon.txt or an empty string 
 
    >>> heal_pokemon('Pikachu 0/75 (Poisoned)', 0, 0, False, False) 
    'Pikachu 0/75 (Poisoned)' 
    >>> heal_pokemon('', 0, 0, False, False) 
    '' 
    >>> heal_pokemon('Pikachu 50/75 (Poisoned)', 1, 0, False, False) 
    'Pikachu 70/75 (Poisoned)' 
    >>> heal_pokemon('Pikachu 0/75 (Poisoned)', 1, 1, True, True) 
    'Pikachu 70/75 (No poison)' 
    """  
    if pokemon == '':  
        return ''  
  
    name = get_pokemon_name(pokemon)  
    health_current = get_pokemon_health(pokemon)  
    health_max = get_pokemon_max_health(pokemon)  
    poisoned_check = get_pokemon_poisoned(pokemon)  
  
    if health_current == health_max and not poisoned_check:  
        return pokemon  
  
    if health_current == 0 and not revive:  
        health_new_num = 0  
    else:  
        healing = (potion_num * POTION_HEAL) + (  
            super_potions_num * SUPER_POTION_HEAL)  
        health_new_num = health_current + healing  
  
        health_new_num = min(health_new_num, health_max)  
  
    if antidote:  
        poison_text = '(No poison)'  
    elif poisoned_check:  
        poison_text = '(Poisoned)'  
    else:  
        poison_text = '(No poison)'  
  
    health_new = str(health_new_num)  
    max_health = str(health_max)  
  
    return name + ' ' + health_new + "/" + max_health + ' ' + poison_text  
  
  
def is_pokemon_healthy(pokemon: str) -> bool:  
    """ Return True if and only if the pokemon is healthy. If the input is 
    empty, return False. 
 
    >>> is_pokemon_healthy('Snorlax 0/700 (Poisoned)') 
    False 
    >>> is_pokemon_healthy('Eevee 80/80 (Poisoned)') 
    False 
    >>> is_pokemon_healthy('') 
    False 
    >>> is_pokemon_healthy('Pikachu 75/75 (No poison)') 
    True 
 
    """  
    if pokemon == '':  
        return False  
    health = get_pokemon_health(pokemon) == get_pokemon_max_health(pokemon)  
  
    return health and not get_pokemon_poisoned(pokemon)  
  
  
def is_name_length_at_least(pokemon: str, threshold: int) -> bool:  
    """Return True if and only if the length of the name of the pokemon is 
    at least the threshold value. If the input pokemon string is empty, 
    return False. 
 
    >>> is_name_length_at_least('Eevee 80/80 (Poisoned)', 5) 
    True 
    >>> is_name_length_at_least('', 20) 
    False 
    >>> is_name_length_at_least('Pikachu 75/75 (No poison)', 17) 
    False 
    """  
    if pokemon == '':  
        return False  
    name_get = get_pokemon_name(pokemon)  
    return len(name_get) >= threshold  
  
  
def is_name_palindrome(pokemon: str) -> bool:  
    """Return True if and only if the name of the pokemon is a palindrome. If 
    the input is the empty string, return False. 
 
    >>> is_name_palindrome('') 
    False 
    >>> is_name_palindrome('Eevee 80/80 (Poisoned)') 
    True 
    >>> is_name_palindrome('Pikachu 5/75 (No poison)') 
    False 
 
    """  
    if pokemon == '':  
        return False  
  
    name = get_pokemon_name(pokemon)  
    name_lower = name.lower()  
  
    return name_lower == name_lower[::-1]  
  
  
def is_name_repeats_first_two_char(pokemon: str) -> bool:  
    """Return True if and only if the name of the pokemon has the first two 
    characters(in that sequence) somewhere else in its name. If the input is 
    empty. return False. 
 
    >>> is_name_repeats_first_two_char('') 
    False 
    >>> is_name_repeats_first_two_char('Eevee 80/80 (Poisoned)') 
    True 
    >>> is_name_repeats_first_two_char('Pikachu 5/75 (No poison)') 
    False 
 
    """  
  
    if pokemon == '':  
        return False  
    name = get_pokemon_name(pokemon)  
    name_lower = name.lower()  
    return name_lower[0:2] in name_lower[2:]  
  
  
def compute_potion_cost(pokemon: str) -> float:  
    """Return the cost of potions and super potions needed for healing the 
    pokemon. If the input is empty return 0.0. 
 
    >>> compute_potion_cost('Pikachu 5/75 (No poison)') 
    3.48 
    >>> compute_potion_cost('') 
    0.0 
    >>> compute_potion_cost('Snorlax 0/700 (Poisoned)') 
    34.86 
    """  
    if pokemon == '':  
        return 0.0  
  
    health_current = get_pokemon_health(pokemon)  
    health_max = get_pokemon_max_health(pokemon)  
    healing_left = health_max - health_current  
  
    if healing_left == 0:  
        return 0.0  
  
    need_super = healing_left // SUPER_POTION_HEAL  
    after_super_potion = health_current + (need_super * SUPER_POTION_HEAL)  
    left_to_heal = health_max - after_super_potion  
  
    if left_to_heal > 0:  
        need_potion = (left_to_heal + POTION_HEAL - 1) // POTION_HEAL  
    else:  
        need_potion = 0  
  
    total = (need_potion * POTION_COST) + (need_super * SUPER_POTION_COST)  
  
    return round(total, 2)  
  
  
def compute_antidote_cost(pokemon: str) -> float:  
    """Return the cost of antidote needed for healing the pokemon, if the input 
    is empty return 0.0 
 
    >>> compute_antidote_cost('') 
    0.0 
    >>> compute_antidote_cost('Eevee 80/80 (Poisoned)') 
    0.0 
    >>> compute_antidote_cost('Pikachu 5/75 (Poison)') 
    0.0 
    >>> compute_antidote_cost('Girafarig 110/110 (Poisoned)') 
    1.2 
    """  
    if pokemon == '':  
        return 0.0  
  
    cost = ANTIDOTE_BASE_COST  
    savings = 0.0  
  
    if use_antidote(pokemon) == is_name_length_at_least(pokemon, 5):  
        savings += 0.20  
  
    if use_antidote(pokemon) == is_name_palindrome(pokemon):  
        savings += 0.40  
  
    if use_antidote(pokemon) == is_name_repeats_first_two_char(pokemon):  
        savings += 0.60  
  
    savings_cost = cost * savings  
    savings_round = math.floor(savings_cost * 100) / 100  
    end_cost = max(0.0, cost - savings_round)  
  
    return round(end_cost, 2)  
  
  
def compute_revive_cost(pokemon: str) -> float:  
    """Return the cost of revive needed for healing a pokemon, if the input is 
    empty, return 0.0 
 
    >>> compute_revive_cost('') 
    0.0 
    >>> compute_revive_cost('Snorlax 0/700 (Poisoned)') 
    9.99 
    >>> compute_revive_cost('Charmander 0/200 (No poison)') 
    4.0 
    >>> compute_revive_cost('Eevee 80/80 (Poisoned)') 
    0.0 
    """  
  
    if pokemon == '':  
        return 0.0  
    if get_pokemon_health(pokemon) != 0:  
        return 0.0  
  
    cost = REVIVE_COST_PER_HEALTH * get_pokemon_max_health(pokemon)  
  
    return min(cost, 9.99)  
  
  
def compute_healing_cost(pokemon: str) -> float:  
    """Return the total cost of healing the pokemon, if the input is empty 
    return 0.0. 
 
    >>> compute_healing_cost('') 
    0.0 
    >>> compute_healing_cost('Pikachu 5/75 (No poison)') 
    3.48 
    >>> compute_healing_cost('Snorlax 0/700 (Poisoned)') 
    47.25 
    """  
    if pokemon == '':  
        return 0.0  
  
    potion = compute_potion_cost(pokemon)  
    antidote = compute_antidote_cost(pokemon)  
    revive = compute_revive_cost(pokemon)  
    return potion + antidote + revive  
  
  
# function main  
if __name__ == "__main__":  
    """ The code below reads your doctests, and checks if your code returns the 
    correct output. Do not change this code!! 
    For example, for get_pokemon_name, it will check if 
    get_pokemon_name('Eevee 50/80 (No poison)') returns 'Eevee', and 
    get_pokemon_name('Pikachu 75/75 (Poisoned)') returns 'Pikachu', and 
    get_pokemon_name('') returns '' 
    If any of them do not match the doctests output, it will throw an error. 
    """  
    import doctest  
    doctest.testmod()  
