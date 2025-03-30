
document.getElementById("stalker-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    let lat = document.getElementById("latitude").value;
    let lon = document.getElementById("longitude").value;
    let timeDiff = document.getElementById("time_diff").value;
    let distanceDiff = document.getElementById("distance_diff").value;

    if (!lat || !lon || !timeDiff || !distanceDiff) {
        document.getElementById("result").innerText = "⚠️ Please fill all fields!";
        return;
    }

    try {
        console.log("📡 Sending request...");
        const response = await fetch("http://127.0.0.1:5000/stalker/predict", {  
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                latitude: parseFloat(lat),
                longitude: parseFloat(lon),
                time_diff: parseFloat(timeDiff),
                distance_diff: parseFloat(distanceDiff)
            })
        });

        console.log("✅ Response received:", response);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("✅ Data:", data);
        document.getElementById("result").innerText = data.result;
    } catch (error) {
        console.error("❌ Fetch error:", error);
        document.getElementById("result").innerText = "❌ Error detecting stalker.";
    }
});
