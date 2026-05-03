document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const btn = document.getElementById('predict-btn');
    const resultContainer = document.getElementById('result-container');
    const predictionText = document.getElementById('prediction-text');
    
    // Animate button
    const originalText = btn.innerText;
    btn.innerText = 'Predicting...';
    btn.disabled = true;
    
    const data = {
        schooling: document.getElementById('schooling').value,
        income: document.getElementById('income').value,
        adultMortality: document.getElementById('adultMortality').value,
        bmi: document.getElementById('bmi').value,
        alcohol: document.getElementById('alcohol').value,
        polio: document.getElementById('polio').value,
        gdp: document.getElementById('gdp').value
    };
    
    console.log("Sending data:", data);
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        console.log("Received result:", result);
        
        if (response.ok) {
            predictionText.innerText = result.prediction.toFixed(1);
            resultContainer.classList.remove('hidden');
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('An error occurred. Please check the console for details.');
        console.error("Fetch error:", error);
    } finally {
        btn.innerText = originalText;
        btn.disabled = false;
    }
});
