document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", async function (event) {
        event.preventDefault();  
        
        const formData = new FormData(form);
        const response = await fetch("/legal-document", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log("Server Response:", result);
        alert(result.message);  
    });
});