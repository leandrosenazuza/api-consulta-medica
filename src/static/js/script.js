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


    // Fazer solicitação AJAX para obter informações da coleta
    $.ajax({
    url: "/coleta/{{ paciente.codigoColetaPaciente }}",
    method: "GET",
    success: function(data) {
        // Preencher os campos do formulário com os dados da coleta
        $("#coletaAnos{{ paciente.codigoColetaPaciente }}").val(data.coletaAnos);
        $("#ultimaColeta{{ paciente.codigoColetaPaciente }}").val(data.ultimaColeta);
        $("#proximaColeta{{ paciente.codigoColetaPaciente }}").val(data.proximaColeta);
    },
    error: function(xhr, status, error) {
        console.error("Erro ao obter informações da coleta:", error);
    }
});