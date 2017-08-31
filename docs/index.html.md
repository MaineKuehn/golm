---
title: golm API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - python

toc_footers:
  - <a href='https://mainekuehn.github.io/workshop-collaborative_software'>Workshop Presentation</a>
  - <a href='https://github.com/MaineKuehn/golm'>Have a look at the source code</a>
  - <a href='https://github.com/MaineKuehn/rpconnect'>RPConnect project</a>

search: true
---

# Introduction

This is the API of the Game of Life Master, short **golm**, that is utilised in the course of the Workshop *Collaborative Software Development*. Golm is the central nameserver within the workshop.

You can use the NameServer API of golm to register new services and get a list of available services you can utilise for processing.

Golm offers language bindings in Python! You can view the required code examples in the dark area to the right.

# NameServer

## Registering a service

> To register a service, use this code:

```python
from golm.nameserver import NameServerAPI

api = NameServerAPI('host', port)
api.add('service', service_port)
```

> Make sure to replace `host` and `port` with the respective connection information.
> The parameters `service` and `service_port` provide the respective information about the service to register.

The NameServer API is instantiated by providing the hostname as well as port the golm service is running at. Internally a lightweight [RPConnect](https://github.com/MaineKuehn/rpconnect) framework is utilised. Please ensure to provide correct connection information. Valid connection information might look like this:

`host: coldev-s`

`port: 8080`

Required information to add your service look alike.

<aside class="notice">
You must replace <code>host</code>, <code>port</code>, <code>service</code> and <code>service_port</code> with the respective information of the given setup.
</aside>

## Get list of services

```python
from golm.nameserver import NameServerAPI

api = NameServerAPI('host', port)
services = api.get()
```

> Make sure to replace `host` and `port` with the repsective connection information.

> The above command returns JSON structured like this: 

```json
[
  {"service1": port},
  ...,
  {"servicen": port}
]
```

This endpoint retrieves a list of available services.

The NameServer API is instantiated by providing the hostname as well as port the golm service is running at. Internally a lightweight [RPConnect](https://github.com/MaineKuehn/rpconnect) framework is utilised. Please ensure to provide correct connection information. Valid connection information might look like this:

`host: coldev-s`

`port: 8080`

