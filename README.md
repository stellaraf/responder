# Responder

Responder is an extremely simple REST/HTTP API used for measuring reachability, performance, or latency statistics to a given [Orion](https://stellar.tech/orion) data center location.

## API Routes

| Route        | Function                                                      |
| :----------- | :------------------------------------------------------------ |
| `/test/http` | Responds with a simple JSON response of `{ "success": true }` |

## Running

### Direct

```bash
python3 -m responder.main
```

### Docker

#### Individual Containers

```bash
docker build --no-cache --tag responder:0.1.0 .
docker run --publish 8080:8080 --detach --name responder responder:0.1.0
```

#### Docker-Compose

```bash
docker-compose up --build
```
