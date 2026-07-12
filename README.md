# Pokemon-Health-Management-and-Healing-Simulator
A Python project that simulates Pokémon health management by parsing game data, tracking health and status conditions, applying healing mechanics, and calculating recovery item costs using modular algorithms and string processing.

# ⚡ Pokémon Health & Healing System

A Python application that simulates Pokémon health management by parsing Pokémon status data, applying healing mechanics, calculating item costs, and determining recovery requirements. The project demonstrates string processing, algorithm design, and modular programming through a collection of reusable functions.

---

##  Overview

This project implements a simplified Pokémon healing system using Python. Each Pokémon is represented as a formatted string containing its name, current health, maximum health, and poison status. The program extracts Pokémon information, determines healing requirements, updates health conditions, and calculates the cost of items such as Potions, Super Potions, Antidotes, and Revives.

The project emphasizes clean function design, string manipulation, and logical decision-making while simulating mechanics inspired by the Pokémon games.

---

##  Features

-  Parse Pokémon names, health, and status from formatted strings
-  Calculate current and maximum HP
-  Detect poisoned Pokémon
-  Determine the number of Potions and Super Potions required
-  Apply healing, antidotes, and revives
-  Calculate the total cost of healing items
-  Analyze Pokémon names using string-based algorithms
-  Includes comprehensive doctests for validation

---

##  Technologies Used

- Python 3
- String Processing
- Mathematical Calculations
- Modular Programming
- Conditional Logic
- Doctest Testing

---

##  Project Structure

```
pokemon_healing.py    # Core healing and cost calculation functions
constants.py          # Item values and game constants
README.md             # Project documentation
```

---

##  Core Functions

| Function | Description |
|----------|-------------|
| `get_pokemon_name()` | Extracts the Pokémon's name. |
| `get_pokemon_health()` | Returns the current HP. |
| `get_pokemon_max_health()` | Returns the maximum HP. |
| `get_pokemon_poisoned()` | Determines whether the Pokémon is poisoned. |
| `heal_pokemon()` | Applies healing items and updates the Pokémon's status. |
| `compute_potion_cost()` | Calculates potion costs. |
| `compute_antidote_cost()` | Calculates antidote costs with discounts. |
| `compute_revive_cost()` | Calculates revive costs. |
| `compute_healing_cost()` | Computes the total healing cost. |

---

##  Example

Input:

```python
pokemon = "Pikachu 50/75 (Poisoned)"
```

After healing:

```python
heal_pokemon(pokemon, 1, 0, True, False)
```

Output:

```
Pikachu 70/75 (No poison)
```

---

##  Testing

This project uses Python's built-in **doctest** module.

Run all tests with:

```bash
python pokemon_healing.py
```

Each function contains doctests to verify expected behavior.

---

##  Learning Objectives

This project demonstrates:

- String parsing and manipulation
- Python function design
- Conditional programming
- Mathematical computations
- Data validation
- Algorithm development
- Software testing with doctests

---

##  Skills Demonstrated

- Python
- String Manipulation
- Algorithm Design
- Problem Solving
- Modular Programming
- Mathematical Programming
- Software Testing
- Computational Thinking

---
