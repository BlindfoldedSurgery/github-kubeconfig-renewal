import base64
from typing import Dict, Optional

from kubernetes import client, config
from kubernetes.client import V1Secret, V1SecretList

from . import UnknownServiceaccountToken

try:
    config.load_incluster_config()
except config.config_exception.ConfigException:
    config.load_kube_config()


api = client.CoreV1Api()


def find_serviceaccount_token(name: str, namespace: str) -> Dict[str, str]:
    secret_list: V1SecretList = api.list_namespaced_secret(namespace)
    for secret in secret_list.items:
        if secret.type != "kubernetes.io/service-account-token":
            continue

        serviceaccount_name = secret.metadata.annotations.get("kubernetes.io/service-account.name")
        if serviceaccount_name == name:
            break
    else:
        raise UnknownServiceaccountToken(f"couldn't find secret for serviceaccount `{name}` in `{namespace}`")

    return get_serviceaccount_info_from_secret(secret)


def get_serviceaccount_info_from_secret(secret: V1Secret) -> Dict[str, str]:
    token = base64.b64decode(secret.data["token"]).decode("utf-8")
    namespace = base64.b64decode(secret.data["namespace"]).decode("utf-8")

    return {
        "token": token,
        "ca.crt": secret.data["ca.crt"],
        "namespace": namespace,
    }
