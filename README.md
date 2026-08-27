# se-demo

[![CI](https://github.com/tylerhanks/se-demo/actions/workflows/ci.yaml/badge.svg)](https://github.com/tylerhanks/se-demo/actions/workflows/ci.yaml)

A demo repo for CSE2410 (Intro to Software Engineering) projects at Florida Tech. This README covers how to set up a new repo with best practices for your group projects.

## How to set up project board

1. From the top bar of the Github repo, navigate to Projects -> create new project
2. Select the kanban option, give your project a name, and accept the default import options
3. Any existing issues for the repo will be automatically imported into the backlog
4. You can edit WIP limits using the three dots at the top of each column
5. Customize columns and WIP limits to your team's desires

## How to set up branch protection

1. From the top bar of the Github repo, navigate to Settings -> Branches
2. Click "Add classic branch protection rule"
3. Set the branch name pattern to `main`
4. Check "Require a pull request before merging"
5. If you are still setting up the repo, I recommend not setting an approval requirement. After the repo is set up and your team is ready to start developing, edit the rule to set the required approvals to at least 1.

## How to set up Automated Testing/Continuous Integration

1. From the repo root, create a folder `.github/workflows/`
2. In `.github/workflows/`, make a file `ci.yaml`
3. At the top of `ci.yaml`, paste the snippet:
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    name: <name_of_test>
    runs-on: ubuntu-latest

  steps:
    # TODO
```
4. Replace `<name_of_test>` with a name related to the type of test suite you are running. For example, this repo uses `pytest` so `<name_of_test>=pytest`.
5. Research the steps needed to execute your testing workflow using Github actions. Googling "Github actions for <your-project-language-or-testing-framework> testing" is a good place to start. Paste the necessary steps into the `# TODO` block above. This repo contains an example for Python with `pytest`.
6. Test if CI is working by pushing a new branch and seeing if your tests run.

## How to require passing tests before merge

1. Ensure your automated CI tests are working and you have set up branch protection
2. Navigate back to your branch protection rule, click the three dots, and click edit
3. Check "Require status checks to pass before merging"
4. Search `<name_of_test>` from step 4. above in the search bar and select the result
5. Click "save changes" at the bottom of the page
6. Now verify by opening a PR with failing tests; you should not be allowed to merge until the tests pass
