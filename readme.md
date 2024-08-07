# ElectionEvaluator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/release/python-312/)

## Table of Contents

- [ElectionEvaluator](#electionevaluator)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Reference](#api-reference)
    - [`ElectionEvaluator`](#electionevaluator-1)
    - [`Candidate` (Pydantic Model)](#candidate-pydantic-model)
    - [`Election` (Pydantic Model)](#election-pydantic-model)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

**ElectionEvaluator** is a Python library designed to analyze election data from a CSV file. It calculates various statistics about candidates and elections, including age summation, candidate count, average age, and more. The library also provides functionality to convert data into structured Pydantic models for further processing and analysis.

## Features

- Load and process election data from a CSV file.
- Calculate age summation, candidate count, and average age.
- Identify indexes of youngest/oldest presidents and competitors.
- Generate structured election and candidate data using Pydantic models.
- Print detailed election information.

## Installation

To install **ElectionEvaluator**, clone the repository and install the required dependencies:

1. Clone the repository: `git clone https://github.com/yourusername/ElectionEvaluator.git`
2. Navigate to the project directory: `cd ElectionEvaluator`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage

Here's an example of how to use the ElectionEvaluator:

```python

from election_evaluator import ElectionEvaluator

file_path = '../presidents_election_full.csv'
evaluator = ElectionEvaluator(file_path=file_path)
summary = evaluator.get_summary()
elections = evaluator.get_elections()

print(summary)
for election in elections:
print(election)

evaluator.print_election_details()

``` 

## API Reference

### `ElectionEvaluator`

- **`__init__(self, file_path: str)`**
  - Initialize the ElectionEvaluator with the path to the CSV file.

- **`get_summary(self) -> dict`**
  - Returns a summary dictionary of the computed attributes.

- **`get_elections(self) -> List[Election]`**
  - Returns the list of Election instances.

- **`print_election_details(self)`**
  - Prints detailed information about the election.

### `Candidate` (Pydantic Model)

- **Attributes**
  - `age: int` - Age of the candidate.
  - `name: str` - Name of the candidate.
  - `electee: bool` - Whether the candidate is elected.

### `Election` (Pydantic Model)

- **Attributes**
  - `year: int` - Year of the election.
  - `candidates: List[Candidate]` - List of candidates in the election.

- **Methods**
  - `from_loc(cls, loc: pd.Series) -> Election` - Creates an Election instance from a pandas Series.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
