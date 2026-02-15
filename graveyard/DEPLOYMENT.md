# GitHub Pages Deployment

Your portfolio is now pushed to GitHub! Here's how to enable GitHub Pages:

## Steps to Go Live

1. **Go to Repository Settings**
   - Navigate to: https://github.com/amirsolobass/sitegen
   - Click "Settings" (top right)

2. **Configure GitHub Pages**
   - In left sidebar, click "Pages" under "Code and automation"
   - Under "Build and deployment":
     - Source: Select "Deploy from a branch"
     - Branch: Select "main"
     - Folder: Select "/docs"
     - Click "Save"

3. **Wait for Build**
   - GitHub will build and deploy your site
   - This usually takes 1-2 minutes

## Your Live URLs

Once deployed, your portfolio will be live at:

- **Main Portfolio**: https://amirsolobass.github.io/sitegen/main_index.html
- **Projects Hub**: https://amirsolobass.github.io/sitegen/projects/
- **BookBot**: https://amirsolobass.github.io/sitegen/projects/bookbot/
- **AI Agent**: https://amirsolobass.github.io/sitegen/projects/aiagent/
- **ChordToNote**: https://amirsolobass.github.io/sitegen/projects/chordtonote/

## What Was Deployed

The `/docs` folder contains the complete static website with:
- All project pages with installation and usage instructions
- Responsive HTML generated from your markdown files
- Styled with custom CSS from `static/index.css`
- Ready to serve directly from GitHub Pages

## Future Updates

To make changes:
1. Edit markdown files in `content/` directory
2. Run `python3 src/main.py` to regenerate HTML in `/docs`
3. Commit and push to GitHub
4. GitHub Pages will automatically update within minutes
