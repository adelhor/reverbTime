# Reverberation Time Calculation Toolkit

This Python project contains several utilities for acoustic engineering applications, including database management, main processing, and reverberation time calculation.

## Project Structure

- `main.py`: The entry point of the application. It integrates various modules and executes the program.
- `DB.py`: Manages interactions with a MySQL database, handles database operations, ensuring that data is correctly managed and queried.
- `reverbTime.py`: Implements algorithms to calculate the reverberation time based on input data and acoustic parameters.

## Installation

You need Python and some external libraries to run these scripts. Follow the steps below to set up your environment:

1. Clone the repository:

```bash
git clone https://github.com/adelhor/reverberation_time_calculation.git
cd reverberation_time_calculation
```
2. Install the necessary Python packages:

```bash
pip install -r requirements.txt
```
Included libraries in requirements.txt are:/
numpy/
matplotlib/
mysql-connector-python

## Usage
Once you've installed the dependencies, execute main.py to start the application:
```bash
python main.py
```
Ensure your database configurations and other necessary parameters are correctly set within each script.

