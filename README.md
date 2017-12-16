Django on AWS Lambda sample using serverless framework and serverless-wsgi plugin.

# Instalation

```
npm install -g serverless
git clone https://github.com/koty/dj-lambda-sample.git
cd dj-lambdsa-sample
npm install
copy serverless.env.yml.template to serverless.env.yml and edit values
edit settings.py
serverless deploy --aws-profile your_some_profile
```
