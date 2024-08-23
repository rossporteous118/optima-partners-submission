# Optima Partners Engineering Interview Assignments

Welcome to the Optima Partners Engineering interview assignment repository! Here you will find the assignment that you have been asked to complete as part of the interview process.

## Completing Assignments

Before attempting to complete the assignment you must first fork this repository to your personal account in your preferred version control system. GitHub is the easiest to use for these assignments but it is possible to use another VCS.

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
git remove -v
```

- First pull from GitHub using the "sync" remote

```sh
git pull sync
```

- Setup local "optima" branch to track "sync" remote's "main" branch

```sh
git branch --track optima sync/main
```

- Switch to the new branch

```sh
git checkout optima
```

- Create new "main" branch branched out of "optima" branch

```sh
git checkout -b main
```

- Push local "main" branch to "origin" remote VCS

```sh
git push -u origin main
```

## Submissions

Assignment submissions must be delivered to Optima Partners as a Pull Request into the original repository. As part of the Pull Request submission, you will be asked to fill out a brief description of your solution, what question it answers and what requirements your solution has achieved. Your submission will be marked against the requirements that the Pull Request says have been met. Any supporting documentation that is provided will also be taken into account.
