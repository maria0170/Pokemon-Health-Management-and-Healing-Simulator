

from typing import Any, Dict
import unittest
import checker_generic
import pokemon_center as pc

FILENAME = "pokemon_center.py"
PYTA_CONFIG = "a1_pyta.txt"
TARGET_LEN = 79
SEP = "="

CONSTANTS = {
    "POTION_HEAL": 20,
    "SUPER_POTION_HEAL": 50,
    "POTION_COST": 0.99,
    "SUPER_POTION_COST": 2.49,
    "ANTIDOTE_BASE_COST": 2.99,
    "REVIVE_COST_PER_HEALTH": 0.02,
    "REVIVE_COST_CAP": 9.99
}

pkmn = "Pikachu 50/75 (Poisoned)"


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_get_pokemon_name(self) -> None:
        self._check(pc.get_pokemon_name, [pkmn], str)

    def test_get_pokemon_health(self) -> None:
        self._check(pc.get_pokemon_health, [pkmn], int)

    def test_get_pokemon_max_health(self) -> None:
        self._check(pc.get_pokemon_max_health, [pkmn], int)

    def test_get_pokemon_poisoned(self) -> None:
        self._check(pc.get_pokemon_poisoned, [pkmn], bool)

    def test_num_super_potions(self) -> None:
        self._check(pc.num_super_potions, [pkmn], int)

    def test_num_potions(self) -> None:
        self._check(pc.num_potions, [pkmn], int)

    def test_use_antidote(self) -> None:
        self._check(pc.use_antidote, [pkmn], bool)

    def test_use_revive(self) -> None:
        self._check(pc.use_revive, [pkmn], bool)

    def test_heal_pokemon(self) -> None:
        self._check(pc.heal_pokemon, [pkmn, 0, 0, True, True], str)

    def test_is_pokemon_healthy(self) -> None:
        self._check(pc.is_pokemon_healthy, [pkmn], bool)

    def test_is_name_length_at_least(self) -> None:
        self._check(pc.is_name_length_at_least, [pkmn, 2], bool)

    def test_is_name_palindrome(self) -> None:
        self._check(pc.is_name_palindrome, [pkmn], bool)

    def test_is_name_repeats_first_two_char(self) -> None:
        self._check(pc.is_name_repeats_first_two_char, [pkmn], bool)

    def test_compute_potion_cost(self) -> None:
        self._check(pc.compute_potion_cost, [pkmn], float)

    def test_compute_antidote_cost(self) -> None:
        self._check(pc.compute_antidote_cost, [pkmn], float)

    def test_compute_revive_cost(self) -> None:
        self._check(pc.compute_revive_cost, [pkmn], float)

    def test_compute_healing_cost(self) -> None:
        self._check(pc.compute_healing_cost, [pkmn], float)
        


    def test_check_constants(self) -> None:
        """Values of constants."""

        print("\nChecking that constants refer to their original values")
        self._check_constants(CONSTANTS, pc)
        print("  check complete")

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print("\nChecking {}...".format(func.__name__))
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print("  check complete")

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = "The value of constant {} should be {} but is {}.".format(
                name, expected, actual
            )
            self.assertEqual(expected, actual, msg)


print("".center(TARGET_LEN, SEP))
print(" Start: checking coding style ".center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(" End checking coding style ".center(TARGET_LEN, SEP))

print(" Start: checking type contracts ".center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(" End checking type contracts ".center(TARGET_LEN, SEP))

print("\nScroll up to see ALL RESULTS:")
print("  - checking coding style")
print("  - checking type contract\n")


