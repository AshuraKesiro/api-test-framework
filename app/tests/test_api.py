import pytest

@pytest.mark.asyncio
async def test_health(client):
    resp = await client.get("/health")
    assert resp.status_code == 200
    assert resp.json().get("status") == "ok"

@pytest.mark.asyncio
async def test_missing_route(client):
    resp = await client.get("/not-found")
    assert resp.status_code in (404, 405)
