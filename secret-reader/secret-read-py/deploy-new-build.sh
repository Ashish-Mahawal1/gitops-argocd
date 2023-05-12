#!/bin/bash/
cd ./src
docker build . -t ashishmahawal/read-secret
docker push ashishmahawal/read-secret

kubectl delete -f ../deployment/app.yml
kubectl apply -f ../deployment/app.yml

sleep 15

kubectl get pods secret-reader
kubectl logs secret-reader