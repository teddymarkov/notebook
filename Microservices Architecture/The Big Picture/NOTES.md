# Microservices: The Big Picture

*From the Pluralsight course: https://app.pluralsight.com/library/courses/microservices-big-picture/table-of-contents*

## Software Development Lifecycle

### Software Development Stages

1. Requirements gathering
2. Plan & Design
3. Development
4. Testing
5. Release
6. Monitoring
7. Maintenance

### Parties

- Users and business analysts - gather requirements, write down user stores and plan the execution
- Developers, web designers and architects design and develop the software
- Project managers coordinate the product and synchronize everyone
- The operational team is responsible for monitoring, dealing with security and making sure the software is up and running

## What are Microservices?

A set of practices aimed to increase the speed and efficiency of development ond management of software solutions that scale. It is technology-agnostic. It is the principles and architectural patterns that will create a microservice architecture.

A microservice is build around a business capability and can be independently deployed.

### Micro...

**Bounded context:** It must do one thing and do it well. So, Micro refers to the scope of functionality. In order to do this sub-domains have to be identified  and a microservice to be built for each.

### ...Service

A service is an independently deployable component that supports interoperability through message based communication.

With microservices, the Software Development Stages iterate on smaller periods and the parties (teams) are also smaller. Having many services means more teams, that must communicate with each other.

## Microservices Elements

### Monoliths

| Pros              | Cons                         |
|-------------------|------------------------------|
| Simple to develop | New team member productivity |
| Simple to build   | Growing teams                |
| Simple to test    | Code harder to understand    |
| Simple to deploy  | No emerging technologies     |
| Simple to scale   | Scale for bad reasons        |
|                   | Overloaded container         |
|                   | Huge database                |

### Building Microservices

A domain corresponds to multiple subdomains. Each subdomain corresponds to a different part of the business.

BUT there are relations between subdomains, e.g. Users, Products and Orders. One solution is to duplicate data.

Sharing databases is discouraged and is an antipattern in the microservices world.

### Organization

From One team per domain -> One team per sub-domain.

Right sized teams: teams size can vary.

Team independence.

Each team is solely responsible for the entire lifecycle of the product.

Inter-team communication requires management.

Each team being independent, they can have their own documentation, repositories and version. 

Each service needs independent data storage.

In the microservices world there is no distributed transaction. There is no immediate consistency of a data. This leads to eventual consistency data based on event sourcing.

### User Interface

Each team can have their own set of graphical components. Challenge is how to maintain a Single application in an environment of unique UIs.

####UI composition:
- Server side composition, developed by multiple microservices teams;
- Client side composition, the browser build a single UI interface;

### Services





