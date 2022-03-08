#!/bin/bash

RELEASE_NAME="python-message-slack"

echo "Configuring namespace..."
if kubectl get namespace ${NAMESPACE}; then
  echo -e "Namespace ${NAMESPACE} found!!"
else
  kubectl create namespace ${NAMESPACE}
  echo -e "Namespace ${NAMESPACE} created!!"
fi

echo -e "Checking if we can deploy things to the namespace..."
if kubectl auth can-i create deployment --namespace ${NAMESPACE}; then
  echo -e "Deploying charts into ${NAMESPACE}..."
  helm upgrade ${RELEASE_NAME} charts/${RELEASE_NAME}  --install --set slackSecret.url=${SLACK_URL} --namespace ${NAMESPACE}
else
  echo -e "The charts files weren't able to be deployed"
fi
