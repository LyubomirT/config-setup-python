# Configuration Creator for Python

A Python library for managing configurations. Supports saving and loading configurations in various formats, such as JSON, YAML, XML, INI, and CFG.

## Installation

To install the library, you can use pip:

```
pip install ConfigSetup
```

## Usage

To use the ConfigSetup library in your Python code, you can import it and create an instance of the `ConfigSetup` class:

```python
from config_setup import ConfigSetup

config = ConfigSetup()
```

### Setting and Getting Values

To set a value in the configuration, you can use the `set` method:

```python
config.set('name', 'John')
```

To get a value from the configuration, you can use the `get` method:

```python
name = config.get('name')
```

### Saving and Loading Configurations

To save the configuration to a file, you can use the `save` method and specify the file format:

```python
config.save('config', 'json')
```
To load a configuration from a file, you can use the `load` method and specify the file path:

```python
config.load('config.json')
```

### Validating Configurations

To validate a configuration data string against a specific format, you can use the `validate` method and specify the format:

```python
data = '{"name": "John", "age": 30}'
valid = config.validate(data, 'json')
```

### Clearing the Configuration

To clear the configuration, you can use the `clear` method:

```python
config.clear()
```

## License

This library is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions are always welcome! If you'd like to contribute to this library, please follow these steps:

1.  Fork the project on GitHub.
2.  Clone your forked repository to your local machine.
3.  Create a new branch for your changes.
4.  Make your changes and commit them, making sure to write clear commit messages.
5.  Push your branch to your forked repository.
6.  Submit a pull request to the main project repository, explaining your changes and why they should be merged.

Before submitting a pull request, please make sure to run the tests by executing the following command from the project's root directory:

```
python -m unittest discover
```

If any tests fail, please investigate and fix the issue before submitting your pull request.

Thank you for your interest in contributing to this project!