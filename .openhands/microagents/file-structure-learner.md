---
name: File Structure Learner
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers:
  - Alpha
---

# File Structure Learner Microagent

This microagent is designed to help learn and analyze file structures within repositories and projects.

## Purpose

When triggered by the keyword "Alpha", this microagent provides capabilities to:
- Analyze directory structures and file hierarchies
- Identify file types and their purposes
- Map out project organization patterns
- Understand codebase architecture through file structure analysis

## Capabilities

### File Structure Analysis
- Recursively explore directory trees
- Categorize files by type, extension, and purpose
- Identify common project patterns (src/, tests/, docs/, etc.)
- Generate visual representations of file hierarchies

### Pattern Recognition
- Detect common project structures (monorepo, microservices, etc.)
- Identify framework-specific patterns (React, Django, Spring, etc.)
- Recognize configuration files and their relationships
- Map dependencies between modules and components

### Documentation Generation
- Create file structure documentation
- Generate directory tree visualizations
- Document file purposes and relationships
- Provide insights on project organization

## Usage Examples

When "Alpha" is mentioned in the conversation, this microagent will:

1. **Basic Structure Learning**: Analyze the current directory structure and provide insights
2. **Deep Analysis**: Perform comprehensive file structure analysis including file relationships
3. **Pattern Detection**: Identify and explain architectural patterns found in the codebase
4. **Documentation**: Generate structured documentation of the file hierarchy

## Tools and Commands

The microagent can utilize various tools for file structure analysis:
- `find` command for file discovery
- `tree` command for visual hierarchy display
- `ls` with various flags for detailed file information
- File content analysis for understanding purposes
- Git commands to understand version control structure

## Limitations

- Analysis depth may be limited by very large repositories
- Binary files are identified but not analyzed for content
- Some file relationships may require domain-specific knowledge
- Performance may vary with repository size

## Error Handling

- Gracefully handle permission denied errors
- Skip binary files that cannot be analyzed
- Provide meaningful feedback when directories are inaccessible
- Continue analysis even if some files cannot be processed

This microagent enhances the AI assistant's ability to understand and work with project structures effectively.