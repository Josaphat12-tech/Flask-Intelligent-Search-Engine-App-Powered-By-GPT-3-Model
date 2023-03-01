const questionForm = document.getElementById('question-form');
const questionInput = document.getElementById('question-input');
const chatHistory = document.getElementById('chat-history');

questionForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const question = questionInput.value;
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const answer = xhr.responseText;
                const newQuestion = document.createElement('div');
                newQuestion.classList.add('chat-message', 'mb-4');
                const newQuestionContent = `
                    <div class="chat-message-content
