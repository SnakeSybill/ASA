#Nome da aplicação na nuvem
service: mobile-serverless-app 

# Plugins utilizados em desenvolvimento
plugins:
  - serverless-webpack
  - serverless-offline

# Configuração de plugins
custom:
  webpack:
    webpackConfig: ./webpack.config.js
    includeModules: true

# Provedor dos serviços de nuvem
provider:
  name: aws
  runtime: nodejs8.10
  stage: dev
  region: us-east-1

# Configurações do IAM
iamRoleStatements:
    # Neste caso a configuração permite que as funções executem as seguintes ações 
    - Effect: Allow 
      Action:           
        - dynamodb:DescribeTable
        - dynamodb:Query
        - dynamodb:Scan
        - dynamodb:GetItem
        - dynamodb:PutItem
        - dynamodb:UpdateItem
        - dynamodb:DeleteItem
    # Recursos nos quais as ações são permitidas (todos os bancos na região us-east-1)
      Resource: "arn:aws:dynamodb:us-east-1:*:*"

# Funções desenvolvidas
functions:
  # Função PutUsuario
  PutUsuario:
    # Arquivo onde a função se encontra
    handler: handler.PutUsuario
    # Eventos que disparam a função
    events:
      - http:
          # Rota de API para a função
          path: put-usuario
          # Método HTTP suportado
          method: post
          # Permite CORS
          cors: true
          # Autorizada pelo usuário do IAM configurado
          authorizer: aws_iam
          