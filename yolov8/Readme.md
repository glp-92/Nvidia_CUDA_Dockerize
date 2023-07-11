## YoloV8
1. [Check Install Ultralytics Docker tab](https://docs.ultralytics.com/quickstart/)
    ```
    docker pull ultralytics/ultralytics:latest
    docker run -it --ipc=host --gpus all ultralytics/ultralytics:latest
    ```
2. Create `server.py` script and place endpoints of the API
    - `/`: displays welcome message
    - `/version`: retrieves Pytorch version and Cuda devices
    - `/predict`: predicts an image passed by {"image"} field on body, encoded on base64
3. Create `Dockerfile` and configure the imagen
    ```
    FROM ultralytics/ultralytics:latest

    # Aditional dependencies if exists
    # RUN apt-get update && apt-get install -y <packagename>

    # Copy all files on these folder to /app folder on container
    COPY . /app
    # Change the workdir to /app
    WORKDIR /app

    # Install dependencies, flask in this case
    RUN pip install -r requirements.txt

    # Expose Flask port 5000
    EXPOSE 5000

    # cmd to run server
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
6. Run the `client.py` file to test an image processing:
    ```
    import cv2
    import requests
    import base64
    import json, time

    # Read img
    image = cv2.imread("test.jpg")

    # Convert to base64
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    payload = {
        'image': image_base64
    }

    # Send POST request to endpoint
    url = 'http://localhost:5000/predict'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    # Show response
    print(response.json())
    ```
    
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