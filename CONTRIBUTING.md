# Contributing to Physities

Thank you for your interest in contributing to Physities! This document provides guidelines for contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment (see below)
4. Create a feature branch
5. Make your changes
6. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/physities.git
cd physities

# Install Rust (if not installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dev dependencies
pip install -e ".[dev]"

# Build Rust extension
maturin develop

# Verify setup
pytest tests/ -v
```

## Making Changes

### Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Run `ruff check .` before committing

**Rust:**
- Follow Rust API Guidelines
- Run `cargo clippy` before committing
- Run `cargo fmt` for formatting

### Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks
- `refactor:` - Code refactoring
- `test:` - Test additions/changes

Example:
```
feat: add support for temperature units

- Add Celsius and Fahrenheit units
- Add conversion between temperature scales
- Update documentation
```

### Testing

- Add tests for new features
- Ensure all tests pass: `pytest tests/ -v`
- Tests should be marked with `@pytest.mark.unit`

### Documentation

- Update README.md for user-facing changes
- Update docs/ for architectural changes
- Add docstrings for public APIs

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feat/your-feature
   ```

2. **Make your changes and commit:**
   ```bash
   git add -A
   git commit -m "feat: description of changes"
   ```

3. **Push to your fork:**
   ```bash
   git push origin feat/your-feature
   ```

4. **Open a Pull Request** on GitHub

5. **Address review feedback** if any

6. **Merge** once approved

## Types of Contributions

### Bug Reports

- Use the GitHub issue tracker
- Include Python/Rust versions
- Provide minimal reproduction steps
- Include error messages/tracebacks

### Feature Requests

- Open an issue to discuss first
- Describe the use case
- Explain expected behavior

### Code Contributions

- Bug fixes
- New units or dimensions
- Performance improvements
- Documentation improvements

### Documentation

- Fix typos or errors
- Improve examples
- Add tutorials

## Code Review

All submissions require review. We use GitHub pull requests for this purpose.

**What we look for:**
- Correctness
- Test coverage
- Code style
- Documentation
- Performance considerations

## Questions?

- Open an issue for questions
- Check existing issues first
- Be patient and respectful

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
