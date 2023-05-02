# 5 NLP Models
# Installation

You can deploy this service using kubernetes, docker compose


## Using Docker
You have to have installed Docker
```bash
git clone https://github.com/ArsenyVel/5_nlp_models

docker build -t 5_models_app -f Dockerfile.tt .

# to run container on detached mode and be exposed on port 4000
sudo docker run -p 4000:4000 -d  5_models_app
```
Reach your service on 4000 port

If port 4000 in use try to change the port number in the main.py and Dockerfile.tt . 

## minikube

Make sure you minikube cluster has access to local docker images if not
reuse the Docker daemon from Minikube with eval $(minikube docker-env)
```bash

git clone https://github.com/ArsenyVel/5_nlp_models

docker build -t 5_models_app -f Dockerfile.tt .

kubectl apply -f app.yaml
```
