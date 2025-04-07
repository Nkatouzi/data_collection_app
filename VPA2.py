from flask import Flask, request

app = Flask(__name__)

# The instructions HTML we'll show on the main page
INSTRUCTIONS_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Video Player Application111</title>
</head>
<body>
    <h1>Video Player Application.</h1>
    <p>
        Rename the video file to "hand_video".<br><br>
        Press the 'Start' button to begin playback.
    </p>

    <form action="/start" method="POST">
        <button type="submit">Start</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    # Show the instructions page with a "Start" button
    return INSTRUCTIONS_HTML

@app.route("/start", methods=["POST"])
def start():
    # When the user presses the "Start" button, we return "I LOVE YOU"
    return "I LOVE YOU Farshid"

if __name__ == "__main__":
    app.run(debug=True)