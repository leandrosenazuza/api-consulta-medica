// Obtenha o botão do navbar-toggler
const navbarToggler = document.querySelector('.navbar-toggler');

// Adicione um evento de clique ao botão
navbarToggler.addEventListener('click', function () {
    // Aqui você pode adicionar código adicional para executar quando o botão é clicado
    // O código pode fazer ações como, por exemplo, registrar uma mensagem de console
    console.log('Botão de navbar-toggler foi clicado.');

    // Se quiser, você pode manipular o estado de collapse de forma manual também, mas não é necessário.
    // Por exemplo:
    // const collapseElement = document.getElementById('navbarToggleExternalContent');
    // if (collapseElement.classList.contains('show')) {
    //     // Fecha o colapso manualmente
    //     collapseElement.classList.remove('show');
    // } else {
    //     // Abre o colapso manualmente
    //     collapseElement.classList.add('show');
    // }
});
