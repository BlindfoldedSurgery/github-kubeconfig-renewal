from typing import Dict, Any


def create(*, cluster_name: str, cluster_url: str, user_name: str, user_token: str, ca_data: str,
           context_name: str = "default") -> Dict[str, Any]:
    return {
        "apiVersion": "v1",
        "kind": "Config",
        "clusters": [{
            "name": cluster_name,
            "cluster": {
                "certificate-authority-data": ca_data,
                "server": cluster_url,
            },
        }],
        "users": [{
            "name": user_name,
            "user": {
                "token": user_token,
            },
        }],
        "contexts": [{
            "name": context_name,
            "context": {
                "cluster": cluster_name,
                "user": user_name,
            },
        }],
        "current-context": context_name,
    }
