# Turn-Based Game - Claude Code Guidelines

## Project Overview

This is a Python-based turn-based game project that demonstrates game development concepts including game logic, player management, turn-based mechanics, and testing frameworks. The project showcases object-oriented programming principles in Python and provides a foundation for understanding game development patterns and structures.

## Development Environment

**Operating System**: Windows 11
**Shell**: Git Bash / PowerShell / Command Prompt
**Important**: Always use Windows-compatible commands:
- Use `dir` instead of `ls` for Command Prompt
- Use PowerShell commands when appropriate
- File paths use backslashes (`\`) in Windows
- Use `python -m http.server` for local development server
- Git Bash provides Unix-like commands but context should be Windows-aware

## Development Guidelines

### Code Quality
- Follow Python PEP 8 style guidelines
- Use meaningful variable and function names
- Implement proper error handling and logging
- Add comprehensive docstrings for functions and classes
- Use type hints where appropriate
- Maintain clean, readable code
- Follow language-specific best practices

### Security
- No sensitive information in the codebase
- Use HTTPS for all external resources
- Regular dependency updates
- Follow security best practices for the specific technology stack

### Game Development Specific Guidelines
- Implement proper game state management and transitions
- Use appropriate data structures for game logic and player management
- Handle user input responsively and consistently
- Implement proper turn-based mechanics with clear state tracking
- Separate game logic from presentation layer
- Use efficient algorithms for game calculations and rule enforcement
- Implement proper save/load functionality where applicable
- Design modular and extensible game components

### Python-Specific Guidelines
- Use virtual environments for dependency management
- Organize code into logical modules and packages
- Implement proper unit testing with the testing framework
- Use Python's built-in data structures effectively
- Follow Python naming conventions and idioms
- Implement proper exception handling for game scenarios

## Learning and Communication
- Always explain coding actions and decisions to help the user learn
- Describe why specific approaches or technologies are chosen
- Explain the purpose and functionality of code changes
- Provide context about best practices and coding patterns used
- Provide detailed explanations in the console when performing tasks, as many concepts may be new to the user