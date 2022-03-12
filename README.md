# Python Messaging App for Slack
## Requirements
Configure this applications before in your local computer:

- [Jenkins](https://www.jenkins.io/) is a tool to be used for create your pipeline for testing, deploying, etc.
- [Python 3.10.0](https://www.python.org/) is the programming language used to create the application.
- [Docker](https://www.docker.com/) is a tool used to create a custom image of your application and then deploy it into a cluster.
- [Kubernetes](https://kubernetes.io/) is a tool that enables the creation of clusters in a local machine or even a virtual machine, it is used along with Docker to create big applications.
- [Helm](https://helm.sh/) is a package manager for the kubernetes files, it is used within the project.

## Installation

### Github
Add this repository to your local machine.
```bash
git clone git@github.com:nabetse28/python-message-slack.git
```
Get into the folder.
```bash
cd python-message-slack/
```
### Python
You need to get a `Webhook` from your app in Slack.

Create a new `Python Virtual Environment`.

```bash
python3 -m venv venv
```

Activate the `venv` with the following command.
```bash
source ./venv/bin/activate
```

Install all the dependencies of the project.
```bash
pip install -r requirements.txt
```

Run the project
```bash
python app.py
```

## Help
Exit `venv` mode with the following command
```bash
deactivate
```
