// FORM ELEMENTS

const expiryMonth = document.getElementById('id_expiry_month');
const expiryYear = document.getElementById('id_expiry_year');

const numberValidation = (input, type) => {
    // if not a number, raise error
    if (isNaN(+input)) {
        return `Please enter a valid ${type}.`;
    } else {
        return '';
    }
};

const monthValidation = (input) => {
    if (input < 1 || input > 12) {
        return 'Please enter a valid month.';
    } else {
        return '';
    }
};

expiryMonth.addEventListener('input', (e) => {
    const input = e.target.value;

    console.log(numberValidation(input, 'month'));
});

expiryYear.addEventListener('input', (e) => {
    const input = e.target.value;

    console.log(numberValidation(input, 'year'));
    console.log(monthValidation(input));
});
