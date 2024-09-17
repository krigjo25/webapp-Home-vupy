import pytest
from core import GithubApi

def test_connection()-> None:
    """Testing  the connection to the request
        Github : https://api.github.com/user/"""

    actual = GithubApi().ApiCall(endpoint = GithubApi().API_URL, header = GithubApi().head)
    expected = {
                'login': f'krigjo25', 
                'id': actual['id'],
                'node_id': actual['node_id'], 
                'avatar_url': 'https://avatars.githubusercontent.com/u/73070534?v=4',
                'gravatar_id': '',
                'url': 'https://api.github.com/users/krigjo25',
                'html_url': 'https://github.com/krigjo25',
                'followers_url': 'https://api.github.com/users/krigjo25/followers',
                'following_url': 'https://api.github.com/users/krigjo25/following{/other_user}',
                'gists_url': 'https://api.github.com/users/krigjo25/gists{/gist_id}',
                'starred_url': 'https://api.github.com/users/krigjo25/starred{/owner}{/repo}',
                'subscriptions_url': 'https://api.github.com/users/krigjo25/subscriptions',
                'organizations_url': 'https://api.github.com/users/krigjo25/orgs',
                'repos_url': 'https://api.github.com/users/krigjo25/repos',
                'events_url': 'https://api.github.com/users/krigjo25/events{/privacy}',
                'received_events_url': 'https://api.github.com/users/krigjo25/received_events',
                'type': 'User', 
                'site_admin': False,
                'name': 'Kristoffer Gjøsund',
                'company': None,
                'blog': 'https://krigjo25.github.io/Front-end/',
                'location': 'Indre-Østfold, Østfold, Norway',
                'email': None, 'hireable': True,
                'bio': {actual['bio']},
                'twitter_username': None,
                'notification_email': None,
                'public_repos': actual['public_repos'],
                'public_gists': actual['public_gists'],
                'followers': 0,
                'following': actual['following'],
                'created_at': '2020-10-18T15:26:00Z', 
                'updated_at': '2024-08-13T20:44:57Z'}
    
    
    
    #   Testing the connection response
    assert expected == actual
