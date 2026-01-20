// ===============================
// EMOTION DETECTION JS (FINAL)
// ===============================

document.addEventListener("DOMContentLoaded", () => {

    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const emotionText = document.getElementById("emotion");
    const startBtn = document.getElementById("startEmotionBtn");
    const box = document.getElementById("emotionBox");

    const ctx = canvas.getContext("2d");
    let cameraStarted = false;

    startBtn.addEventListener("click", () => {

        if (cameraStarted) return;
        cameraStarted = true;

        box.style.display = "block";
        emotionText.innerText = "📷 Mengaktifkan kamera...";

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
                video.play();
                emotionText.innerText = "🧠 Mendeteksi emosi...";
                setInterval(sendFrame, 2000);
            })
            .catch(err => {
                console.error(err);
                alert("Akses kamera ditolak oleh browser");
            });
    });

    function sendFrame() {
        if (!video.videoWidth) return;

        ctx.drawImage(video, 0, 0, 224, 224);

        canvas.toBlob(blob => {
            let formData = new FormData();
            formData.append("image", blob);

            fetch("/predict_emotion", {
                method: "POST",
                body: formData
            })
            .then(res => res.json())
            .then(data => {
                emotionText.innerText =
                    `🧠 Emosi: ${data.emotion} (${(data.confidence*100).toFixed(1)}%)`;
            })
            .catch(err => console.error(err));
        }, "image/jpeg");
    }

});
