# Initial setup
## Commands
- choco install awscli
- aws configure
- npm install -g serverless
- npm install --save-dev serverless-iam-roles-per-function
- npm install --save-dev serverless-pseudo-parameters

# Working with CLI
- https://serverless.com/framework/docs/providers/aws/cli-reference/

## Running the function
- https://serverless.com/framework/docs/providers/aws/cli-reference/invoke/
- serverless invoke --function addGamer --stage dev --region ap-southeast-1 --path payload/add-gamer.json
- serverless invoke -f addGamer -s dev -r ap-southeast-1 --path payload/add-gamer.json

## Checking for the logs
- https://serverless.com/framework/docs/providers/aws/cli-reference/logs/
- serverless logs -f addGamer -s dev -r ap-southeast-1 --startTime 2h