ORGANIZATIONS = [
    {
        "name": "BlindfoldedSurgery",
        "token_environment_variable_name": "GITHUB_TOKEN_BLINDFOLDEDSURGERY",
        "repos": [
            {
                "name": "github-kubeconfig-renewal",
                "serviceaccount": {
                    "name": "github-config-renewal",
                    "namespace": "mgmt",
                }
            },
            {
                "name": "github-action-helm",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "action-example",
                }
            },
            {
                "name": "architecture",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "blindfoldedsurgery",
                }
            },
            {
                "name": "ingress-dashboard",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "mgmt",
                }
            },
            {
                "name": "bus-frontend",
                "serviceaccount": {
                    "name": "github",
                    "namespace": "timhatdiehandandermaus",
                }
            },
        ],
    },
]

KUBECONFIG_SECRET_NAME = "KUBECONFIG_RAW"

CLUSTER = {
    "name": "carstens-tech",
    "url": "https://k8s.carstens.tech:6443",
}
