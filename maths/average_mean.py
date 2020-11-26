"""Find mean of a list of numbers."""


def average(nums):
    """Find mean of a list of numbers."""
    return sum(nums) / len(nums)


def test_average():
    """
    >>> test_average()
    """
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21])
    assert 20 == average([5, 10, 15, 20, 25, 30, 35])
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == "__main__":
    """Call average module to find mean of a specific list of numbers."""
    print(average([2, 4, 6, 8, 20, 50, 70]))

    
    Run isort --profile black . on the entire repo and add that command to our Autoblack GitHub Action.

--recursive was removed from isort in v5.0 https://timothycrosley.github.io/isort/CHANGELOG

Checklist:

  I have read CONTRIBUTING.md.
  This pull request is all my own work -- I have not plagiarized.
  I know that pull requests will not be merged if they fail the automated tests.
  This PR only changes one algorithm file. To ease review, please open separate PRs for separate algorithms.
  All new Python files are placed inside an existing directory.
  All filenames are in all lowercase characters with no spaces or dashes.
  All functions and variable names follow Python naming conventions.
  All function parameters and return values are annotated with Python type hints.
  All functions have doctests that pass the automated testing.
  All new algorithms have a URL in its comments that points to Wikipedia or other similar explanation.
  If this pull request resolves one or more open issues then the commit message contains Fixes: #{$ISSUE_NO}.
