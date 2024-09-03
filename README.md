# assignment-backend
Backend script for My Assignments android app

## How to run?
1. Clone this repository
   ```bash
   git clone https://github.com/nanerbs25/assignment-backend
   ```
2. Open the repository
   ```bash
   cd assignment-backend
   ```
3. Run the backend
   ```bash
   gunicorn --workers 4 --bind 0.0.0.0:8000 backend3:app
   ```

## Can this backend run on a phone?
- **Yes**, since this is a python script, you can install termux and install python and some packages then run the app.
