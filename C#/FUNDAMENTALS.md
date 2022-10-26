# C# Fundamentals

## Overview

C# is part of .NET.

.NET Ecosystem - Developer Platform from Microsoft which allows us to build applications. It includes different languages, libraries and tools. .NET 6 is cross-platform.

C# is the main language for .NET. It is object-oriented and type-safe. Backwards compatible - C# 1.0 would still compile under C# 10 compiler.

Types of applications:

- Console apps
- Desktop apps
- Web apps
- Mobile apps on iOS or Android
- Services - Windows services, background processes

## Setting-Up the Work Environment

**Projects** are containers for code files. The project holds references to all the files that are part of the application. Once we are done with editing, projects are compiled by the compiler into executable files (assembly).

**Solution** is a grouping for projects. Its function is the organization of all projects.

### The CLI for .NET

Cross-platform

Example:

- Create a new project:

```cmd
dotnet new console -n "FirstProgram"
```

- Compile the application

```cmd
dotnet build
```

- Execute the application

```cmd
dotnet run
```






