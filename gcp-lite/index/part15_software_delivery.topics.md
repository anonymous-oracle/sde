# Part 15 · Software Delivery & Version Control · TOPIC LIST

Rules and directives for this part: `index/part15_software_delivery.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Software Delivery & Version Control

### Git

- **Everyday Git**
  - Commits, branches, merges, rebases and tags; a commit is an immutable snapshot with parent pointers, a branch is a movable name for one commit, a merge joins two histories in a commit with two parents, a rebase replays commits onto a new base, and a lightweight tag is a plain ref while an annotated tag is a named object with its own message and author
  - Conflict resolution: a conflict arises when both sides change the same region of a file differently; git writes markers (`<<<<<<<`, `=======`, `>>>>>>>`) into the file and lists the path as unmerged in `git status`; the resolver edits the file to the intended result, stages it with `git add`, and commits; `git merge --abort` returns to the state before the merge; a merge with no textual conflict can still be wrong, so the result needs tests
  - Remotes, pushing and pulling; pull requests; SSH remote URLs (`git@host:owner/repo.git`) authenticated by a key pair whose public half the host trusts, checked with a read-only authentication test before the first push; HTTPS remotes authenticated by a token instead
- **Git's data model**
  - Content-addressed objects: blobs, trees, commits, tags; a blob holds one file's content with no name; a tree maps names and modes to blob and tree IDs, so it is one directory level; a commit names one root tree, its parent commits, its author and its message; an annotated tag names another object and carries a message; each object's ID is the SHA-1 hash of its type, size and content, so identical content is stored once
  - The commit graph as a DAG and a Merkle structure: one hash authenticates the whole history
  - Refs and branches as pointers: a ref is a name holding one object ID, stored as a small file under refs or in packed-refs; a branch is a ref under refs/heads, and HEAD is a symbolic ref naming the current branch; creating a branch writes one new pointer, and moving a branch moves only that pointer, so the old commits stay reachable while any ref or reflog entry reaches them
  - Three-way merge against the merge base (a lowest common ancestor)
  - Rebase as replay that creates new commits; git takes the commits reachable from the branch but not from the new base, moves the branch to the base, and reapplies each commit in order; each replayed commit gets a new hash because its parent changed, and the originals are left behind; rebasing history that others have already fetched forces them to reconcile two copies, so rewrite only local commits
  - Object IDs as SHA-1 hashes (with a SHA-256 object format); zlib-compressed loose objects and delta-compressed packfiles; the index (staging area)
- **The Git command line**
  - Setup and inspection: `git config --global`, `git init`, `git clone`, `git status`, `git log --oneline --graph --all`, `git show`, `git diff` and `git diff --staged`, `git blame`
  - Recording: `git add -p`, `git commit --amend`, `git restore` and `git restore --staged`, `git rm`, `git mv`, `.gitignore`
  - Branching: `git switch -c`, `git branch -d`, `git merge --no-ff`, `git rebase` and `git rebase --onto`, `git cherry-pick`, `git revert`, `git reset --soft`, `--mixed` and `--hard`, `git stash push` and `pop`
  - Remotes: `git remote -v`, `git fetch --prune`, `git pull --rebase`, `git push -u`, `git push --force-with-lease` instead of `--force`, `git tag -a` and pushing tags
  - Recovery and search: `git reflog`, `git bisect start`, `good`, `bad` and `run`, `git grep`, `git worktree add`
  - Plumbing: `git hash-object -w`, `git cat-file -t` and `-p`, `git ls-tree`, `git update-index`, `git write-tree`, `git commit-tree`, `git update-ref`, `git rev-parse`, `git merge-base`

### Delivery models

- SDLC models; Agile and Scrum basics; the software development life cycle models include waterfall (phases in sequence, each finished before the next), iterative and incremental (working increments built and reviewed in cycles), spiral (cycles driven by risk) and the V-model (each design phase paired with a test phase); Agile values working software, collaboration and response to change; Scrum has three roles (product owner, Scrum Master, developers), time-boxed sprints with planning, a daily scrum, a review and a retrospective, and three artifacts: the product backlog, the sprint backlog and the increment
- Trunk-based development versus GitFlow: trunk-based development keeps one main line into which developers merge short-lived branches at least daily, hiding unfinished work behind feature flags so integration problems surface early; GitFlow keeps long-lived develop, feature, release and hotfix branches, which isolates releases at the cost of longer merges and later integration; the DORA research associated trunk-based development with higher delivery performance, while GitFlow suits software shipped as numbered releases that users install
- Code-review culture and the evidence on review; engineering practices at scale: review norms, and design docs written before a large change and reviewed by the people who depend on it; the test pyramid: many fast unit tests, fewer integration tests and a few end-to-end tests, with CI running the fast layers on every change
- Reading and writing code as cognition: working-memory limits when reading unfamiliar code; comprehension by tracing data and control flow rather than line by line; names, structure and comments as the reader's aids
- Small batches read as queueing: smaller batches wait less; Little's law (work in the system equals arrival rate times average time in the system) shows that at a fixed flow rate, a smaller batch means less work waiting and a shorter time for each change to reach users; a small batch pays a fixed overhead per release (setup, testing, deployment), so the best batch size balances that overhead against the waiting it saves
- The four DORA metrics: deployment frequency, lead time for changes, change failure rate, time to restore service

### The profession

- The ACM Code of Ethics and Professional Conduct: the 2018 code sets general principles to contribute to society and human well-being, avoid harm, be honest and trustworthy, be fair and take action not to discriminate, respect the work needed to produce new ideas, respect privacy and honour confidentiality; it is applied by reasoning through cases where principles conflict, since the principles are not ranked by a formula
- Permissive versus copyleft licences and why a dependency's licence matters; dataset licences reviewed with the same checklist as software: data under an open licence with attribution or share-alike terms, data with no stated licence (no permission to reuse by default), and the terms on model weights and training data
- Responsibility for privacy in system design: collect only the data a stated purpose needs (data minimisation), keep it only as long as that purpose requires (retention limits), restrict access by role, pseudonymise identifiers where full anonymisation cannot be achieved, and make the privacy-protective setting the default rather than an opt-in afterthought (privacy by design); a privacy review belongs in the design document, beside the security review

### Exercises

- From scratch: a mini Git storing blobs, trees and commits as zlib-compressed, SHA-1-addressed objects, with `log`, refs and a merge-base finder
- A commit reconstructed by hand with plumbing commands, then checked with `git cat-file`
- A three-way merge conflict resolved and its merge base explained
- The four DORA metrics measured for a small project
- **Reasoning drills**
  - Predict merge and rebase outcomes on a commit graph before running them
  - Reason about batch size and lead time with Little's law
  - Recover from a mistaken hard reset using only the reflog, predicting each step first
