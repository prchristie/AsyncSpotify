# Tests

## Install dependencies

```bash
pip install -r requirements.dev.txt
pip install -r requirements.txt
```

## Run the tests in IntelliJ

![Test in intellij](https://i.imgur.com/4BNRlRz.png)

## Run the tests in the console

Go into the root directory of this project and run the following command

```bash
pytest -s --cov=async_spotify src/test --cov-report=xml
```