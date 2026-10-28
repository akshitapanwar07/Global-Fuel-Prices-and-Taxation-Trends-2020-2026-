# Global Fuel Analytics — Flask App

A small Python Flask app that serves the Global Fuel Analytics website and embeds the published Tableau Public dashboard and story.

## Run locally in VS Code

1. Open this folder in VS Code.
2. Open Terminal → New Terminal.
3. Create a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open the local address shown in the terminal, normally `http://127.0.0.1:5000`.

The Tableau dashboard and story need an internet connection and must remain publicly accessible on Tableau Public.

## Push to GitHub

Create an empty GitHub repository, then run these commands from this folder (replace the URL with your own repository URL):

```bash
git init
git add .
git commit -m "Create Flask Global Fuel Analytics app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Global-Fuel-Analytics.git
git push -u origin main
```

## Deployment note

GitHub Pages cannot run a Python Flask backend. To host this Flask app publicly, use a Python-compatible host such as Render or PythonAnywhere. The project can still be stored in GitHub. Do not use Flask's debug server as a production server.
