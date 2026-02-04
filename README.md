# Advanced Git & GitHub Assignment – Log Health Tool

A Python-based **Log Analysis & Data Health Tool** demonstrating advanced Git workflows including branch isolation, stashing, hotfixes, and controlled merging.

## 📌 Project Overview

This project implements a practical tool that:

* **Reads** application logs from CSV files
* **Analyzes** log data with multiple health checks
* **Displays** clear console summaries

The codebase demonstrates professional Git practices including feature branches, hotfixes, Git stash for task interruption, and clean merge workflows.

## 🎯 Learning Objectives

By working through this project, you will learn:

* **Branch Isolation** : How feature branches prevent changes from affecting main
* **Git Stash** : Safely save incomplete work when switching tasks
* **Hotfix Workflow** : Handle urgent fixes on main without disrupting features
* **Controlled Merging** : Integrate features cleanly with proper commit history
* **Safe Task Switching** : Professional patterns used in real software teams

## 📁 Project Structure

```
log_health_tool/
├── data/
│   └── app_logs.csv          # Sample application logs
├── src/
│   ├── loader.py             # CSV log loading module
│   └── analyzer.py           # Log analysis logic
├── README.md                 # This file
└── .gitignore                # Git ignore rules
```

## ✨ Features

### Phase 1: Base Tool Setup

* Load CSV application logs
* Display total log record count
* Proper project structure and small commits

### Phase 2: Error Logging Summary (Feature Branch)

* Count ERROR, WARNING, and INFO level logs
* Display log level distribution
* Isolated on`feature-error-summary` branch
* Main branch remains unaffected until merge

### Phase 3: Git Stash – Simulated Interruption

* Start time-based grouping feature (incomplete)
* Stash work using`git stash`
* Switch to`hotfix-log-loader` branch for urgent fixes
* Fix CSV empty file handling

### Phase 4: Stashed Work Recovery

* Apply stashed changes with`git stash apply`
* Complete time-based log grouping feature
* Merge into main with clean history
* Verify no code loss

## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* Git
* GitHub account

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/log_health_tool.git
   cd log_health_tool
   ```
2. **Create Python environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies (if any):**
   ```bash
   # No external dependencies required
   # Pure Python implementation
   ```

### Running the Tool

```bash
python src/loader.py
```

Expected output:

```
Total Log Records: 150
Log Levels: ERROR: 25, WARNING: 45, INFO: 80
Time-based Distribution: [grouped by hour/day]
```

## 📚 Git Workflow Explanation

### Why Git Stash Was Needed

In real-world development, you often face this scenario:

* You're working on a feature branch with uncommitted changes
* An urgent production bug needs fixing NOW
* You can't commit incomplete work to the feature branch
* Solution:**Git Stash** temporarily saves your work

### When Git Stash Was Applied

**Phase 3 Scenario:**

1. Working on`feature-error-summary` branch
2. Started implementing time-based log grouping (incomplete)
3. Urgent hotfix needed → Stashed changes
4. Switched to`hotfix-log-loader` branch for emergency fix
5. Fixed bug in`loader.py` for empty CSV handling
6. Returned to feature branch and restored stashed work

### Branch History

```
main                          ← Production code
├── feature-error-summary     ← Feature development
│   ├── Add error counting
│   ├── [STASHED: time grouping]
│   └── Complete time grouping (restored from stash)
└── hotfix-log-loader         ← Emergency fix
    └── Fix empty CSV handling
```

### Proof of Branch Isolation

Before merging `feature-error-summary`:

* **Main branch** ran without error-level summaries ✓
* Feature changes existed ONLY on feature branch ✓
* Main branch remained unaffected ✓

After merging:

* Main now includes all feature functionality ✓
* Clean, linear merge history ✓

## 🔧 Implementation Details

### src/loader.py

* Loads CSV application logs
* Handles empty files gracefully (hotfix)
* Returns list of log records

### src/analyzer.py

* Counts log levels (ERROR, WARNING, INFO)
* Groups logs by time periods
* Formats console output
* Produces readable summaries

## 📊 Commit History Pattern

This project demonstrates proper Git practices:

```
commit abc1234: Add project structure and base setup
commit def5678: Implement CSV loader with basic output
commit ghi9012: [feature-error-summary] Add log level counting
commit jkl3456: [hotfix-log-loader] Handle empty CSV files
commit mno7890: Merge hotfix into main
commit pqr1234: [feature-error-summary] Add time-based grouping
commit stu5678: Merge feature-error-summary into main
```

Notice:

* Small, focused commits
* Clear commit messages
* Feature work isolated on branches
* Hotfix applied separately
* Clean merges at the end

## 🧪 Testing Recommendations

### Manual Testing

1. **Test CSV Loading:**
   ```bash
   python -c "from src.loader import load_logs; print(load_logs('data/app_logs.csv'))"
   ```
2. **Test Error Analysis:**
   ```bash
   python -c "from src.analyzer import analyze; analyze('data/app_logs.csv')"
   ```

### Edge Cases to Handle

* Empty CSV files
* Missing log level column
* Malformed timestamp entries
* Very large log files

## 🔑 Key Git Commands Used

This project demonstrates these essential commands:

```bash
# Create and switch to feature branch
git checkout -b feature-error-summary

# Save incomplete work
git stash

# List stashed work
git stash list

# Apply stashed changes
git stash apply

# Create hotfix branch
git checkout -b hotfix-log-loader

# Merge branches
git merge feature-error-summary
git merge hotfix-log-loader
```

## 📖 Repository Information

* **Repository Type:** Public/Learning
* **Primary Language:** Python
* **Git Workflow:** Feature branch + Hotfix pattern
* **No External Dependencies:** Pure Python implementation

## ❓ FAQ

**Q: Why use Git Stash instead of committing incomplete work?**
A: Git Stash keeps your commit history clean. You don't want half-finished features in the log. Stash is perfect for temporary context switches.

**Q: Can the feature branch affect main if it's not merged?**
A: No. Feature branches are completely isolated. Changes exist only on that branch until you explicitly merge.

**Q: What happens if I accidentally delete stashed work?**
A: You can recover it! Git keeps stash history. Use `git stash list` to see all stashes. Dropped stashes remain in the git reflog for ~30 days.

**Q: How is the hotfix different from a feature?**
A: Hotfixes branch from main (not develop), fix critical bugs, and merge back immediately. Features are longer-running and get more thorough testing.

## 🎓 Real-World Applications

This workflow pattern is used in:

* **Agile Teams** : Sprint-based development with emergency hotfixes
* **DevOps Pipelines** : Feature branches integrate with CI/CD
* **Open Source** : PRs follow this isolated-branch pattern
* **Enterprise** : Controlled releases from main branch only

## 📝 Notes for Developers

* Keep commits small and focused
* Write meaningful commit messages
* Always test before merging
* Use descriptive branch names
* Clean up merged branches after integration

## 🤝 Contributing

This is an educational project. To extend it:

1. Create a feature branch from main
2. Implement your feature
3. Test thoroughly
4. Submit a pull request
5. Code review before merging

## 📄 License

Educational use. See specific assignment requirements for licensing details.

## 🎯 Summary

This project demonstrates professional Git workflows that prevent code conflicts, enable safe task switching, and maintain clean project history. The combination of feature branches, Git stash, and hotfix patterns reflects real-world software development practices used in companies worldwide.

Happy coding! 🚀
