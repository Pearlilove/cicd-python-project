# Python CI/CD Pipeline with GitHub Actions

## Project Overview

This project demonstrates a simple Continuous Integration (CI) pipeline using Python, Git, GitHub, and GitHub Actions.

The application contains a function that adds two numbers. Automated unit tests verify that the function works correctly for positive numbers, negative numbers, and zero.

GitHub Actions automatically runs the tests whenever code is pushed to the repository or a pull request is opened.

## Objectives

- Build a simple Python application.
- Write automated unit tests using Python's `unittest` framework.
- Configure GitHub Actions to run tests automatically.
- Practise version control and collaboration workflows using Git and GitHub.

## Technologies Used

- **Python:** Application development and automated testing.
- **unittest:** Testing the application's functionality.
- **Git:** Version control.
- **GitHub:** Hosting the source code.
- **GitHub Actions:** Automating the testing process.
- **Ubuntu:** Development environment.

## Project Structure

```text
cicd-python-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── test_app.py
├── .gitignore
└── README.md
```

### File Descriptions

- `app.py`: Contains the `add_numbers()` function and a simple example of how to run the application.
- `test_app.py`: Contains automated unit tests for the addition function.
- `.github/workflows/ci.yml`: Defines the GitHub Actions workflow that runs the tests.
- `.gitignore`: Prevents Python cache files from being tracked by Git.
- `README.md`: Documents the project and explains how to use it.

## How the Application Works

The application defines a function called `add_numbers(a, b)`, which accepts two numbers and returns their sum.

When `app.py` is executed directly, it adds 5 and 3 and prints the result.

Example output:

```text
The result is: 8
```

## Running the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/Pearlilove/cicd-python-project.git
cd cicd-python-project
```

### 2. Run the application

```bash
python3 app.py
```

### 3. Run the automated tests

```bash
python3 -m unittest -v
```

The tests check the function's behaviour with positive numbers, negative numbers, and zero.

## Continuous Integration Workflow

The GitHub Actions workflow is defined in `.github/workflows/ci.yml`.

The workflow:

1. Triggers when code is pushed or a pull request is opened.
2. Runs on an Ubuntu virtual machine hosted by GitHub.
3. Checks out the repository's source code.
4. Sets up Python.
5. Runs the automated unit tests.

If the tests pass, the workflow completes successfully. If a test fails, GitHub Actions reports the failure so the problem can be investigated.

## What I Learned

Through this project, I practised:

- Writing a basic Python application.
- Creating and running automated unit tests.
- Using Git to track changes and GitHub to host a project.
- Configuring a CI workflow with GitHub Actions.
- Understanding how automated testing helps identify problems when code changes.

## Future Improvements

- Add more application functions and unit tests.
- Introduce code quality checks and linting.
- Extend the pipeline with additional validation steps.
- Explore automated deployment in a future project.

## Author

**Pearlilove**

GitHub: [@Pearlilove](https://github.com/Pearlilove)
