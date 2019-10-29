from flask import Response

def test_get_clients(client):
    response = client.get("/api/client")
    data = response.get_json()
    assert "clients" in data
    assert (
        [client["name"] for client in data["clients"]] ==
        ["Client A", "Client B", "Client C"]
    )
