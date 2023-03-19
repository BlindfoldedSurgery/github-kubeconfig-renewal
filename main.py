import os
from typing import Dict

import yaml
from github import Github

import config
from src import kube, kubeconfig


def get_kubeconfig_for_serviceaccount(name: str, namespace: str) -> str:
    serviceaccount = kube.find_serviceaccount_token(name, namespace)
    k8sconfig = kubeconfig.create(cluster_name=config.CLUSTER["name"], cluster_url=config.CLUSTER["url"],
                                  user_name=name, user_token=serviceaccount["token"], ca_data=serviceaccount["ca.crt"])

    return yaml.dump(k8sconfig)


def create_organization_secret(github_organization, organization: Dict) -> bool:
    secret_value = get_kubeconfig_for_serviceaccount(organization["serviceaccount"]["name"],
                                                     organization["serviceaccount"]["namespace"])
    return github_organization.create_secret(config.KUBECONFIG_SECRET_NAME, secret_value)


def create_repository_secret(github_repo, repo: Dict) -> bool:
    secret_value = get_kubeconfig_for_serviceaccount(repo["serviceaccount"]["name"],
                                                     repo["serviceaccount"]["namespace"])
    return github_repo.create_secret(config.KUBECONFIG_SECRET_NAME, secret_value)


def update_github_secrets():
    for organization in config.ORGANIZATIONS:
        # don't access GitHub api if not necessary
        if not organization.get("repos") and not organization.get("serviceaccount"):
            continue

        access_token = os.getenv(organization["token_environment_variable_name"])
        github_api = Github(access_token)

        github_organization = github_api.get_organization(organization["name"])
        if organization.get("serviceaccount"):
            create_organization_secret(github_organization, organization)

        for repo in organization.get("repos", []):
            github_repo = github_organization.get_repo(repo["name"])
            create_repository_secret(github_repo, repo)


if __name__ == "__main__":
    update_github_secrets()
