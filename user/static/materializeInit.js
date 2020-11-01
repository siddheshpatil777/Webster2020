$(document).ready(function () {

    $('.sidenav').sidenav();
    $('.materialboxed').materialbox();
    $('.parallax').parallax();
    $('.tabs').tabs({
        swipeable: true
    });
    $('.modal').modal();
    $('.tooltipped').tooltip();
    $('.fixed-action-btn').floatingActionButton({
        hoverEnabled: false
    });
    $('.modal-overlay').addClass('baapbaap');

    $('select').not('.disabled').formSelect();
    $('.tap-target').tapTarget();

    $('.tabs').tabs();
    // $(".dropdown-trigger").dropdown();
        
   
        

    $('#menu').on('click', function () {
        var instance = M.TapTarget.getInstance(document.getElementById('fd'));
        instance.open();
        // console.log("dfsdfsdfsd");
        // $('.tap-target').tapTarget('next');
    });
});