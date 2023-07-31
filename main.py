import inspect
import os
import sys
from functools import lru_cache
from typing import Dict, Union, Optional

import github
import yaml
from github import Auth, Github, Organization, Repository, AuthenticatedUser

import config
from src import create_logger, kube, kubeconfig, UnknownServiceaccountToken

GithubEntity = Union[Organization, AuthenticatedUser]


@lru_cache()
def get_kubeconfig_for_serviceaccount(name: str, namespace: str) -> str:
    serviceaccount = kube.find_serviceaccount_token(name, namespace)

    k8sconfig = kubeconfig.create(
        cluster_name=config.CLUSTER["name"],
        cluster_url=config.CLUSTER["url"],
        user_name=name,
        user_token=serviceaccount.token,
        ca_data=serviceaccount.ca_certificate,
    )

    return yaml.dump(k8sconfig)


def create_secret(github_entity: Union[Repository, Organization], entity_config: Dict) -> bool:
    logger = create_logger(inspect.currentframe().f_code.co_name)

    secret_value = get_kubeconfig_for_serviceaccount(
        entity_config["serviceaccount"]["name"],
        entity_config["serviceaccount"]["namespace"],
    )

    try:
        github_entity.create_secret(config.KUBECONFIG_SECRET_NAME, secret_value)
    except github.GithubException:
        logger.error(f"failed to retrieve github user for {entity_config}", exc_info=True)
        return False
    except UnknownServiceaccountToken:
        logger.error(f"failed to retrieve serviceaccount token for {entity_config}", exc_info=True)
        return False

    return True


def get_github_entity(github_api: Github, entity_config: dict) -> Optional[GithubEntity]:
    logger = create_logger(inspect.currentframe().f_code.co_name)

    try:
        return github_api.get_organization(entity_config["name"])
    except github.GithubException:
        try:
            # fake it til you make it
            return github_api.get_user(entity_config["name"])
        except github.GithubException:
            logger.error(f"failed to retrieve github user for {entity_config}", exc_info=True)
            return None
    except UnknownServiceaccountToken:
        logger.error(
            f"failed to retrieve serviceaccount token for {entity_config}",
            exc_info=True,
        )
        return None


def get_github_repo(entity: GithubEntity, repo: dict) -> Optional[Repository]:
    logger = create_logger(inspect.currentframe().f_code.co_name)

    try:
        logger.info(f"create secret for repo {repo}")
        github_repo = entity.get_repo(repo["name"])
    except github.GithubException:
        logger.error(f"couldn't retrieve repo {repo}", exc_info=True)
        return None

    return github_repo


def update_github_secrets() -> bool:
    logger = create_logger(inspect.currentframe().f_code.co_name)

    success = True
    for organization in config.ORGANIZATIONS:
        # don't access GitHub api if not necessary
        if not organization.get("repos") and not organization.get("serviceaccount"):
            logger.debug(f"skip {organization} due to no defined/empty repos/serviceaccount key")
            continue

        access_token = os.getenv(organization["token_environment_variable_name"])
        if not access_token:
            logger.error(f"empty access_token for {organization}")
            success = False
            continue

        auth = Auth.Token(access_token)
        github_api = Github(auth=auth)

        github_entity = get_github_entity(github_api, organization)
        if not github_entity:
            success = False
            continue

        if organization.get("serviceaccount"):
            logger.info(f"create secret for organization {organization}")
            if not create_secret(github_entity, organization):
                success = False

        for repo in organization["repos"]:
            github_repo = get_github_repo(github_entity, repo)
            if not github_repo:
                success = False
                continue

            if not create_secret(github_repo, repo):
                success = False

    return success


if __name__ == "__main__":
    if not update_github_secrets():
        sys.exit(1)
