
// SCROLLING

(function ($) {
    "use strict"; // Start of use strict

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function () {
        $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 56
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };

    // Collapse now if page is not at top
    navbarCollapse();

    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

    var $root = $('html, body');

    $('a[href*=\\#]').on('click', function (event) {
        event.preventDefault();
        $('html,body').animate({ scrollTop: $(this.hash).offset().top }, 500);
    });

    // // Hide navbar when modals trigger
    // $('.portfolio-modal').on('show.bs.modal', function(e) {
    //     $(".navbar").addClass("d-none");
    // })
    // $('.portfolio-modal').on('hidden.bs.modal', function(e) {
    //     $(".navbar").removeClass("d-none");
    // })

})(jQuery); // End of use strict