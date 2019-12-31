var = \
{
    'SMSMessageData': {
        'Message': 'Sent to 1/1 Total Cost: NGN 2.2000',
        'Recipients': [
            {
                'cost': 'NGN 2.2000',
                'messageId': 'ATXid_26aa6a0bbc15555867ce1004b19e60fb',
                'status': 'Success',
                'number': '+2348121704436',
                'messageParts': 1,
                'statusCode': 101
            }
        ]
    }
}

print(var['SMSMessageData']['Message'])

