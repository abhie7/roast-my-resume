function acceptDisclaimer() {
    // Use a timeout to change the display to none after a short delay
    setTimeout(() => {
        alert('Server under maintenance, come after some time');
    }, 50);
}

document
    .getElementById('resumeForm')
    .addEventListener('submit', function (event) {
        const fileInput = document.getElementById('resumeInput');
        const fileName = fileInput.value;
        const errorMessage = document.getElementById('error-message');

        if (!fileName.endsWith('.pdf')) {
            event.preventDefault(); // Prevent form submission
            errorMessage.style.display = 'block'; // Show error message
            errorMessage.style.margin = '0 0 1.6rem 0';
        } else {
            errorMessage.style.display = 'none'; // Hide error message
        }
    });

document
    .getElementById('resumeInput')
    .addEventListener('change', function (event) {
        const fileName = event.target.files[0]
            ? event.target.files[0].name
            : 'No file chosen. I dare you to only choose .pdf files. (Please)';
        document.getElementById('fileName').textContent = fileName;
        document.querySelector('.custom-file-label').textContent =
            'Choose Another File';
    });

document
    .getElementById('resumeForm')
    .addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(this);

        // Show loader
        document.getElementById('loader').style.display = 'flex';
        document.getElementById('roastMessage').innerText = '';

        console.log('Sending request to groq server...');

        fetch('/', {
            method: 'POST',
            body: formData,
        })
            .then((response) => {
                console.log('Received response from groq server:');
                return response.json();
            })
            .then((data) => {
                // Hide loader
                document.getElementById('loader').style.display = 'none';

                if (data.roast_message) {
                    // Display roast message
                    document.getElementById('roastMessage').innerHTML =
                        marked.parse(data.roast_message);
                    // console.log(marked.parse(data.roast_message));
                } else {
                    console.error('No roast message received');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                // Hide loader in case of error
                document.getElementById('loader').style.display = 'none';
            });

        document.querySelector('.result').classList.add('visible');
    });
