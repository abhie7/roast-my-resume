document
    .getElementById('resumeForm')
    .addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(this);

        fetch('/', {
            method: 'POST',
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                document.getElementById('roastMessage').textContent =
                    data.roast_message;
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
