# import the JSON utility package
import json
# import the Python math library
import math

# import the AWS SDK (for Python the package name is boto3)
import boto3
# import packages for date/time formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# replace 'YOUR_DYNAMODB_TABLE_NAME' with your actual table when using this code
table = dynamodb.Table('YOUR_DYNAMODB_TABLE_NAME')

# store the current time in a human-readable format
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the Lambda handler function
def lambda_handler(event, context):

    # extract the two numbers from the Lambda event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))

    # write result and time to the DynamoDB table
    response = table.put_item(
        Item={
            'ID': str(mathResult),
            'LatestGreetingTime': now
        }
    )

    # return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(mathResult))
    }


# return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(mathResult))
    }
