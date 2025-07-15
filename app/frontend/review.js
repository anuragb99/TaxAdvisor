document.addEventListener('DOMContentLoaded', function() {
    const reviewForm = document.getElementById('review-form');
    const successMessage = document.getElementById('success-message');
    const backBtn = document.getElementById('back-btn');

    // Load data from localStorage
    const data = JSON.parse(localStorage.getItem('extractedUserFinancials') || '{}');
    let hasData = false;
    for (const [key, value] of Object.entries(data)) {
        const input = reviewForm.elements.namedItem(key);
        if (input) {
            input.value = value;
            hasData = true;
        }
    }
    if (hasData) {
        successMessage.textContent = 'Data extracted and loaded successfully!';
        successMessage.style.display = 'block';
    }

    backBtn.addEventListener('click', function() {
        window.location.href = 'upload.html';
    });
}); 