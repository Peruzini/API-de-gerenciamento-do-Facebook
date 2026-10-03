from typing import Any

import httpx


class MetaGraphClient:
    """Cliente isolado para chamadas à Meta Graph API.

    Tokens devem ser fornecidos pelo backend seguro. Este cliente nunca deve
    expor credenciais em respostas ou logs.
    """

    def __init__(
        self,
        *,
        base_url: str,
        graph_version: str,
        access_token: str,
        timeout: float = 15.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._graph_version = graph_version.strip("/")
        self._access_token = access_token
        self._timeout = timeout

    async def get(self, path: str, *, params: dict[str, Any] | None = None) -> dict[str, Any]:
        request_params = dict(params or {})
        request_params["access_token"] = self._access_token

        url = f"{self._base_url}/{self._graph_version}/{path.lstrip('/')}"

        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.get(url, params=request_params)
            response.raise_for_status()
            return response.json()
