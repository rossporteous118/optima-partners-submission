# Optima Partners Engineering Interview Assignments

Welcome to the Optima Partners Engineering interview assignment repository! Here you will find the assignment that you have been asked to complete as part of the interview process.

## Contents

[Completing Assignments](#completing-assignments)<br>
[Forking the Repo](#forking-the-repo)<br>
[Submissions](#submissions)

## Completing Assignments

Before attempting to complete the assignment you must first [fork this repository](#forking-the-repo) to your personal account in your preferred version control system. GitHub is the easiest to use for these assignments but it is possible to use another VCS.

Ensure you commit and push often so that we can have visibilty of your development process.

You will find detailed instructions for your assignment in its dedicated README.md file.

### Forking the Repo

- Go to your VCS account and create a new repository (its better to have an empty repo)

```sh
git clone <clone_path>
cd <repo_name>
```

- Now add Github repo as a new remote in your VCS called "sync"

```sh
git remote add sync ===<ADD_GITHUB_URL_HERE>===
```

- Verify what are the remotes currently has been setup for your repo. This following command should show "fetch" and "push" for two remotes i.e. "origin" and "sync"

```sh
git remote -v
```

- First pull from GitHub using the "sync" remote

```sh
git pull sync
```

- Setup local "optima" branch to track "sync" remote's "main" branch

```sh
git branch --track optima sync/main
```

- Push local "main" branch to "origin" remote VCS

```sh
git push -u origin main
```

## Submissions

Assignment submissions must be delivered to Optima Partners as a Pull Request into the original repository.

The branch nameing convention for your PR should be as follows:<br>
`submission/assignment_name/firstname_lastname_dayOfMonth`

E.g.<br>

- If the assignments directory name is `api_assignment`.
- Your fist name is `Joe`.
- Your last name is `Blogs`.
- It is the 16th of the month. the branch name should be:<br>
  `submission/api_assignment/Joe_Blogs_16`

As part of the Pull Request submission, you will be asked to:

- Fill out a brief description of your solution:
  - What question it answers.
  - What requirements your solution has achieved.

Your submission will be marked against the requirements that the Pull Request says have been met. Any supporting documentation that is provided will also be taken into account.
