$(document).ready(function($) {
    $('#cpfInput').mask('000.000.000-00');
});

$(document).ready(function($) {
    $('#dataNascimento').mask('0000-00-00');
});

$(document).ready(function($) {
    $('.cpf-mask').mask('000.000.000-00');
    $('.date-mask').mask('0000-00-00');
});

$(document).ready(function() {
    $('.cpf-mask').mask('000.000.000-00');
});


const coletaAnosInput = document.getElementById('coletaAnos');

// Adiciona um evento de "keyup" para verificar o valor inserido no input
coletaAnosInput.addEventListener('keyup', function() {
    const inputValue = coletaAnosInput.value.trim(); // Remove espaços em branco do início e do fim

    // Verifica se o valor inserido corresponde ao formato esperado [ano1, ano2, ano3, ...]
    const regex = /^\[\d{4}(,\s?\d{4})*\]$/;
    const isValid = regex.test(inputValue);

    // Se o valor não corresponder ao formato esperado, limpa o campo
    if (!isValid) {
        coletaAnosInput.value = '';
    }
});