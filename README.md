# nlpy

A unified repository for Python scripts focused on automation, server setup, and analysis.

## 🎯 Purpose
This project is designed to be a **central place for everything you build with Python scripts**:
- small tools for everyday automation
- one-off scripts for server/operations tasks
- analysis and experimentation

The goal is to keep everything clear, reusable, and easy to run.

## 📁 Project structure
```text
.
├── analyzer-domain/          # Domain analysis/crawler-related files
├── setup-server-linode.py    # Setup script for Linode server
├── sub-apt-get-v1.py         # Simple apt-get update/upgrade installer
└── README.md
```

## 🚀 Getting started
1. Clone the repository:
   ```bash
   git clone https://github.com/networkluki/nlpy.git
   cd nlpy
   ```
2. (Recommended) Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Run a script:
   ```bash
   python3 setup-server-linode.py
   ```

## ✅ Keep it professional
- Use clear file names with verbs (`setup-...`, `analyze-...`, `sync-...`).
- Give each script a short header with purpose, input/output, and an example.
- Avoid hardcoded secrets (API keys, passwords).
- Add error handling and clear error messages.
- Document new scripts in this README file.

## 🤝 Contributing
Want to add a script? Please follow this flow:
1. Create the script with a clear name.
2. Add a short description in the README.
3. Test the script locally before committing.

## 📜 License
No license specified yet.
