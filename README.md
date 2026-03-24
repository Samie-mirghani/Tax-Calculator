# Tax Calculator

A lightweight, interactive Python utility that computes itemized state tax, local tax, and total purchase price for any number of consumer transactions — presented in a clean, tabular format.

## Overview

Managing sales tax calculations across multiple purchases can be tedious and error-prone when done manually. **Tax Calculator** automates this process by accepting an arbitrary number of item prices, applying configurable state and local tax rates, and producing a formatted summary table. Built as a modular, single-script solution, it is easy to run, extend, and integrate into larger workflows.

## Key Features

- **Multi-Item Support** — Process any number of purchases in a single session.
- **Dual Tax Computation** — Independently calculates state tax (4.5%) and local tax (2.5%) for each item.
- **Total Tax & Purchase Price** — Derives combined tax and final purchase price per item automatically.
- **Tabular Output** — Displays results in an aligned, currency-formatted table for quick readability.
- **Zero Dependencies** — Runs on any standard Python installation with no external packages required.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language  | Python 3   |
| Interface | CLI (stdin / stdout) |
| Dependencies | None (standard library only) |

## System Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  User Input  │────▶│  Tax Computation │────▶│  Table Display  │
│  (# items,   │     │  • State Tax     │     │  • State Tax    │
│   prices)    │     │  • Local Tax     │     │  • Local Tax    │
│              │     │  • Total Tax     │     │  • Total Tax    │
│              │     │  • Purchase Price│     │  • Purchase $   │
└──────────────┘     └──────────────────┘     └─────────────────┘
```

1. **Input Phase** — The user specifies the number of purchases and enters each item's price.
2. **Computation Phase** — State and local tax rates are applied to each item; totals are accumulated.
3. **Output Phase** — A formatted table is printed showing per-item tax breakdowns and final prices.

## Setup & Installation

### Prerequisites

- **Python 3.6+** installed on your system.

### Running the Calculator

```bash
# Clone the repository
git clone https://github.com/samie-mirghani/tax-calculator.git
cd tax-calculator

# Run the program
python "Project 1 Extra Credit.py"
```

### Example Session

```
This program will compute the taxes for a given amount of purchases and will display the total purchase price
Enter number of purchases: 3
Please enter price of item 1: 25.00
Please enter price of item 2: 49.99
Please enter price of item 3: 12.50

State Tax    Local Tax     Total Tax   Purchase Price
$ 1.13       $0.63          $1.75         $26.75
$ 2.25       $1.25          $3.50         $53.49
$ 0.56       $0.31          $0.88         $13.38
```

## Suggested Topics / Tags

`python` · `tax-calculator` · `sales-tax` · `cli-tool` · `finance` · `automation` · `beginner-friendly`

## License

This project is provided as-is for educational and personal use.
