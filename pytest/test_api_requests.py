import pytest
from core import GithubApi
class TestAPI:
    def test_connection(self)-> None:
        """Testing  the connection to the request
            Github : https://api.github.com/user/"""

        api = GithubApi()
        
        actual = api.ApiCall(endpoint = f"{api.API_URL}user", head = api.head)

        expected = {
                    'login': f'krigjo25', 'id': actual['id'], 'node_id': actual['node_id'], 
                    'avatar_url': actual['avatar_url'], 'gravatar_id': actual['gravatar_id'], 'url': actual['url'],
                    'html_url': actual['html_url'], 'followers_url': actual['followers_url'], 'following_url': actual['following_url'],
                    'gists_url': actual['gists_url'], 'starred_url': actual['starred_url'], 'subscriptions_url': actual['subscriptions_url'],
                    'organizations_url': actual['organizations_url'], 'repos_url': actual['repos_url'], 'events_url': actual['events_url'],
                    'received_events_url': actual['received_events_url'], 'type': actual['type'], 
                    'site_admin': actual['site_admin'], 'name': actual['name'], 'company': actual['company'],
                    'blog': actual['blog'], 'location': actual['location'], 'email': actual['email'],
                    'hireable':actual['hireable'], 'bio': actual['bio'], 'twitter_username': actual['twitter_username'],
                    'notification_email': actual['notification_email'], 'public_repos': actual['public_repos'],
                    'public_gists': actual['public_gists'], 'followers': actual['followers'],
                    'following': actual['following'], 'created_at': actual['created_at'], 'updated_at': actual['updated_at']}
        #   Testing the connection response
        assert expected == actual

    def test_fetch_repos(self)-> None:
        """Testing  fetch_repos
            Github api : https://api.github.com/user/repos"""

        #   Initializing Requests module
        api = GithubApi()

        #   Our actual response from the Api Call
        actual = api.ApiCall(endpoint = f"{api.API_URL}user/repos", head = api.head)

        for i in range(len(actual)):

            #
            expected =  {
                            "id": actual[i]['id'], "node_id": actual[i]['node_id'], "name": actual[i]['name'], "full_name": actual[i]['full_name'],
                            "owner": { 
                                "login": actual[i]['owner']['login'], "id": actual[i]['owner']['id'], 
                                "node_id": actual[i]['owner']['node_id'], "avatar_url": actual[i]['owner']['avatar_url'], 
                                "gravatar_id": actual[i]['owner']['gravatar_id'],"url": actual[i]['owner']['url'],
                                "html_url": actual[i]['owner']['html_url'], "followers_url": actual[i]['owner']['followers_url'],
                                "following_url": actual[i]['owner']['following_url'], "gists_url": actual[i]['owner']['gists_url'], 
                                "starred_url": actual[i]['owner']['starred_url'], "subscriptions_url": actual[i]['owner']['subscriptions_url'], 
                                "organizations_url": actual[i]['owner']['organizations_url'], "repos_url": actual[i]['owner']['repos_url'], 
                                "events_url": actual[i]['owner']['events_url'], "received_events_url": actual[i]['owner']['received_events_url'], 
                                "type": actual[i]['owner']['type'], "site_admin": actual[i]['owner']['site_admin']},
                            
                            "private": actual[i]['private'], "html_url": actual[i]['html_url'], 
                            "description": actual[i]['description'], "fork": actual[i]['fork'], 
                            "url": actual[i]['url'], "archive_url": actual[i]['archive_url'],
                            "assignees_url": actual[i]['assignees_url'], "blobs_url": actual[i]['blobs_url'],
                            "branches_url": actual[i]['branches_url'], "collaborators_url": actual[i]['collaborators_url'], 
                            "comments_url": actual[i]['comments_url'],  "commits_url": actual[i]['commits_url'],
                            "compare_url": actual[i]['compare_url'], "contents_url": actual[i]['contents_url'], 
                            "contributors_url": actual[i]['contributors_url'], "deployments_url": actual[i]['deployments_url'],
                            "downloads_url": actual[i]['downloads_url'], "events_url": actual[i]['events_url'],
                            "forks_url": actual[i]['forks_url'], "git_commits_url": actual[i]['git_commits_url'],
                            "git_refs_url": actual[i]['git_refs_url'], "git_tags_url": actual[i]['git_tags_url'], 
                            "git_url": actual[i]['git_url'], 'has_discussions': actual[i]['has_discussions'],
                            "issue_comment_url": actual[i]['issue_comment_url'], "issue_events_url": actual[i]['issue_events_url'],
                            "issues_url": actual[i]['issues_url'], "keys_url": actual[i]['keys_url'],
                            "labels_url": actual[i]['labels_url'],"languages_url": actual[i]['languages_url'],
                            "merges_url": actual[i]['merges_url'], "milestones_url": actual[i]['milestones_url'],
                            "notifications_url": actual[i]['notifications_url'], "pulls_url": actual[i]['pulls_url'],
                            "releases_url": actual[i]['releases_url'], "ssh_url": actual[i]['ssh_url'],
                            "stargazers_url": actual[i]['stargazers_url'], "statuses_url": actual[i]['statuses_url'],
                            "subscribers_url": actual[i]['subscribers_url'], "subscription_url": actual[i]['subscription_url'],
                            "tags_url": actual[i]['tags_url'], "teams_url": actual[i]['teams_url'],
                            "trees_url": actual[i]['trees_url'], "clone_url": actual[i]['clone_url'],
                            "mirror_url": actual[i]['mirror_url'], "hooks_url": actual[i]['hooks_url'],
                            "svn_url": actual[i]['svn_url'], "homepage": actual[i]['homepage'],
                            "license": actual[i]['license'], "language": actual[i]['language'], 
                            "forks_count": actual[i]['forks_count'], "forks": actual[i]['forks'],
                            "stargazers_count": actual[i]['stargazers_count'], "watchers_count": actual[i]['watchers_count'],
                            "watchers": actual[i]['watchers'], "size": actual[i]['size'],
                            "default_branch": actual[i]['default_branch'], "open_issues_count": actual[i]['open_issues_count'],
                            "open_issues": actual[i]['open_issues'], "is_template": actual[i]['is_template'],
                            "topics": [ i for i in actual[i]['topics']], "has_issues": actual[i]['has_issues'],
                            "has_projects": actual[i]['has_projects'], "has_wiki": actual[i]['has_wiki'],
                            "has_pages": actual[i]['has_pages'], "has_downloads": actual[i]['has_downloads'],
                            "archived": actual[i]['archived'], "disabled": actual[i]['disabled'],
                            "visibility": actual[i]['visibility'], "pushed_at": actual[i]['pushed_at'],
                            "created_at": actual[i]['created_at'], "updated_at": actual[i]['updated_at'],
                            'web_commit_signoff_required': actual[i]['web_commit_signoff_required'], 'allow_forking':actual[i]['allow_forking'],
                            "permissions": {
                                "pull": actual[i]['permissions']['pull'], "push": actual[i]['permissions']['push'],
                                "admin": actual[i]['permissions']['admin'], 'maintain':actual[i]['permissions']['maintain'],
                                'triage':actual[i]['permissions']['triage']}
                        }
        assert actual[i] == expected
        return