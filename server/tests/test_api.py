from datetime import datetime

from flask import Response

def test_get_clients(client):
    response = client.get("/api/client")
    data = response.get_json()
    assert "clients" in data
    assert (
        [client["name"] for client in data["clients"]] ==
        ["Client A", "Client B", "Client C"]
    )


def test_post_get_feature_request(client):
    data = {
        "title": "Test feature",
        "description": "This is a test feature",
        "client_id": 1,
        "priority": "Low",
        "target_date": datetime.now().isoformat(),
    }
    response = client.post("/api/feature-request", json=data)
    out = response.get_json()
    assert out["id"]
    assert out["title"] == "Test feature"

    response2 = client.get(f"/api/feature-request/{out['id']}")
    out2 = response2.get_json()
    assert out2["id"]
    assert out2["title"] == "Test feature"
