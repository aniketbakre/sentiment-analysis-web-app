function checkEmotion() {
    const inputText = document.getElementById('inputText').value;
    console.log('Function called');
    console.log('Input text', inputText);
    if (inputText.trim() === ) {
        alert(Please enter some text.);
        return;
    }

     Simulate emotion analysis (replace this with actual model integration)
    const emotions = [anger, disgust, fear, joy, neutral, sadness, surprise];
    const randomEmotion = emotions[Math.floor(Math.random()  emotions.length)];

    document.getElementById('output').innerText = `Detected Emotion ${randomEmotion}`;
}

function refreshPage() {
    document.getElementById('inputText').value = ;
    document.getElementById('output').innerText = ;
}
