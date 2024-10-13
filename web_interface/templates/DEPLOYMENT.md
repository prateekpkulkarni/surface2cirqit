# Deploying the surface2cirqit Web Interface

This document outlines the steps to deploy the surface2cirqit web interface on PythonAnywhere, a platform for hosting Python web applications.

## Prerequisites

- A PythonAnywhere account (free tier is sufficient)
- Your surface2cirqit GitHub repository

## Deployment Steps

1. **Sign up for PythonAnywhere**
   - Go to [PythonAnywhere.com](https://www.pythonanywhere.com/) and create an account.

2. **Create a new web app**
   - From your dashboard, go to the "Web" tab.
   - Click "Add a new web app".
   - Choose "Flask" as your web framework.
   - Select the Python version that matches your local development environment.

3. **Set up your code**
   - In the "Code" section of your web app configuration, you'll see your app's directory.
   - Navigate to this directory in the PythonAnywhere Files interface.
   - Upload your `app.py` file to this directory.
   - Create a `templates` folder and upload your `index.html` file into it.

4. **Install dependencies**
   - Go to the "Consoles" tab and start a new Bash console.
   - Install your surface2cirqit package and Flask:
     ```
     pip install --user surface2cirqit flask
     ```

5. **Configure the WSGI file**
   - Go back to the "Web" tab.
   - Click on the WSGI configuration file link.
   - Modify the file to look like this:
     ```python
     import sys
     path = '/home/yourusername/mysite'
     if path not in sys.path:
         sys.path.append(path)
     
     from app import app as application
     ```
   - Replace `yourusername` with your PythonAnywhere username and adjust the path if necessary.

6. **Reload your web app**
   - On the "Web" tab, click the "Reload" button for your web app.

7. **Access your web app**
   - Your web app will now be live at `yourusername.pythonanywhere.com`.

## Updating Your Application

To update your application after making changes:

1. Upload the new version of your files using the PythonAnywhere Files interface.
2. If you've added new dependencies, install them using the Bash console.
3. Go to the "Web" tab and click the "Reload" button for your web app.

## Troubleshooting

- If you encounter any errors, check the error logs in the "Web" tab.
- Ensure all necessary files are in the correct directories.
- Verify that all required packages are installed.

## Security Considerations

- Keep your PythonAnywhere account credentials secure.
- Be cautious about exposing sensitive information in your code or interface.
- Consider implementing proper input validation and error handling in your Flask application.

For more detailed information on deploying Flask applications on PythonAnywhere, refer to their [official documentation](https://help.pythonanywhere.com/pages/Flask/).
