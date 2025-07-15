document.addEventListener('DOMContentLoaded', function() {
    const startBtn = document.getElementById('start-btn');
    const landingContainer = document.getElementById('landing-container');
    const formContainer = document.getElementById('form-container');
    const pdfUpload = document.getElementById('pdf-upload');
    const reviewForm = document.getElementById('review-form');
    const errorMessage = document.getElementById('error-message');

    startBtn.addEventListener('click', function() {
        landingContainer.style.display = 'none';
        formContainer.style.display = 'block';
    });

    pdfUpload.addEventListener('change', async function(e) {
        errorMessage.style.display = 'none';
        const file = e.target.files[0];
        if (!file) return;
        if (file.type !== 'application/pdf') {
            errorMessage.textContent = 'Please upload a PDF file.';
            errorMessage.style.display = 'block';
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
        try {
            const res = await fetch('/api/upload-pdf', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (!res.ok) {
                throw new Error(data.detail || 'Extraction failed.');
            }
            // Fill form fields
            for (const [key, value] of Object.entries(data)) {
                const input = reviewForm.elements.namedItem(key);
                if (input) input.value = value;
            }
        } catch (err) {
            errorMessage.textContent = err.message;
            errorMessage.style.display = 'block';
        }
    });
}); 