import base64

from kubernetes import client, config
from kubernetes.client import V1Secret, V1SecretList

from . import UnknownServiceaccountToken, ServiceaccountInfo

try:
    config.load_incluster_config()
except config.config_exception.ConfigException:
    config.load_kube_config()


api = client.CoreV1Api()


def find_serviceaccount_token(name: str, namespace: str) -> ServiceaccountInfo:
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


def get_serviceaccount_info_from_secret(secret: V1Secret) -> ServiceaccountInfo:
    token = base64.b64decode(secret.data["token"]).decode("utf-8")
    namespace = base64.b64decode(secret.data["namespace"]).decode("utf-8")

    # fmt: off
    return ServiceaccountInfo(
        ca_certificate=secret.data["ca.crt"],
        namespace=namespace,
        token=token
    )
