# Low code vinyl

This is a proof-of-concept application using [appsmith](https://github.com/appsmithorg/appsmith), a custom Python API, and a Postgres database.

The solution is containerized and developed locally using Kubernetes.

### To-do:

- Add appsmith
-- redis
-- mongo

## Local environment setup

### To install docker:

[source](https://docs.docker.com/engine/install/ubuntu/)

```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl start docker
```

### To install kind:

[source](https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries)

1. Download the latest release of kind by running the following command:

    ```
    curl -Lo ./kind https://kind.sigs.k8s.io/dl/vX.Y.Z/kind-linux-amd64
    ```

    Replace X.Y.Z with the latest version of kind. You can find the latest version by visiting the releases page on GitHub.

1. Make the kind binary executable:

    ```
    chmod +x ./kind
    ```

1. Move the kind binary to a directory in your PATH by running the following command:

    ```
    sudo mv ./kind /usr/local/bin/kind
    ```

### To install kubectl:

[source](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

1.     sudo apt-get update && sudo apt-get install -y apt-transport-https
1.     curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
1.     echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
1.     sudo apt-get update
1.     sudo apt-get install -y kubectl

### To install helm:

[source](https://helm.sh/docs/intro/install/#from-the-binary-releases)

1. Download the latest version of helm by running the following command:

        curl -Lo ./helm.tar.gz https://get.helm.sh/helm-vX.Y.Z-linux-amd64.tar.gz

    Replace X.Y.Z with the latest version of helm. You can find the latest version by visiting the releases page on GitHub.

1. Extract the helm binary from the downloaded archive by running the following command:

        tar -zxvf ./helm.tar.gz

1. Move the helm binary to a directory in your PATH by running the following command:

        sudo mv ./linux-amd64/helm /usr/local/bin/helm

## Running the application

1. Create the `kind` cluster

        scripts/check_create_kind_cluster
