# Part 15 · Software Delivery & Version Control · TOPIC LIST

Rules and directives for this part: `index/part15_software_delivery.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Software Delivery & Version Control

### Git

- **Everyday Git**
  - Commits, branches, merges, rebases and tags
  - Conflict resolution
  - Remotes, pushing and pulling; pull requests
- **Git's data model**
  - Content-addressed objects: blobs, trees, commits, tags
  - The commit graph as a DAG and a Merkle structure: one hash authenticates the whole history
  - Refs and branches as pointers
  - Three-way merge against the merge base (a lowest common ancestor)
  - Rebase as replay that creates new commits
  - Object IDs as SHA-1 hashes (with a SHA-256 object format); zlib-compressed loose objects and delta-compressed packfiles; the index (staging area)
- **The Git command line**
  - Setup and inspection: `git config --global`, `git init`, `git clone`, `git status`, `git log --oneline --graph --all`, `git show`, `git diff` and `git diff --staged`, `git blame`
  - Recording: `git add -p`, `git commit --amend`, `git restore` and `git restore --staged`, `git rm`, `git mv`, `.gitignore`
  - Branching: `git switch -c`, `git branch -d`, `git merge --no-ff`, `git rebase` and `git rebase --onto`, `git cherry-pick`, `git revert`, `git reset --soft`, `--mixed` and `--hard`, `git stash push` and `pop`
  - Remotes: `git remote -v`, `git fetch --prune`, `git pull --rebase`, `git push -u`, `git push --force-with-lease` instead of `--force`, `git tag -a` and pushing tags
  - Recovery and search: `git reflog`, `git bisect start`, `good`, `bad` and `run`, `git grep`, `git worktree add`
  - Plumbing: `git hash-object -w`, `git cat-file -t` and `-p`, `git ls-tree`, `git update-index`, `git write-tree`, `git commit-tree`, `git update-ref`, `git rev-parse`, `git merge-base`

### Delivery models

- SDLC models; Agile and Scrum basics
- Trunk-based development versus GitFlow
- Code-review culture and the evidence on review; engineering practices at scale: review norms, and design docs written before a large change and reviewed by the people who depend on it
- Reading and writing code as cognition: working-memory limits when reading unfamiliar code; comprehension by tracing data and control flow rather than line by line; names, structure and comments as the reader's aids
- Small batches read as queueing: smaller batches wait less
- The four DORA metrics: deployment frequency, lead time for changes, change failure rate, time to restore service

### The profession

- The ACM Code of Ethics and Professional Conduct
- Permissive versus copyleft licences and why a dependency's licence matters
- Responsibility for privacy in system design

### Exercises

- From scratch: a mini Git storing blobs, trees and commits as zlib-compressed, SHA-1-addressed objects, with `log`, refs and a merge-base finder
- A commit reconstructed by hand with plumbing commands, then checked with `git cat-file`
- A three-way merge conflict resolved and its merge base explained
- The four DORA metrics measured for a small project
- **Reasoning drills**
  - Predict merge and rebase outcomes on a commit graph before running them
  - Reason about batch size and lead time with Little's law
  - Recover from a mistaken hard reset using only the reflog, predicting each step first
