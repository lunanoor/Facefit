const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');
const uploadSection = document.getElementById('upload-section');
const previewSection = document.getElementById('preview-section');
const resultsSection = document.getElementById('results-section');
const imagePreview = document.getElementById('image-preview');

// Drag and drop handlers
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.borderColor = '#6366f1';
    dropArea.style.transform = 'scale(1.02)';
});

dropArea.addEventListener('dragleave', () => {
    dropArea.style.borderColor = 'rgba(255, 255, 255, 0.1)';
    dropArea.style.transform = 'scale(1)';
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.borderColor = 'rgba(255, 255, 255, 0.1)';
    dropArea.style.transform = 'scale(1)';
    const file = e.dataTransfer.files[0];
    handleFile(file);
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    handleFile(file);
});

function handleFile(file) {
    if (!file || !file.type.startsWith('image/')) {
        alert('Please upload a valid image file.');
        return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        uploadSection.classList.add('hidden');
        previewSection.classList.remove('hidden');

        // Simulate analysis delay for effect + actual API call
        analyzeImage(file);
    };
    reader.readAsDataURL(file);
}

async function analyzeImage(file) {
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || 'Something went wrong.');
            resetApp();
            return;
        }

        displayResults(data);

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to connect to the server.');
        resetApp();
    }
}

function displayResults(data) {
    // Hide preview, show results
    previewSection.classList.add('hidden');
    resultsSection.classList.remove('hidden');

    // Populate data
    document.getElementById('result-shape').textContent = data.analysis.face_shape;
    document.getElementById('result-tone').textContent = data.analysis.skin_tone;
    document.getElementById('hair-tips').textContent = data.recommendations.tips || "Try these styles:";

    // Hairstyles
    const hairList = document.getElementById('hair-list');
    hairList.innerHTML = '';
    data.recommendations.hairstyles.forEach(style => {
        const li = document.createElement('li');
        li.textContent = style;
        hairList.appendChild(li);
    });

    // Hair Colors
    const hairColorList = document.getElementById('hair-color-list');
    hairColorList.innerHTML = '';
    data.recommendations.hair_colors.forEach(color => {
        // Generate a pseudo-color for the dot (mapping names to approx hex would be better, but this is a simple demo)
        // For now just consistent style
        const li = createColorItem(color);
        hairColorList.appendChild(li);
    });

    // Clothing Colors
    const clothList = document.getElementById('clothing-color-list');
    clothList.innerHTML = '';
    data.recommendations.clothing_colors.forEach(color => {
        const li = createColorItem(color);
        clothList.appendChild(li);
    });
}

function createColorItem(colorName) {
    const li = document.createElement('li');
    li.className = 'color-item';

    const dot = document.createElement('div');
    dot.className = 'color-dot';
    dot.style.backgroundColor = getColorHex(colorName); // Helper to get approx hex

    li.appendChild(dot);
    li.appendChild(document.createTextNode(colorName));
    return li;
}

function getColorHex(name) {
    // Premium Palette Mapping
    const colors = {
        // Hair Colors
        "Deep Espresso": "#4B3621",
        "Chestnut": "#8B4513",
        "Honey": "#D2B48C",
        "Caramel": "#E5BE82",
        "Mocha": "#4a2c2a",
        "Champagne": "#e5be9e",
        "Silver Gray": "#c0c0c0",
        "Jet Black": "#0a0a0a",
        "Ash Blonde": "#dcd0ba",
        "Light Brown": "#b5651d",
        "Strawberry Blonde": "#ffcc99",

        // Clothing Colors
        "Earth Brown": "#6b4226",
        "Copper": "#b87333",
        "Olive Drab": "#556b2f",
        "Sandstone": "#deb887",
        "Terracotta": "#cd5c5c",
        "Midnight Blue": "#2D4059",
        "Sunset Red": "#EA5455",
        "Deep Amber": "#F07B3F",
        "Golden Sand": "#FFD460",
        "Peach": "#FFE5B4",
        "Soft Pink": "#E3BFC3"
    };
    return colors[name] || "#ccc";
}

function resetApp() {
    fileInput.value = '';
    imagePreview.src = '';
    resultsSection.classList.add('hidden');
    previewSection.classList.add('hidden');
    uploadSection.classList.remove('hidden');
}
