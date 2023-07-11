## Nvidia - Pytorch
1. Install [Nvidia Docs Pytorch Image pull](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/running.html)
    ```
    docker pull nvcr.io/nvidia/pytorch:23.06-py3
    ```
    - Is needed to match pytorch image version with GPU drivers on the system.
    - [Pytorch Versions](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/index.html)
2. Test succesful image pull on Docker >= `19.03`:
    ```
    docker run --gpus all -it --rm nvcr.io/nvidia/pytorch:<xx.xx>-py3
    ```

### Writing custom server to Pytorch infering
1. Create `server.py` script and place endpoints of the API
    - `/`: displays a `hello-world` message
    - `/version`: displays current `torch` version
    ```
    from prediction import get_torch_version
    from flask import Flask
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return "Welcome to Cuda Pytorch container!"

    @app.route("/version", methods=["POST"])
    def get_version():
        return f"{get_torch_version()}"

    if __name__ == '__main__':
        app.run(host='0.0.0.0')
    ```
2. Create `prediction.py` script that retrieves `torch` version
    ```
    import torch

    def get_torch_version():
        return f"Version de Pytorch: {torch.__version__}. Cuda: {torch.cuda.is_available()}. GPU device: {torch.cuda.current_device()}. GPU name: {torch.cuda.get_device_name(0)}"
    ```
3. Create `Dockerfile` and configure the imagen
    ```
    FROM nvcr.io/nvidia/pytorch:21.04-py3

    # Aditional dependencies if exists
    # RUN apt-get update && apt-get install -y <packagename>

    # Copy all files on these folder to /app folder on container
    COPY . /app
    # Change the workdir to /app
    WORKDIR /app

    # Install Python dependencies
    # RUN pip install -r requirements.txt

    # Expose Flask port 5000
    EXPOSE 5000

    # Command to launch the server 'python server.py'
    CMD ["python", "server.py"]
    ```
4. Build the image from the `Dockerfile`
    ```
    docker build -t image-name .
    ```
    - -t specifies image label
    - . indicates place of the `Dockerfile`
5. Run the container associated to the image
    ```
    docker run -p 5000:5000 --gpus all -it image-name
    ```
    - -p mapping port 5000 of host machine to container port 5000
    - --gpus map gpu to the image
    - -it specifies name of the image
    
### Docker Compose
1. [Install cmd](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04):
    - `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
    - `sudo chmod +x /usr/local/bin/docker-compose`
    - `docker-compose --version`
2. Create `docker-compose.yml`:
    ```
    version: '3'
    services:
        app:
            build:
                context: .
                dockerfile: dockerfile
            ports:
                - 5000:5000
            deploy:
                resources:
                    reservations:
                    devices:
                    - capabilities: [gpu]
                        driver: nvidia
    ```
    - context maps to current directory
    - dockerfile maps to specified dockerfile
    - ports attach host port to container port
    - runtime: nvidia specifies Nvidia Container Toolkit GPU support
3. Run the compose by `docker-compose up`
4. Finish and delete containers by `docker-compose down`