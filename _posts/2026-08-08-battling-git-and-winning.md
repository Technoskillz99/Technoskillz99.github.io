---
title: Battling Git, Tokens, and Winning My First Green Squares
date: 2026-08-08 17:00:00 +0100
categories: [Journey, Engineering]
tags: [git, github, workflow, python]
---

Today, I hit a massive wall in my computer science journey, and it had nothing to do with Python or machine learning. It was **Git**.

When you're building a project from scratch, people always talk about the code, but nobody warns you about the:

- Untracked files sitting locally on your laptop.
- The dreaded `fatal: not a git repository` error.
- GitHub's strict rule against using account passwords in the terminal, forcing you to generate and configure Personal Access Tokens (PATs).

### The Struggle

For weeks, I had been writing Python scripts (`tic-tac-toe.py`, squad managers, and Pandas practice) locally on my machine without committing them. My GitHub contribution graph looked like a ghost town for August. When I finally tried to push everything, my terminal threw authentication errors and blocked my pushes.

### The Fix

After wrestling with tokens and git pushes, it finally worked:

1. **Separate your concerns:** Keep your code workspace (`cs-journey`) - this is where I put my codes - completely separate from your static site generator (`Technoskillz99.github.io`)- This is my blog folder.
2. **Master the 3-step rhythm:** `git add .` -> `git commit -m "..."` -> `git push`.
3. **Persist:** Every error message is just a puzzle piece. Most important part is that you don't give up until it's done

Seeing that bright green contribution square pop up on my profile today made all the terminal headaches worth it. Back to Pandas and Premier League data tomorrow!
