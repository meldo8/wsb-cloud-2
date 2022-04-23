import json
import logging
import os

import boto3
from aws_xray_sdk.core import patch_all
from boto3.dynamodb.conditions import Attr

logger = logging.getLogger()
logger.setLevel(os.environ["LOGGING_LEVEL"])

patch_all()

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["PEOPLE_TABLE_NAME"])


def handler(event, context):

    only_people_filter = Attr("id").ne("last_update")

    scan_results = table.scan(
        FilterExpression=only_people_filter,
        ProjectionExpression="id,#n,#s",
        ExpressionAttributeNames={"#n": "name", "#s": "surname"},
    )

    if scan_results.get("LastEvaluatedKey"):
        logger.debug(
            "Query result exceeded limit of 1MB. LastEvaluatedKey is %s",
            scan_results["LastEvaluatedKey"],
        )

    logger.debug("Result count: %s", scan_results["Count"])
    logger.debug("Number of documents scanned: %s", scan_results["ScannedCount"])

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps({"items": scan_results["Items"]}),
    }
