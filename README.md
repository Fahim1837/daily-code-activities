# Daily Code Activities — Git Commit Tracker

> An open-source automation tool that turns every Git commit on your machine into a clean, organized, weekly developer journal — automatically, with zero manual effort.

Every time you commit code in **any** of your local repositories, this tool quietly captures the commit details and appends them to a neatly formatted, per-project, week-by-week Markdown log. No dashboards to update, no spreadsheets to maintain, no end-of-day "what did I even do today?" The history writes itself.

---

## Why this project exists

As developers we ship work constantly across many repositories, but that effort is scattered across dozens of `git log` histories and is almost impossible to see at a glance. This tool solves that by building a **single, chronological, human-readable record of everything you build** — perfect for:

- 📈 **Tracking productivity** — see exactly what you worked on, day by day and week by week.
- 📝 **Standups & status reports** — your weekly log is your standup notes, already written.
- 🧾 **Performance reviews & portfolios** — concrete, timestamped evidence of consistent output.
- 🔥 **Building a coding habit** — a visible, growing streak keeps you accountable.
- 🗂️ **Cross-project visibility** — one place to see activity across every repo you touch.

---

## What it does

The tool hooks into Git's commit lifecycle. The moment a commit lands in a tracked repository, it:

1. **Captures** the commit metadata — commit hash, message, description, branch, project name, and the hosting platform (GitHub, GitLab, Bitbucket, AWS CodeCommit, or self-hosted).
2. **Organizes** that data into a per-project folder, split into weekly files (`week-1.md`, `week-2.md`, …) with the week derived automatically from the date.
3. **Renders** the entry into styled Markdown using reusable templates — including the branch name, a platform icon, and a precise date/time stamp.
4. **Appends** the new entry to the correct weekly file (creating the file and its header the first time a new week begins).
5. **Commits and pushes** the updated journal to your activity repository — fully hands-off.

The result is a self-maintaining journal like this:

```markdown
# Week-18
## 03 - 09 May, 2025
────────────────────── o ──────────────────────

  🌿 evidence-2                          aws  06 May, 2025 | 02:59 PM

Commit: 5d23bbb
Message: Pagination added in the app
Description:
- Pagination added in the app
```

*(Rendered with inline HTML for centered headings, branch/platform icons, and color accents when viewed on GitHub or any Markdown viewer.)*

---

## How it works

```
   git commit
       │
       ▼
┌──────────────────────┐
│  post-commit hook    │   (installed in each tracked repo's .git/hooks)
└──────────┬───────────┘
           │ triggers
           ▼
┌──────────────────────┐
│ git_activity_track.sh│   1. Collects commit metadata via `git` commands
│      (Bash)          │   2. Detects the remote platform
└──────────┬───────────┘   3. Calls the Python script with the data
           │
           ▼
┌──────────────────────┐
│  create_file.py      │   4. Computes the week number & date range
│   (Python + Jinja2)  │   5. Renders the Markdown via templates/
└──────────┬───────────┘   6. Appends the entry to <project>/week-N.md
           │
           ▼
┌──────────────────────┐
│ back to the shell    │   7. Commits & pushes the updated journal
│  git_activity_track.sh│      to the activity repository
└──────────────────────┘
```

### The pieces

| File | Role |
|------|------|
| [`git_activity_track.sh`](git_activity_track.sh) | Entry point. Gathers commit data, detects the Git host, calls the Python script, then commits & pushes the journal. |
| [`scripts/create_file.py`](scripts/create_file.py) | Computes the week number and date range, picks the right template, and writes the entry into the correct per-project weekly file. |
| [`templates/new_file_template.md`](templates/new_file_template.md) | Header rendered once per week (week number + date range). |
| [`templates/existing_file_template.md`](templates/existing_file_template.md) | The per-commit entry block (branch, platform icon, timestamp, commit details). |
| [`assets/`](assets/) | SVG icons for GitHub, AWS, and the branch marker used in the rendered logs. |

---

## Tech stack

- **Bash** — Git introspection, host detection, and orchestration.
- **Python 3** — week/date calculation and file handling.
- **Jinja2** — template-driven Markdown rendering.
- **Git hooks** — `post-commit` automation trigger.

---

## Getting started

### Prerequisites

- Python 3.11+
- Git
- A repository to store your activity log (this one)

### 1. Clone and set up the environment

```bash
git clone <your-fork-url> daily-code-activities
cd daily-code-activities

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Point the script at your machine

In [`git_activity_track.sh`](git_activity_track.sh), make sure the path to this project (used to activate the virtualenv and run the Python script) matches where you cloned it.

### 3. Install the post-commit hook in each repo you want to track

For every project you'd like logged, add a `post-commit` hook that triggers the tracker:

```bash
# In <your-project>/.git/hooks/post-commit
#!/bin/sh
bash /absolute/path/to/daily-code-activities/git_activity_track.sh
```

Then make it executable:

```bash
chmod +x .git/hooks/post-commit
```

### 4. Commit as usual

That's it. From now on, every commit in that repository is automatically captured, formatted, and pushed to your activity journal — no extra steps.

---

## Project structure

```
daily-code-activities/
├── git_activity_track.sh        # Orchestrator (Bash)
├── scripts/
│   └── create_file.py           # Markdown generator (Python + Jinja2)
├── templates/
│   ├── new_file_template.md     # Weekly header template
│   └── existing_file_template.md# Per-commit entry template
├── assets/                      # Platform & branch icons (SVG)
├── requirements.txt
└── <project-name>/              # Auto-generated per-project logs
    ├── week-1.md
    ├── week-2.md
    └── ...
```

---

## Roadmap ideas

- Support for more Git hosts and custom platform icons
- A summary/dashboard view aggregating activity across all projects
- Configurable week start day and timezone
- Optional daily/weekly digest generation

---

## Contributing

This is an open-source project — issues, ideas, and pull requests are welcome. Fork it, adapt the templates to your taste, and make your commit history work for you.

## License

Open source — free to use, modify, and share.
