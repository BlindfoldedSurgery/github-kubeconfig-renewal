import base64
from typing import Dict

from kubernetes import client, config
from kubernetes.client import V1Secret, V1SecretList

config.load_kube_config()
api = client.CoreV1Api()


def find_serviceaccount_token(name: str, namespace: str) -> Dict[str, str]:
    secret_list: V1SecretList = api.list_namespaced_secret(namespace)
    for secret in secret_list.items:
        serviceaccount_name = secret.metadata.annotations.get("kubernetes.io/service-account.name")
        if serviceaccount_name == name:
            break
    else:
        raise ValueError(f"couldn't find secret for serviceaccount `{name}` in `{namespace}`")

    return get_serviceaccount_info_from_secret(secret.metadata.name, secret.metadata.namespace)


def get_serviceaccount_info_from_secret(name: str, namespace: str) -> Dict[str, str]:
    secret: V1Secret = api.read_namespaced_secret(name, namespace)

    token = base64.b64decode(secret.data["token"]).decode("utf-8")
    namespace = base64.b64decode(secret.data["namespace"]).decode("utf-8")
    return {
        "token": token,
        "ca.crt": secret.data["ca.crt"],
        "namespace": namespace,
    }
