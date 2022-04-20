# Final project of the cloud subject

### Intro

Simple AWS Lambda, which is retrieving people sensitive data in a very open manner from DynamoDB.
Technology used:
 - [AWS Api Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
 - [AWS Lambda](https://aws.amazon.com/lambda/)
 - [AWS X-Ray](https://aws.amazon.com/xray/)
 - [AWS Cloud Watch](https://aws.amazon.com/cloudwatch/)
 - [AWS DynamoDB](https://aws.amazon.com/dynamodb)
 - [Serverless framework](https://www.serverless.com/)

### Installation

1. Use `make prepare-env` to install all tools in your local env.
2. Install plugins with `make install-plugins`

### Invoke functions

- Get people `make invoke name=<name of created stage>`

## Tracing

AWS X-Ray is used for tracing calls within ApiGateway and Lambda.
Tracing allows us to view how applications is behaving with metrics regarding Lambda calls, DynamoDB operations.

## Logging & Monitoring

CloudWatch is a monitoring and observability service.
CloudWatch provides data and actionable insights to monitor applications (Lambda, API Gateway and DynamoDB),
respond to system-wide performance changes, and optimize resource utilization. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events.


### Deployment

Code will be deployed to `name` stage in Gateway API.
This way you can test your code in the cloud.
With stages each environment can be separated allowing multiple people to develop and test their code in the cloud without interfering each other.
In order to deploy your code execute the command.

```bash
make deploy-stage name=test_name
```

You will receive a list of all deployed endpoints and functions.

```bash
Serverless: Stack update finished...
Service Information
service: wsb-cloud-2
stage: dm
region: eu-central-1
stack: wsb-cloud-2-dm
resources: 54
api keys:
  None
endpoints:
  GET - https://8ijas87ds9.execute-api.eu-central-1.amazonaws.com/dm/people
functions:
  getPeople wsb-cloud-2-dm-getPeople
```

Please remove your code after you are done by running.

```bash
make remove-stage name=test_name
```
