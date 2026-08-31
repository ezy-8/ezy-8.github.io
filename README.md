# Scripts to Create Personal Website

# How to Build & Deploy This Website

Here are three methods to get this website running, depending on your technical comfort.

## Option 1: The "Just Run It" Method (VS Code)

This is the easiest way. It runs the website on your computer without any special setup.

1.  **Install VS Code:** If you don't have it, download [Visual Studio Code](https://code.visualstudio.com/).
2.  **Install the Extension:**
    *   Open VS Code.
    *   Go to the **Extensions** view (the square icon on the left sidebar, or `Ctrl+Shift+X`).
    *   Search for "Live Server".
    *   Install the one by **Ritwick Dey**.
3.  **Open the Folder:**
    *   In VS Code, go to `File > Open Folder`.
    *   Select the `ezy-8.github.io` folder.
4.  **Launch:**
    *   Right-click on `index.html` in the file explorer.
    *   Select **"Open with Live Server"**.
    *   The website will open in your browser.

## Option 2: The "Slightly Technical" Method (Python)

If you have Python installed (common on Mac/Linux, easy to add to Windows), you can run a mini-server from your terminal.

1.  Open your **Terminal** (or **PowerShell** on Windows).
2.  Navigate to the folder:
    ```bash
    cd path/to/ezy-8.github.io
    ```
3.  Run the server:
    *   **Python 3:** `python -m http.server 8000`
    *   **Python 2:** `python -m SimpleHTTPServer 8000`
4.  Open your browser and go to: `http://localhost:8000`

## Option 3: The "Professional" Method (GitHub Pages)

If you want this website to be live on the internet (like `[IP_ADDRESS]`), you need to use GitHub Pages.

1.  **Create a GitHub Account:** Go to [github.com](https://github.com) and sign up.
2.  **Create a Repository:**
    *   Click "New" to create a repository.
    *   Name it **`ezy-8.github.io`** (exactly this name).
    *   Check the box to **Add a README** (or ignore it, we will overwrite it).
3.  **Push Your Code:**
    *   If you are new to Git, you might need to install it first from [git-scm.com](https://git-scm.com).
    *   Open Terminal/PowerShell and run these commands (make sure you are in the folder):

    ```bash
    # Initialize git in your folder
    git init

    # Add all the files
    git add .

    # Commit them (save a version)
    git commit -m "Initial website commit"

    # Connect to GitHub
    git remote add origin https://github.com/your-username/ezy-8.github.io.git

    # Push the files up
    git push -u origin main 
    ```

    *(Note: If it says `main` is not defined, try `git push -u origin master`)*

4.  **View Your Site:**
    *   Go to your GitHub repository settings (usually a gear icon).
    *   Find the "Pages" section.
    *   It will show you the URL (e.g., `https://your-username.github.io`). It might take a minute to appear.

### Quick Tip for GitHub
If you already have a repository called `ezy-8.github.io`, you can skip steps 1 & 2 and just run:
```bash
git add .
git commit -m "Update website"
git push
```

---
*Note: This website uses clean HTML, CSS, and minimal JavaScript. It requires no database or backend. It will run on any modern device.*
