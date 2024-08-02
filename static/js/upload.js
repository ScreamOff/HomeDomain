document.addEventListener('DOMContentLoaded', function () {
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    const fileNameDisplay = document.getElementById('file-name');

    dropArea.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropArea.classList.add('dragover');
    });

    dropArea.addEventListener('dragleave', () => {
        dropArea.classList.remove('dragover');
    });

    dropArea.addEventListener('drop', (event) => {
        event.preventDefault();
        dropArea.classList.remove('dragover');
        const files = event.dataTransfer.files;
        handleFiles(files);
    });

    fileInput.addEventListener('change', () => {
        const files = fileInput.files;
        handleFiles(files);
    });

    function handleFiles(files) {
        fileNameDisplay.textContent = Array.from(files).map(file => file.name).join(', ') || 'Nie wybrano plików';
    }

    // Dodanie obsługi kliknięcia na etykietę, aby otworzyć okno wyboru plików
    const uploadButton = document.querySelector('label[for="file-input"]');
    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });
});
