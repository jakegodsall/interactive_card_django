// FORM ELEMENTS
const formCardholderName = document.getElementById('id_cardholder_name');
const formCardNumber = document.getElementById('id_card_number');
const formExpiryMonth = document.getElementById('id_expiry_month');
const formExpiryYear = document.getElementById('id_expiry_year');
const formCVC = document.getElementById('id_cvc');

// CARD ELS
const cardCardholderName = document.getElementById('card-name');
const cardCardNumber = document.getElementById('card-number');
const cardExpiryMonth = document.getElementById('card-month');
const cardExpiryYear = document.getElementById('card-year');
const cardCVC = document.getElementById('card-cvc');

formCardholderName.addEventListener('input', (e) => {
    const name = e.target.value;
    cardCardholderName.innerText = name;
});

formExpiryMonth.addEventListener('input', (e) => {
    const expiryMonth = e.target.value;
    cardExpiryMonth.innerText = expiryMonth;

    if (expiryMonth === '') {
        cardExpiryMonth.innerText = '00';
    }
});

formExpiryYear.addEventListener('input', (e) => {
    const expiryYear = e.target.value;
    cardExpiryYear.innerText = expiryYear;

    if (expiryYear === '') {
        cardExpiryYear.innerText = '00';
    }
});

formCVC.addEventListener('input', (e) => {
    const cvc = e.target.value;
    cardCVC.innerText = cvc;

    if (cvc === '') {
        cardCVC.innerText = '000';
    }
});

formCardNumber.addEventListener('input', (e) => {
    const number = e.target.value;
    const originalNumber = '0000000000000000';
    const originalArray = originalNumber.split('');

    const numberString = number.toString();

    for (let i = 0; i < numberString.length; i++) {
        originalArray[i] = numberString[i];
    }

    let formattedNumber = [
        ...originalArray.slice(0, 4),
        ' ',
        ...originalArray.slice(4, 8),
        ' ',
        ...originalArray.slice(8, 12),
        ' ',
        ...originalArray.slice(12, 16),
    ].join('');

    cardCardNumber.innerText = formattedNumber;
});
