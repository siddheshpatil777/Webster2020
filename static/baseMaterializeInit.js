$(window).on('load', function() {
    $('.myLoader-wrapper').fadeOut("slow");
});
$(document).ready(function() {

    $('.sidenav').sidenav();
    $('.materialboxed').materialbox();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.scrollspy').scrollSpy();
    // $('').edge='right';
    var elems = document.getElementById('slide-out');
    var rightNav = M.Sidenav.init(elems, {
        edge: 'right'
    });

    document.getElementById('notificationsButton').addEventListener("click", function() {
        rightNav.open();
    });

});
