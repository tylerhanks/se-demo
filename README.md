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

1. From the repository, navigate to Settings -> Branches.
2. Click "Add classic branch protection rule."
3. Set the branch name pattern to `main`.
4. Check "Require a pull request before merging."
5. While initially setting up the repository, you may leave the required
   number of approvals at 0.
6. Once setup is complete and normal development begins:
   - require at least 1 approval;
   - check "Do not allow bypassing the above settings."

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
      - name: Check out repository
        uses: actions/checkout@v7

      # TODO: Add steps to install dependencies and run tests
```
4. Replace `<name_of_test>` with a name related to the type of test suite you are running. For example, this repo uses `pytest` so `<name_of_test>=pytest`.
5. Research the steps needed to execute your testing workflow using Github actions. Googling "Github actions for <your-project-language-or-testing-framework> testing" is a good place to start. Paste the necessary steps into the `# TODO` block above. This repo contains an example for Python with `pytest`.
6. Push a new branch, open a pull request targeting main, and verify that the CI job runs on the PR.

## How to require passing tests before merge

1. First verify that your CI workflow runs successfully on a pull request.
2. Navigate back to the branch protection rule and edit it.
3. Check "Require status checks to pass before merging."
4. Search for the name of your CI job, e.g. `pytest`, and select it.
   Use the job's `name:` value, i.e. `<name_of_test>` from step 4 above, not the workflow name `CI`.
5. Save changes.
6. Open a PR with a failing test and verify that GitHub prevents the PR
   from being merged.
7. Fix the test/code, push the change, and verify that the passing CI
   check allows the PR to be merged.
