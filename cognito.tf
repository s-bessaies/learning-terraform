resource "aws_cognito_user_pool" "pool" {
  name = "mypool"
}

resource "aws_cognito_user_pool_client" "client" {
  name = "client"
  allowed_oauth_flows_user_pool_client = true
  generate_secret = false
  allowed_oauth_scopes = ["aws.cognito.signin.user.admin","email", "openid", "profile"]
  allowed_oauth_flows = ["implicit", "code"]
  explicit_auth_flows = ["ADMIN_NO_SRP_AUTH", "USER_PASSWORD_AUTH"]
  supported_identity_providers = ["COGNITO"]

  user_pool_id = aws_cognito_user_pool.pool.id
   callback_urls = ["https://gpsessions.com/login"]
   logout_urls = ["https://gpsessions.com/logout"]
}

resource "aws_cognito_user" "user_01" {
  user_pool_id = aws_cognito_user_pool.pool.id
  username = "user01"
  password = "USER@123"
}