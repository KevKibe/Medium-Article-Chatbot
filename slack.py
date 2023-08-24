import sys
import requests
import getopt


def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    response = requests.post("https://hooks.slack.com/services/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",
                             data = payload)
    print = response.text
def main(argv):

    message = ''
    try : opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('message')
        sys.exit(2)
    if len(opts) ==0:
        message = "Hello, World"
    for opt, arg in opts:
        if opts == "-h":
