from .base import OAuth2Login


class LinkedInLogin(OAuth2Login):
    

    config_prefix = "LINKEDIN_LOGIN_"
    
    redirect_endpoint = "_linkedin_login"
    state_session_key = "_linkedin_login_state"

    default_scope = (
    "r_liteprofile,"
    "r_emailaddress,"
    "w_member_social"
  )
    default_redirect_path = "/login/linkedin"
    auth_url = "https://www.linkedin.com/oauth/v2/authorization"
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    profile_url = "https://api.linkedin.com/v2/me?"