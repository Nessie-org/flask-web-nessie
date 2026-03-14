# flask-web-nessie
A Flask web server for the [Nessie](https://github.com/Nessie-org) ecosystem. It serves a frontend interface and exposes a REST API for discovering and executing Nessie plugins.

---

## Installation

Clone the repository and install dependencies from `requirements.txt`:

It is necessary to install web, one visualization plugin as well as data provider plugin that web server could work properly.
```bash
git clone https://github.com/Nessie-org/flask-web-nessie.git
cd flask-web-nessie
pip install -r requirements.txt
```

---

## Running the server
```bash
python main.py
```

---

## Backend Endpoints

### `GET` — Index

Serves the main HTML interface. Any URL that does not match a defined route will fall through to this handler.

| Field            | Details               |
|------------------|-----------------------|
| **Method**       | `GET`                 |
| **URL**          | any unspecified route |
| **Body**         | not expected          |
| **Query params** | not expected          |
| **Returns**      | `HTML`                |

---

### `POST` — Perform Action

Executes a named action using a specified plugin.

| Field            | Details           |
|------------------|-------------------|
| **Method**       | `POST`            |
| **URL**          | `/perform-action` |
| **Body**         | JSON (see below)  |
| **Query params** | not expected      |
| **Returns**      | `HTML`            |

#### Request body
```json
{
  "Action Name": "the action you want to perform",
  "payload": {
    "...": "plugin-specific fields"
  },
  "Plugin Name": "name of the plugin that handles this action"
}
```

#### Example
```json
{
  "Action Name": "visualise_graph",
  "payload": {
    "Graph": {
      "nodes": [{ "id": "A" }, { "id": "B" }],
      "edges": [{ "from": "A", "to": "B" }]
    }
  },
  "Plugin Name": "neisse-graph-visualiser-block"
}
```

---

### `GET` — Get Plugins

Returns a list of plugins that support a given action.

| Field            | Details                         |
|------------------|---------------------------------|
| **Method**       | `GET`                           |
| **URL**          | `/plugins`                      |
| **Body**         | not expected                    |
| **Query params** | `Action Name` — the action name |
| **Returns**      | `JSON`                          |

#### Query param

| Param         | Type     | Description                          |
|---------------|----------|--------------------------------------|
| `Action Name` | `string` | The action name to filter plugins by |

#### Example request
```
GET /plugins?Action Name=visualise_graph
```

#### Response
```json
[
  {
    "name": "neisse-graph-visualiser-block",
    "requirements": {}
  }
]
```

---

## Repository

[https://github.com/Nessie-org/flask-web-nessie](https://github.com/Nessie-org/flask-web-nessie)

---

## License

See [LICENSE](./LICENSE) for details.
