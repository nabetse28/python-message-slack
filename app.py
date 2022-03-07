from utils import slack_util

import logging

SLACK = slack_util.SlackUtility()


def main():
    logging.info("Sending message to slack...")
    SLACK.send("This is a message from Slack App :sweat_smile:")


if __name__ == "__main__":
    main()
