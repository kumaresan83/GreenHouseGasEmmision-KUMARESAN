// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {

    // --- Element References ---
    const welcomePage = document.getElementById('welcome-page');
    const predictorPage = document.getElementById('predictor-page');
    const startButton = document.getElementById('start-button');
    const welcomeNavButton = document.getElementById('welcome-nav-button');
    const predictButton = document.getElementById('predict-button');
    const resultText = document.getElementById('result-text');

    // Get references to all input fields
    const supplyWoMarginInput = document.getElementById('supply-wo-margin');
    const marginInput = document.getElementById('margin');
    const dqReliabilityInput = document.getElementById('dq-reliability');
    const dqTemporalInput = document.getElementById('dq-temporal');
    const dqGeoInput = document.getElementById('dq-geo');
    const dqTechInput = document.getElementById('dq-tech');
    const dqDataInput = document.getElementById('dq-data');

    // Get references to the value display spans for the sliders
    const dqReliabilityValue = document.getElementById('dq-reliability-value');
    const dqTemporalValue = document.getElementById('dq-temporal-value');
    const dqGeoValue = document.getElementById('dq-geo-value');
    const dqTechValue = document.getElementById('dq-tech-value');
    const dqDataValue = document.getElementById('dq-data-value');

    // --- Page Navigation Logic ---
    const showWelcomePage = () => {
        welcomePage.classList.remove('hidden');
        predictorPage.classList.add('hidden');
        welcomeNavButton.classList.add('hidden');
    };

    const showPredictorPage = () => {
        welcomePage.classList.add('hidden');
        predictorPage.classList.remove('hidden');
        welcomeNavButton.classList.remove('hidden');
    };

    // --- Prediction Logic ---
    const updateSliderValues = () => {
        dqReliabilityValue.textContent = parseFloat(dqReliabilityInput.value).toFixed(2);
        dqTemporalValue.textContent = parseFloat(dqTemporalInput.value).toFixed(2);
        dqGeoValue.textContent = parseFloat(dqGeoInput.value).toFixed(2);
        dqTechValue.textContent = parseFloat(dqTechInput.value).toFixed(2);
        dqDataValue.textContent = parseFloat(dqDataInput.value).toFixed(2);
    };

    const predictEmissionFactor = () => {
        const supplyWoMargin = parseFloat(supplyWoMarginInput.value) || 0;
        const margin = parseFloat(marginInput.value) || 0;
        const dqReliability = parseFloat(dqReliabilityInput.value);
        const dqTemporal = parseFloat(dqTemporalInput.value);
        const dqGeo = parseFloat(dqGeoInput.value);
        const dqTech = parseFloat(dqTechInput.value);
        const dqData = parseFloat(dqDataInput.value);
        
        // A very simplified "prediction" formula for demonstration
        const averageDq = (dqReliability + dqTemporal + dqGeo + dqTech + dqData) / 5;
        let prediction = (supplyWoMargin + margin) * averageDq;
        
        resultText.textContent = `Predicted Factor = ${prediction.toFixed(4)}`;
    };

    // --- Event Listeners ---
    startButton.addEventListener('click', showPredictorPage);
    welcomeNavButton.addEventListener('click', showWelcomePage);
    predictButton.addEventListener('click', predictEmissionFactor);

    // Event listeners for slider changes to update the displayed value
    dqReliabilityInput.addEventListener('input', updateSliderValues);
    dqTemporalInput.addEventListener('input', updateSliderValues);
    dqGeoInput.addEventListener('input', updateSliderValues);
    dqTechInput.addEventListener('input', updateSliderValues);
    dqDataInput.addEventListener('input', updateSliderValues);

    // Initial state setup on page load
    showWelcomePage();
    updateSliderValues();
});
