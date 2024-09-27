# Installation Guide for forgekit

## Quick Installation

You can install **forgekit** via `pip`:

```bash
pip install forgekit
```

This is the fastest way to get started.

## Manual Installation

If you prefer to install the package manually, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/0xMarcio/forgekit
   ```

2. Navigate to the project directory:

   ```bash
   cd forgekit
   ```

3. Install the package using `pip`:

   ```bash
   pip install .
   ```

## Installing Dependencies

All necessary dependencies are listed in the [requirements.txt](https://github.com/0xMarcio/forgekit/blob/main/requirements.txt) file. If you're installing manually, run:

```bash
pip install -r requirements.txt
```

This ensures that all the required libraries are installed for **forgekit** to function properly.

## Example Usage

The repository includes a detailed example file, [examples.py](https://github.com/0xMarcio/forgekit/blob/main/examples.py), showcasing a typical workflow using **forgekit**. This file covers:

- Data display and summary
- Missing data handling
- Outlier removal
- Data normalization
- K-Means clustering
- Plotting (both static and interactive)
- Rolling averages
- Report generation

### Running [examples.py](https://github.com/0xMarcio/forgekit/blob/main/examples.py)

To run the example script:

1. Make sure you've installed **forgekit** and its dependencies.
2. Execute the script:

```bash
python3 examples.py
```

This will guide you through an interactive process, displaying results step-by-step.

## Further Help

If you encounter issues or want to contribute, feel free to open issues or pull requests in the repository.
