---
name: Test Runner
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers: []
---

# Test Runner Microagent

This microagent provides capabilities for running test cases in various programming environments and frameworks.

## Purpose

The Test Runner microagent helps execute and manage test suites across different testing frameworks and programming languages. It can identify test files, run specific tests or entire test suites, and provide detailed feedback on test results.

## Capabilities

### Test Discovery
- Automatically detect test files based on common naming conventions (test_*.py, *_test.py, *.test.js, etc.)
- Identify testing frameworks in use (pytest, unittest, jest, mocha, etc.)
- Scan project structure for test directories and configurations

### Test Execution
- Run individual test files or entire test suites
- Execute tests with appropriate framework commands
- Support for various testing frameworks:
  - Python: pytest, unittest, nose2
  - JavaScript/Node.js: jest, mocha, jasmine
  - Java: JUnit, TestNG
  - Go: go test
  - Ruby: RSpec, minitest
  - And more

### Test Reporting
- Provide detailed test results including pass/fail status
- Show test coverage information when available
- Display error messages and stack traces for failing tests
- Generate summary reports of test execution

### Environment Management
- Install missing test dependencies when needed
- Set up virtual environments for isolated testing
- Configure test environment variables
- Handle test database setup and teardown

## Usage Examples

### Running Python Tests
```bash
# Run all tests with pytest
pytest

# Run specific test file
pytest tests/test_example.py

# Run tests with coverage
pytest --cov=src tests/
```

### Running JavaScript Tests
```bash
# Run all tests with jest
npm test

# Run specific test file
npm test -- test_example.test.js

# Run tests in watch mode
npm test -- --watch
```

### Running Tests with Custom Configuration
```bash
# Run tests with specific configuration file
pytest -c pytest.ini

# Run tests with verbose output
pytest -v

# Run tests and stop on first failure
pytest -x
```

## Best Practices

1. **Test Discovery**: Always scan the project structure to identify the testing framework and test files before execution
2. **Dependency Management**: Check for and install missing test dependencies before running tests
3. **Environment Setup**: Ensure proper test environment configuration including environment variables and test databases
4. **Error Handling**: Provide clear error messages and suggestions when tests fail or cannot be executed
5. **Performance**: Use parallel test execution when supported by the framework
6. **Reporting**: Always provide clear, actionable feedback on test results

## Common Test File Patterns

- Python: `test_*.py`, `*_test.py`, `tests/`
- JavaScript: `*.test.js`, `*.spec.js`, `__tests__/`
- Java: `*Test.java`, `*Tests.java`, `src/test/`
- Go: `*_test.go`
- Ruby: `*_spec.rb`, `spec/`

## Error Handling

When tests fail or cannot be executed:
1. Check for missing dependencies and install them
2. Verify test file paths and naming conventions
3. Ensure proper test framework configuration
4. Check for environment-specific issues
5. Provide clear error messages with suggested solutions

## Limitations

- Requires appropriate testing frameworks to be installed
- May need specific environment setup for certain test types
- Performance depends on test suite size and complexity
- Some advanced testing features may require manual configuration