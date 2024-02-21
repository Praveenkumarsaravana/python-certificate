from flask import Flask, render_template, request

app = Flask(__name__)

# Certificate details mapping
CERTIFICATE_DETAILS = {
    (1, 90): {"image": "images/perfect.jpg", "name": "Perfect"},
    (1, 80): {"image": "images/super.jpg", "name": "Super"},
    (1, 70): {"image": "images/good.jpg", "name": "Good"},
    (1, 60): {"image": "images/average.jpg", "name": "Average"},
    (1, 0): {"image": "images/normal.jpg", "name": "Normal"},
    (3, 90): {"image": "images/super.jpg", "name": "Super"},
    (3, 80): {"image": "images/good.jpg", "name": "Good"},
    (3, 70): {"image": "images/average.jpg", "name": "Average"},
    (3, 0): {"image": "images/normal.jpg", "name": "Normal"},
    (5, 90): {"image": "images/good.jpg", "name": "Good"},
    (5, 80): {"image": "images/average.jpg", "name": "Average"},
    (5, 0): {"image": "images/normal.jpg", "name": "Normal"},
}

# Default certificate details
DEFAULT_CERTIFICATE = {"image": "images/normal.jpg", "name": "Normal Certificate"}


@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route('/get_certificate', methods=['POST'])
def get_certificate():
    """Retrieve certificate based on form data."""
    attempts = int(request.form['attempts'])
    marks = int(request.form['marks'])

    # Find matching certificate details
    certificate_details = find_matching_certificate(attempts, marks)

    # Render certificate template
    return render_template('certificate.html',
                           certificate_image=certificate_details["image"],
                           certificate_name=certificate_details["name"])


def find_matching_certificate(attempts, marks):
    """Find the matching certificate details."""
    for (max_attempts, min_marks), details in CERTIFICATE_DETAILS.items():
        if attempts <= max_attempts and marks >= min_marks:
            return details
    return DEFAULT_CERTIFICATE


if __name__ == "__main__":
    app.run(debug=True)
