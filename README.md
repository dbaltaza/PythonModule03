# Python Module 03

Small collection of Python exercises focused on core data handling patterns:
arguments parsing, tuples, sets, dictionaries, generators, and comprehensions.

## Requirements

- Python `3.10+`
- No external dependencies

## Project Structure

- `ex0/ft_command_quest.py`: reads CLI arguments and prints argument stats.
- `ex1/ft_score_analytics.py`: parses numeric scores and computes analytics.
- `ex2/ft_coordinate_system.py`: tuple-based coordinates, parsing, and distance.
- `ex3/ft_achievement_tracker.py`: set operations for achievement analysis.
- `ex4/ft_inventory_system.py`: dictionary-based inventory parsing and reporting.
- `ex5/ft_data_stream.py`: generator streams and event processing.
- `ex6/ft_analytics_dashboard.py`: list/dict/set comprehensions in a dashboard.

## How To Run

From the repository root:

```bash
python3 ex0/ft_command_quest.py hello world
python3 ex1/ft_score_analytics.py 10 20 35
python3 ex2/ft_coordinate_system.py
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:12 potion:4 shield:1 potion:3
python3 ex5/ft_data_stream.py
python3 ex6/ft_analytics_dashboard.py
```

## Exercise Notes

### ex0 - Command Quest

- Uses `sys.argv` to inspect command-line input.
- Handles missing arguments cleanly.

### ex1 - Score Analytics

- Validates score inputs and rejects invalid values.
- Reports total, average, min/max, and range.

### ex2 - Coordinate System

- Represents positions as 3D tuples.
- Parses coordinates from string input and computes Euclidean distance.

### ex3 - Achievement Tracker

- Demonstrates set union, intersection, and difference.
- Finds rare achievements owned by only one player.

### ex4 - Inventory System

- Parses `name:quantity` pairs from CLI.
- Aggregates quantities, sorts items, and provides category/restock insights.

### ex5 - Data Stream

- Simulates events via generators for constant-memory processing.
- Includes extra generator demos for Fibonacci and prime numbers.

### ex6 - Analytics Dashboard

- Uses comprehensions for player/score/achievement summaries.
- Combines list, dict, and set transformations in one report.
