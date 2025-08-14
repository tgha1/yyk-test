---
name: File Modifier
type: knowledge
version: 1.0.0
agent: CodeActAgent
triggers:
  - beta
---

# File Modifier Microagent

This microagent is designed to help modify files in the repository when triggered by the "beta" keyword.

## Capabilities

- Modify existing files in the repository
- Create new files when needed
- Handle various file types (text, code, configuration files, etc.)
- Perform search and replace operations
- Add, remove, or update content in files

## Usage

When the trigger word "beta" is mentioned in the conversation, this microagent becomes active and provides enhanced file modification capabilities.

## Common File Modification Tasks

1. **Text Replacement**: Replace specific text patterns in files
2. **Content Addition**: Add new content to existing files
3. **Content Removal**: Remove specific sections or lines from files
4. **File Creation**: Create new files with specified content
5. **Bulk Operations**: Perform modifications across multiple files

## Best Practices

- Always backup important files before making significant changes
- Use precise search patterns to avoid unintended modifications
- Verify changes after modification
- Consider the file encoding and format when making changes
- Test modifications in a safe environment first

## Limitations

- Cannot modify binary files directly
- Large file operations may take time
- Some file types may require special handling
- Always respect file permissions and access controls

## Error Handling

If file modification fails:
- Check file permissions
- Verify file exists and is accessible
- Ensure the target directory exists
- Validate the modification syntax