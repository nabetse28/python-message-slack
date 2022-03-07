import os
import logging
import requests


class SlackUtility:
    """
    Class to handle the slack notification
    """

    slack_url = None
    slack_channel = None

    def __init__(self):
        """
        Initialization of class
        """
        self.slack_url = os.getenv("SLACK_URL")
        self.slack_channel = os.getenv("SLACK_URL", "#random")

    def send(self, text=None):
        """
        Functions that sends messages to a specific slack channel
        """
        try:

            msg = {
                "channel": self.slack_channel,
                "text": f"{text}" if text is not None else "",
                "username": "esteban-project",
            }
            headers = {"accept": "application/json", "Content-Type": "application/json"}
            logging.info("Sending slack message")

            return requests.post(self.slack_url, json=msg, headers=headers, verify=False)
        except requests.HTTPError as exc:
            logging.info("Exception in sending message to slack %s", exc)
