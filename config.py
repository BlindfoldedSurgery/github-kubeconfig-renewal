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
            },
        ],
    },
    {
        "name": "torbencarstens",
        "token_environment_variable_name": "GITHUB_TOKEN_TORBENCARSTENS",
        "repos": [
            {
                "name": "container-workshop",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "static",
                }
            },
        ]
    },
    {
        "name": "preparingforexams",
        "token_environment_variable_name": "GITHUB_TOKEN_PREPARINGFOREXAMS",
        "repos": [
            {
                "name": "telegram-horoscope-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
        ]
    },

]

KUBECONFIG_SECRET_NAME = "KUBECONFIG_RAW"

CLUSTER = {
    "name": "carstens-tech",
    "url": "https://k8s.carstens.tech:6443",
}
