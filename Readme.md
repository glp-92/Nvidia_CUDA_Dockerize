# Nvidia Cuda Container Implementation

This repository provides implementation paths to dockerize some DL Python frameworks and libraries.

Tested on Ubuntu 20.04 LTS with Nvidia GTX 1050. 

### Requirements:
1. [Install Docker](https://docs.docker.com/engine/install/) as container manager. Found some privilege uncompatibilities with Docker Desktop

2. Install [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
    ```
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
        sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
        sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
      && \
        sudo apt-get update
    ```
    ```
    sudo apt-get update \
        && sudo apt-get install -y nvidia-container-toolkit
    ```
3. To confirm succesful install:
    ```
    nvidia-ctk --version
    ```

### Check the following implementation docs:
- [Tensorflow Cuda Docker](tensorflow/Readme.md)
- [Pytorch Cuda Docker](pytorch/Readme.md)
- [YoloV8 Cuda Docker](yolov8/Readme.md)

### To do list:
- Finish current implementations
- Kubernetes Cluster for highly available infering context
- Kubernetes Cluster for GPU management
- Provide safe API to inject custom prediction func
- Code and model optimizations
