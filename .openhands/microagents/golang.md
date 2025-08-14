---
name: golang
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers: ["golang", "go", "go language", "go programming"]
---

# Golang Microagent

This microagent provides comprehensive information about the Go programming language (Golang). It covers language features, best practices, common patterns, and development guidance for Go developers.

## Capabilities

- Explain Go language fundamentals and syntax
- Provide information about Go's unique features (goroutines, channels, interfaces)
- Share best practices and idiomatic Go code patterns
- Explain Go's standard library and ecosystem
- Discuss Go's concurrency model and memory management
- Provide guidance on Go project structure and tooling

## Language Overview

**Go (Golang)** is an open-source programming language developed by Google in 2007 and released in 2009. It was created by Robert Griesemer, Rob Pike, and Ken Thompson.

### Key Features

1. **Simplicity**: Clean, readable syntax with minimal keywords
2. **Fast Compilation**: Extremely fast build times
3. **Static Typing**: Strong type system with type inference
4. **Garbage Collection**: Automatic memory management
5. **Concurrency**: Built-in support for concurrent programming
6. **Cross-Platform**: Compiles to native binaries for multiple platforms

## Core Concepts

### Goroutines and Concurrency
- **Goroutines**: Lightweight threads managed by Go runtime
- **Channels**: Communication mechanism between goroutines
- **Select Statement**: Multiplexing for channel operations
- **Sync Package**: Mutexes, WaitGroups, and other synchronization primitives

### Interfaces
- **Implicit Implementation**: Types satisfy interfaces automatically
- **Empty Interface**: `interface{}` can hold any type
- **Type Assertions**: Runtime type checking and conversion

### Error Handling
- **Explicit Error Returns**: Functions return error as last value
- **Error Interface**: Simple `Error() string` method
- **Panic/Recover**: Exception-like mechanism for unrecoverable errors

## Standard Library Highlights

- **net/http**: HTTP client and server
- **encoding/json**: JSON marshaling/unmarshaling
- **fmt**: Formatted I/O operations
- **os**: Operating system interface
- **io**: I/O primitives
- **context**: Request-scoped values and cancellation
- **testing**: Built-in testing framework

## Development Tools

- **go build**: Compile packages and dependencies
- **go run**: Compile and run Go programs
- **go test**: Run tests and benchmarks
- **go mod**: Module dependency management
- **go fmt**: Format Go source code
- **go vet**: Static analysis tool
- **gofmt**: Code formatter

## Best Practices

1. **Code Organization**
   - Use meaningful package names
   - Keep packages focused and cohesive
   - Follow standard project layout

2. **Error Handling**
   - Always check errors explicitly
   - Wrap errors with context when appropriate
   - Use sentinel errors for expected conditions

3. **Concurrency**
   - Don't communicate by sharing memory; share memory by communicating
   - Use channels for communication between goroutines
   - Avoid goroutine leaks with proper cleanup

4. **Performance**
   - Profile before optimizing
   - Use sync.Pool for object reuse
   - Minimize allocations in hot paths

## Common Patterns

### Worker Pool
```go
func workerPool(jobs <-chan Job, results chan<- Result) {
    for job := range jobs {
        results <- process(job)
    }
}
```

### Context Usage
```go
func doWork(ctx context.Context) error {
    select {
    case <-ctx.Done():
        return ctx.Err()
    case <-time.After(time.Second):
        // do work
        return nil
    }
}
```

### Interface Design
```go
type Reader interface {
    Read([]byte) (int, error)
}
```

## Use Cases

Go is particularly well-suited for:

- **Web Services**: REST APIs, microservices
- **System Programming**: CLI tools, system utilities
- **Network Programming**: Servers, proxies, load balancers
- **Cloud Infrastructure**: Docker, Kubernetes, Terraform
- **DevOps Tools**: Monitoring, deployment, automation
- **Distributed Systems**: High-performance concurrent applications

## Popular Go Projects

- **Docker**: Containerization platform
- **Kubernetes**: Container orchestration
- **Prometheus**: Monitoring and alerting
- **Terraform**: Infrastructure as code
- **Hugo**: Static site generator
- **CockroachDB**: Distributed SQL database

## Learning Resources

- **Official Documentation**: https://golang.org/doc/
- **Go Tour**: Interactive introduction to Go
- **Effective Go**: Official style guide
- **Go Blog**: Regular updates and deep dives
- **Go Playground**: Online Go compiler and sharing tool

## Limitations and Considerations

- **Generics**: Added in Go 1.18, still evolving
- **Dependency Management**: Module system is relatively new
- **Learning Curve**: Different approach to OOP and error handling
- **Verbosity**: Explicit error handling can be verbose
- **Package Management**: Less mature ecosystem compared to some languages

## Getting Started

1. **Installation**: Download from https://golang.org/dl/
2. **Setup**: Configure GOPATH and GOROOT (or use modules)
3. **First Program**: Create a simple "Hello, World!" application
4. **Learn Basics**: Variables, functions, structs, interfaces
5. **Practice Concurrency**: Experiment with goroutines and channels
6. **Build Projects**: Start with small CLI tools or web services

Go's philosophy emphasizes simplicity, readability, and efficiency, making it an excellent choice for modern software development, especially in cloud-native and distributed systems contexts.