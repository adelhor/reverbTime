# Reverberation Time Calculation Tool

This Python project contains several utilities for acoustic engineering applications, including database management, main processing, and reverberation time calculation.

## Project Structure

- **Main Application Logic (`main.py`):** As the core component of the application, this script orchestrates various functionalities and provides the following outputs:
  - A high-level summary or report of the application's actions and outcomes.
  - Detailed logs that include the progress of each operation and any critical information or warnings.
- **Database Operations (`database.py`)** This module is responsible for handling all database interactions. When executed, users can expect the following outputs:
  - Connection status updates indicating successful or failed database connections.
  - Confirmation messages upon successful completion of database operations such as insertions, updates, and deletions.
  - Logs or error messages detailing any issues encountered during database operations.
- **Reverberation Time Analysis (`algorithm.py`):** Focused on acoustic analysis, this script outputs:
  - Numerical results or graphs related to reverberation time calculations or simulations.
  - Descriptive summaries or interpretations of the analysis results.
  - Optionally, exported data or figures for further review or sharing.

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
Included libraries in requirements.txt are:\
- numpy\
- matplotlib\
- mysql-connector-python\
- python-dotenv

## Usage
Once you've installed the dependencies, execute main.py to start the application:
```bash
python main.py
```
Ensure your database configurations and other necessary parameters are correctly set within each script.

## Output
After displaying the calculated values in the output console, the main program will restart once the chart is closed, allowing the user to choose option.
#### The example output
![image](https://github.com/adelhor/reverberation_time_calculation/assets/115109011/25a5e64a-d25a-49cd-8e81-eabe2f3b5d24)

