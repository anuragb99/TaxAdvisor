document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('upload-btn');
    const pdfUpload = document.getElementById('pdf-upload');
    const errorDiv = document.getElementById('upload-error');
    const progressDiv = document.getElementById('progress');

    uploadBtn.addEventListener('click', async function() {
        errorDiv.style.display = 'none';
        progressDiv.style.display = 'none';
        const file = pdfUpload.files[0];
        if (!file) {
            errorDiv.textContent = 'Please select a PDF file.';
            errorDiv.style.display = 'block';
            return;
        }
        if (file.type !== 'application/pdf') {
            errorDiv.textContent = 'Only PDF files are allowed.';
            errorDiv.style.display = 'block';
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
        progressDiv.style.display = 'block';
        try {
            const res = await fetch('/api/upload-pdf', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (!res.ok) {
                throw new Error(data.detail || 'Extraction failed.');
            }
            localStorage.setItem('extractedUserFinancials', JSON.stringify(data));
            window.location.href = 'review.html';
        } catch (err) {
            errorDiv.textContent = err.message;
            errorDiv.style.display = 'block';
        } finally {
            progressDiv.style.display = 'none';
        }
    });
}); 