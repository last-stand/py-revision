# Python Revision Through Unit Testing
This project is helpful in learning about unit tests. It uses `unittest` libraray from python to assert and run tests.


## Installation

Go inside the root folder of the project and run,

```
pip install -r requirements.txt
```

## Running tests
Run single test file,
```
python -m unittest tests/unit/<filename.py>
```
Run all tests blindly with verbose info,
```
python3 -m unittest -v
```

Run all tests in the folder,
```
python -m unittest discover <test_directory>
# or
python -m unittest discover -s <directory> -p '*_test.py'
```