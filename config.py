ORGANIZATIONS = [
    {
        "name": "OpenAlcoholics",
        "token_environment_variable_name": "GITHUB_TOKEN_OPENALCOHOLICS",
        "repos": [
            {
                "name": "postgres-operator",
                "serviceaccount": {
                    "name": "postgresoperator-github",
                    "namespace": "postgres-operator",
                }
            }
        ],
    },
]

KUBECONFIG_SECRET_NAME = "KUBECONFIG_RAW"

CLUSTER = {
    "name": "carstens-tech",
    "url": "https://k8s.carstens.tech:6443",
}
