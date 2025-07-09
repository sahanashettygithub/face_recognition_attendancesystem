const video = document.getElementById('video');
const markBtn = document.getElementById('markBtn');
const statusText = document.getElementById('status');
const totalEl = document.getElementById('total-students');
const presentEl = document.getElementById('present-students');
const absentEl = document.getElementById('absent-students');
const rateEl = document.getElementById('attendance-rate');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Camera access denied:", err);
        statusText.textContent = "Camera access denied";
    });

markBtn.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = 320;
    canvas.height = 240;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageDataURL = canvas.toDataURL('image/jpeg');

    fetch('/mark_attendance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageDataURL })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            statusText.textContent = `✔️ Marked Present: ${data.name}`;
            presentEl.textContent = data.present;
            absentEl.textContent = data.absent;
            rateEl.textContent = `${data.rate}%`;
        } else {
            statusText.textContent = `❌ ${data.message}`;
        }
    })
    .catch(err => {
        console.error("Error submitting image:", err);
        statusText.textContent = "Error submitting image.";
    });
});
