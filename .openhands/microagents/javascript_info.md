---
name: javascript_info
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers: ["js", "javascript"]
---

# JavaScript Information Microagent

This microagent provides comprehensive information about JavaScript, including its features, syntax, best practices, and ecosystem. It's designed to help users understand JavaScript concepts, troubleshoot issues, and learn about modern JavaScript development.

## Capabilities

- Explain JavaScript fundamentals and advanced concepts
- Provide syntax examples and code snippets
- Discuss JavaScript frameworks and libraries
- Share best practices and coding standards
- Help with debugging and troubleshooting
- Explain ES6+ features and modern JavaScript
- Discuss Node.js and server-side JavaScript
- Cover JavaScript testing frameworks and tools

## Core JavaScript Topics

### 1. **Language Fundamentals**
- Variables (var, let, const)
- Data types (primitives and objects)
- Functions (regular, arrow, async)
- Scope and closures
- Hoisting and temporal dead zone
- Event loop and asynchronous programming

### 2. **Object-Oriented Programming**
- Objects and prototypes
- Classes and inheritance
- Constructor functions
- Method binding and `this` context
- Getters and setters

### 3. **Modern JavaScript (ES6+)**
- Template literals
- Destructuring assignment
- Spread and rest operators
- Modules (import/export)
- Promises and async/await
- Map, Set, and other new data structures

### 4. **DOM Manipulation**
- Selecting and modifying elements
- Event handling
- Creating and removing elements
- Working with forms and user input

### 5. **Asynchronous JavaScript**
- Callbacks and callback hell
- Promises and promise chaining
- Async/await syntax
- Fetch API for HTTP requests
- Error handling in async code

## Popular JavaScript Frameworks & Libraries

### Frontend Frameworks
- **React**: Component-based UI library
- **Vue.js**: Progressive framework for building UIs
- **Angular**: Full-featured framework for web applications
- **Svelte**: Compile-time framework with no virtual DOM

### Backend & Runtime
- **Node.js**: Server-side JavaScript runtime
- **Express.js**: Web application framework for Node.js
- **Deno**: Modern runtime for JavaScript and TypeScript

### Utility Libraries
- **Lodash**: Utility library for common programming tasks
- **Moment.js/Day.js**: Date manipulation libraries
- **Axios**: HTTP client library

## Best Practices

### Code Quality
- Use strict mode (`'use strict'`)
- Prefer `const` and `let` over `var`
- Use meaningful variable and function names
- Write pure functions when possible
- Handle errors appropriately

### Performance
- Minimize DOM manipulation
- Use event delegation for dynamic content
- Debounce/throttle expensive operations
- Lazy load resources when appropriate
- Use efficient algorithms and data structures

### Security
- Validate and sanitize user input
- Avoid `eval()` and similar dangerous functions
- Use HTTPS for sensitive data
- Implement proper authentication and authorization

## Common JavaScript Patterns

### Module Pattern
```javascript
const MyModule = (function() {
    let privateVariable = 0;
    
    return {
        publicMethod: function() {
            return privateVariable++;
        }
    };
})();
```

### Observer Pattern
```javascript
class EventEmitter {
    constructor() {
        this.events = {};
    }
    
    on(event, callback) {
        if (!this.events[event]) {
            this.events[event] = [];
        }
        this.events[event].push(callback);
    }
    
    emit(event, data) {
        if (this.events[event]) {
            this.events[event].forEach(callback => callback(data));
        }
    }
}
```

## Debugging Tips

- Use browser developer tools effectively
- Console methods: `log()`, `error()`, `warn()`, `table()`
- Set breakpoints and step through code
- Use `debugger` statement for programmatic breakpoints
- Understand stack traces and error messages

## Testing in JavaScript

### Testing Frameworks
- **Jest**: Popular testing framework with built-in mocking
- **Mocha**: Flexible testing framework
- **Jasmine**: Behavior-driven testing framework
- **Cypress**: End-to-end testing framework

### Testing Types
- Unit testing for individual functions
- Integration testing for component interactions
- End-to-end testing for complete user workflows

## Package Management

### npm (Node Package Manager)
- Installing packages: `npm install package-name`
- Managing dependencies in `package.json`
- Scripts and automation
- Semantic versioning

### Alternative Package Managers
- **Yarn**: Fast, reliable package manager
- **pnpm**: Efficient package manager with hard links

## Development Tools

### Build Tools
- **Webpack**: Module bundler
- **Vite**: Fast build tool
- **Parcel**: Zero-configuration build tool
- **Rollup**: Module bundler for libraries

### Code Quality Tools
- **ESLint**: JavaScript linter
- **Prettier**: Code formatter
- **TypeScript**: Typed superset of JavaScript

## Resources for Learning

- MDN Web Docs: Comprehensive JavaScript documentation
- JavaScript.info: Modern JavaScript tutorial
- You Don't Know JS: Book series on JavaScript
- FreeCodeCamp: Interactive coding lessons
- Eloquent JavaScript: Online book about JavaScript

## Common Gotchas

- `==` vs `===` (type coercion)
- `this` binding in different contexts
- Hoisting behavior with `var`
- Asynchronous code execution order
- Reference vs value assignment for objects/arrays

This microagent is designed to provide accurate, up-to-date information about JavaScript and help users at all skill levels improve their JavaScript knowledge and coding practices.