// FORM ELEMENTS
const form = document.forms[0];
const cardholder = document.getElementById('id_cardholder_name');
const cardnumber = document.getElementById('id_card_number');
const expiryMonth = document.getElementById('id_expiry_month');
const expiryYear = document.getElementById('id_expiry_year');
const cvc = document.getElementById('id_cvc');

form.noValidate = true;

const setError = (widget, message) => {
    const errorLi = widget.nextElementSibling.firstElementChild;
    console.log(errorLi);
    errorLi.innerText = message;
};

const removeError = (widget) => {
    const errorLi = widget.nextElementSibling.firstElementChild;
    errorLi.innerText = '';
};

const isNumber = (input) => {
    return isNaN(Number(input));
};

// CARDHOLDER NAME VALIDATION
cardholder.addEventListener('input', (e) => {
    const cardholderInput = e.target.value.trim();
    const re = /^[a-zA-Z -]+$/;

    // Only letters, spaces and hyphens
    if (!re.exec(cardholderInput)) {
        setError(cardholder, 'Please use valid characters.');
    } else {
        removeError(cardholder);
    }
});

// CARDNUMBER VALIDATION
cardnumber.addEventListener('input', (e) => {
    const cardnumberInput = e.target.value.trim();

    // Is a number
    if (isNumber(cardnumberInput)) {
        setError(cardnumber, 'Wrong format, numbers only.');
    } else {
        removeError(cardnumber);
    }
});

// EXPIRY MONTH VALIDATION
expiryMonth.addEventListener('input', (e) => {
    const expiryMonthInput = e.target.value.trim();

    // If is not a number
    if (isNumber(expiryMonthInput)) {
        setError(expiryMonth, 'Enter a valid month.');
    } else if (expiryMonthInput < 1 || expiryMonthInput > 12) {
        // if is out of range
        setError(expiryMonth, 'Enter a valid month.');
    } else {
        removeError(expiryMonth);
    }
});

// EXPIRY YEAR VALIDATION
expiryYear.addEventListener('input', (e) => {
    const expiryYearInput = e.target.value.trim();
    const currentYear = new Date().getFullYear() - 2000;

    // If is not a number
    if (isNumber(expiryYearInput)) {
        setError(expiryYear, 'Enter a valid year.');
    } else if (expiryYearInput < currentYear) {
        setError(expiryYear, 'Enter a valid year.');
    } else {
        removeError(expiryYear);
    }
});

// CVC VALIDATION
cvc.addEventListener('input', (e) => {
    const cvcInput = e.target.value.trim();

    // If is not a number
    if (isNumber(cvcInput)) {
        setError(cvc, 'Enter a valid CVC.');
    } else {
        removeError(cvc);
    }
});
