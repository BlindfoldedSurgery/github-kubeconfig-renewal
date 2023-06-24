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
            {
                "name": "github-kubeconfig-renewal",
                "serviceaccount": {
                    "name": "github-config-renewal",
                    "namespace": "mgmt",
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
            {
                "name": "festival-api",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "festival",
                }
            },
            {
                "name": "telegram-songlinker-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-songlinker-bot",
                }
            },
            {
                "name": "twittergram",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "twittergram",
                }
            },
            {
                "name": "telegram-speech-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "bob",
                }
            },
            {
                "name": "wheel-of-misfortune-backend",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "misfortune",
                }
            },
            {
                "name": "telegram-moderator-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "random-action-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "vodka-az",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "vodka-az",
                }
            },
            {
                "name": "probability-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "wheel-of-misfortune-app",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "misfortune",
                }
            },
            {
                "name": "papyrus-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "papyrus",
                }
            },
            {
                "name": "hhh-diff-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "kwbot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "papyrus-api",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "papyrus",
                }
            },
            {
                "name": "nhbot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "bildbot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "deletespamtelegrambot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "festival-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "festival",
                }
            },
            {
                "name": "annoying-mention-echo-bot",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "telegram-bots",
                }
            },
            {
                "name": "k8s-pypi",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "pypi",
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
