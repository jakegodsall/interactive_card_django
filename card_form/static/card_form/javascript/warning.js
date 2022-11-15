const warningTemplate = document.getElementById('warning-template');
const backgroundImage = document.getElementById('background-image');

const clone = warningTemplate.content.cloneNode(true);

document.body.insertBefore(clone, backgroundImage);

const warningAccept = document.getElementById('warning-accept');

warningAccept.addEventListener('click', () => {
    document.getElementById('warning-overlay').remove();
});
