function acceptDisclaimer() {
    console.log('Accept button clicked');
    const disclaimerBox = document.getElementById('disclaimerBox');

    // Set display to flex first
    disclaimerBox.setAttribute('style', 'display: flex !important;');

    // Use a timeout to change the display to none after a short delay
    setTimeout(() => {
        disclaimerBox.setAttribute('style', 'display: none !important;');
    }, 100);
}
