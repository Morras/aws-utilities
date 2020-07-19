import urllib.request
from urllib.error import HTTPError
import os
import boto3

WEBSITE_URLS = os.environ['WEBSITE_URLS']
SNS_TOPIC = os.environ['SNS_TOPIC']

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    
    failled_urls = []
    
    for url in WEBSITE_URLS.split(','):
        try:
            request = urllib.request.Request(url=url.strip(), method='HEAD')
            response = urllib.request.urlopen(request)
            if response.status != 200:
                failled_urls.append(url)
                print("Received unexpected status code {} back from request to {}".format(response.status. url))
        except HTTPError as err:
            failled_urls.append(url)
            print('Failed to send request to {} with error: {} ({})'.format(url, err.reason, err.code))
        except:
            failled_urls.append(url)
            print('Failed to send request to {}'.format(url))
    
    sns_client.publish(
        TopicArn=SNS_TOPIC,
        Message="Failed to get a positive respond to HTTP request to the following URLS: {}".format(str(failed_urls)),
        Subject="One or more websites are not responding as expected"
    )
    