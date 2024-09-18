import pytest
from core import GithubApi
def test_connection()-> None:
    """Testing  the connection to the request
        Github : https://api.github.com/user/"""

    api = GithubApi(URL="https://api.github.com/user")
    
    actual = api.ApiCall(endpoint = api.API_URL, header = api.head)

    expected = {
                'login': f'krigjo25', 'id': actual['id'], 'node_id': actual['node_id'], 
                'avatar_url': actual['avatar_url'], 'gravatar_id': actual['gravatar_id'], 'url': actual['url'],
                'html_url': actual['html_url'], 'followers_url': actual['followers_url'], 'following_url': actual['following_url'],
                'gists_url': actual['gists_url'], 'starred_url': actual['starred_url'], 'subscriptions_url': actual['subscriptions_url'],
                'organizations_url': actual['organizations_url'], 'repos_url': actual['repos_url'], 'events_url': actual['events_url'],
                'received_events_url': actual['received_events_url'], 'type': actual['type'], 
                'site_admin': actual['site_admin'],
                'name': actual['name'], 'company': actual['company'], 'blog': actual['blog'],
                'location': actual['location'], 'email': actual['email'], 'hireable':actual['hireable'],
                'bio': actual['bio'], 'twitter_username': actual['twitter_username'], 'notification_email': actual['notification_email'],
                'public_repos': actual['public_repos'],'public_gists': actual['public_gists'], 'followers': actual['followers'],
                'following': actual['following'], 'created_at': actual['created_at'], 'updated_at': actual['updated_at']}
    #   Testing the connection response
    assert expected == actual
