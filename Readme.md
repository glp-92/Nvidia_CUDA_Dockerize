# Nvidia Cuda Container Implementation

This repository provides implementation paths to dockerize some DL Python frameworks and libraries.

Tested on Ubuntu 20.04 LTS with Nvidia GTX 1050. 

### Requirements:
1. [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es) as container manager

2. Install [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
    ```
    sudo apt-get update \
        && sudo apt-get install -y nvidia-container-toolkit-base
    ```
3. To confirm succesful install:
    ```
    nvidia-ctk --version
    ```

Check the following implementations docs:
- [Tensorflow Cuda Docker DOC](tensorflow/Readme.md)
- [Pytorch Cuda Docker DOC](pytorch/Readme.md)
- [YoloV8 Cuda Docker DOC](yolov8/Readme.md)

To do list:
- Finish current implementations
- Kubernetes Cluster for highly available infering context
- Kubernetes Cluster for GPU management
- Provide safe API to inject custom prediction func
- Code and model optimizations
