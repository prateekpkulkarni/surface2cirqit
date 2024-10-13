---

# Contributing to `surface2cirqit`

Thank you for your interest in contributing to `surface2cirqit`! Whether you’re reporting bugs, adding features, improving documentation, or helping others, your contribution is valuable to the community. Please follow these guidelines to ensure a smooth collaboration.

## Getting Started

### 1. Fork the Repository
To start contributing:
1. Fork the repository by clicking the "Fork" button at the top of this page.
2. Clone the forked repository to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/surface2cirqit.git
   ```
3. Navigate into the project directory:
   ```bash
   cd surface2cirqit
   ```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. To set up the development environment:
1. Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Running Tests
Before submitting any pull requests (PRs), make sure all tests pass:
```bash
pytest tests/
```
You can also run linters to ensure code quality:
```bash
flake8 surface2cirqit/
```

## Contributing Workflow

### 1. Open an Issue
If you want to report a bug or suggest an enhancement, please [open an issue](https://github.com/prateekpkulkarni/surface2cirqit/issues) first. Provide enough detail so others can understand the context and respond appropriately.

### 2. Branching Strategy
When you’re ready to work on your contribution, create a new branch:
```bash
git checkout -b feature/your-feature-name
```

### 3. Commit Messages
Write clear, concise commit messages that describe the change:
- Use the present tense ("Add feature" not "Added feature").
- Limit the subject line to 50 characters.
- Reference the issue number in the commit message, if applicable (e.g., `Fix #42`).

### 4. Submitting Pull Requests
Once your work is complete:
1. Push your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Create a pull request from your forked repository's branch to the `main` branch of `surface2cirqit`. Include a detailed description of your changes in the PR.

### 5. Review Process
- A project maintainer will review your PR.
- You may be asked to make revisions.
- Once approved, your PR will be merged into the main codebase.

## Code Style Guidelines

1. Follow [PEP 8](https://pep8.org/) for Python code.
2. Use type hints where appropriate.
3. Ensure that all public methods and functions have clear docstrings that explain their purpose and usage.

## Feature Suggestions

For new features:
- Discuss the feature in an issue before beginning work.
- Ensure that new features are consistent with the goals and scope of `surface2cirqit`.

## Reporting Bugs

If you find a bug:
1. Check if the bug has already been reported in the [issues](https://github.com/prateekpkulkarni/surface2cirqit/issues).
2. If not, open a new issue and describe the bug, including:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Any relevant error messages or screenshots

## Improving Documentation

We welcome improvements to the documentation:
1. Make sure to update relevant sections in the `README.md` if your changes affect functionality or usage.
2. If you're adding a new module or function, ensure it’s documented in the code and update the relevant markdown files.

---

Thank you again for contributing to `surface2cirqit`! Your effort and input help make this project better.

