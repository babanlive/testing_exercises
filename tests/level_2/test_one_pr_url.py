from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__valid_url():
    assert is_github_pull_request_url("https://github.com/babanlive/testing_exercises/pull/1")


def test__is_github_pull_request_url__invalid_url():
    assert not is_github_pull_request_url("https://github.com/babanlive/testing_exercises")

def test__is_github_pull_request_url___invalid_domain_name():
    assert not is_github_pull_request_url("https://gitlab.com/babanlive/testing_exercises/pull/1")