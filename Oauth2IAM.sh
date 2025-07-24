# https://yandex.cloud/ru/docs/iam/operations/iam-token/create
curl \
  --request POST \
  --data '{"yandexPassportOauthToken":"y0__..."}' \
  https://iam.api.cloud.yandex.net/iam/v1/tokens