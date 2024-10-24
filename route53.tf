data "aws_route53_zone" "my_domain" {
  name = "gpsessions.com"
  private_zone = false
}

# resource "aws_api_gateway_domain_name" "dns_public_env_name" {
#   domain_name = "api.gpsessions.com"  
# }

resource "aws_route53_record" "custom_domain_record" {
  name = "api" # The subdomain (api.sumeet.life)
  type = "CNAME"
  ttl = "300" # TTL in seconds

  records = ["${aws_api_gateway_rest_api.example_api.id}.execute-api.${var.myregion}.amazonaws.com"]

  zone_id = data.aws_route53_zone.my_domain.zone_id
}