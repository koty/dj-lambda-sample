Django on AWS Lambda sample using serverless framework and serverless-wsgi plugin.

# Instalation

```
npm install -g serverless
git clone https://github.com/koty/dj-lambda-sample.git
cd dj-lambdsa-sample
npm install
serverless deploy --aws-profile your_some_profile
```
# Limitations
This sample doesn't work properly because of using SQLite in settings.py. 
So please fix settings.py like RDS to connect database.
