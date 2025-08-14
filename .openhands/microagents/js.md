---
name: js
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers: ["js", "javascript", "JS", "JavaScript"]
---

# JavaScript Information Microagent

This microagent provides comprehensive information about JavaScript, including language features, best practices, frameworks, and development guidance.

## Capabilities

- Explain JavaScript language fundamentals
- Provide information about ES6+ features
- Discuss JavaScript frameworks and libraries
- Share best practices and coding patterns
- Explain asynchronous programming concepts
- Provide debugging and performance tips

## Core JavaScript Topics

### Language Fundamentals
- **Variables and Data Types**: var, let, const, primitives, objects
- **Functions**: Function declarations, expressions, arrow functions, closures
- **Objects and Arrays**: Object manipulation, array methods, destructuring
- **Control Flow**: Conditionals, loops, error handling
- **Scope and Hoisting**: Function scope, block scope, variable hoisting

### Modern JavaScript (ES6+)
- **Arrow Functions**: Concise syntax and lexical this binding
- **Template Literals**: String interpolation and multi-line strings
- **Destructuring**: Object and array destructuring patterns
- **Modules**: Import/export statements, module systems
- **Classes**: Class syntax, inheritance, static methods
- **Promises and Async/Await**: Asynchronous programming patterns
- **Spread and Rest Operators**: Object/array spreading and parameter handling

### Advanced Concepts
- **Closures**: Function scope and data privacy
- **Prototypes**: Prototype chain and inheritance
- **Event Loop**: Asynchronous execution model
- **Hoisting**: Variable and function hoisting behavior
- **This Binding**: Context binding in different scenarios

## Popular JavaScript Frameworks and Libraries

### Frontend Frameworks
- **React**: Component-based UI library
- **Vue.js**: Progressive framework for building UIs
- **Angular**: Full-featured application framework
- **Svelte**: Compile-time optimized framework

### Backend Runtime
- **Node.js**: Server-side JavaScript runtime
- **Express.js**: Web application framework for Node.js
- **Nest.js**: Progressive Node.js framework

### Utility Libraries
- **Lodash**: Utility library for common programming tasks
- **Moment.js/Day.js**: Date manipulation libraries
- **Axios**: HTTP client library

## Best Practices

### Code Quality
- Use strict mode (`'use strict'`)
- Prefer `const` and `let` over `var`
- Use meaningful variable and function names
- Follow consistent code formatting
- Implement proper error handling

### Performance
- Minimize DOM manipulation
- Use event delegation
- Implement lazy loading
- Optimize loops and iterations
- Use appropriate data structures

### Security
- Validate and sanitize user input
- Avoid `eval()` and similar functions
- Use HTTPS for data transmission
- Implement proper authentication
- Prevent XSS and CSRF attacks

## Common Patterns and Examples

### Async/Await Pattern
```javascript
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
```

### Module Pattern
```javascript
// ES6 Modules
export const myFunction = () => {
  // function implementation
};

export default class MyClass {
  // class implementation
}
```

### Event Handling
```javascript
// Modern event handling
document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#myButton');
  button.addEventListener('click', handleClick);
});
```

## Development Tools

### Package Managers
- **npm**: Node Package Manager
- **Yarn**: Alternative package manager
- **pnpm**: Fast, disk space efficient package manager

### Build Tools
- **Webpack**: Module bundler
- **Vite**: Fast build tool
- **Parcel**: Zero-configuration build tool
- **Rollup**: Module bundler for libraries

### Testing Frameworks
- **Jest**: JavaScript testing framework
- **Mocha**: Feature-rich test framework
- **Cypress**: End-to-end testing
- **Playwright**: Cross-browser testing

## Debugging and Development

### Browser DevTools
- Console for logging and debugging
- Network tab for monitoring requests
- Performance profiling
- Memory usage analysis

### Common Debugging Techniques
- Use `console.log()` for basic debugging
- Set breakpoints in browser DevTools
- Use `debugger` statement
- Implement proper error boundaries
- Use linting tools (ESLint)

## Resources and Learning

### Official Documentation
- MDN Web Docs: Comprehensive JavaScript reference
- ECMAScript specifications
- Node.js documentation

### Learning Platforms
- FreeCodeCamp
- JavaScript.info
- Eloquent JavaScript (book)
- You Don't Know JS (book series)

## Guidelines

- Always provide accurate, up-to-date information
- Include practical examples when explaining concepts
- Mention browser compatibility when relevant
- Suggest best practices and modern approaches
- Explain both the "how" and "why" of JavaScript concepts

## Limitations

- Focus on standard JavaScript (ECMAScript)
- Avoid deprecated or obsolete features unless specifically asked
- Provide context for browser-specific features
- Mention when features require polyfills or transpilation