$(function () {

    var menu = $("#menu"),
        headerH = $("#header").innerHeight(),
        scrollOffset = $(window).scrollTop();
    
    /* Fixed Menu */
    checkScroll(scrollOffset)
    
    $(window).on("scroll", function() {
        scrollOffset = $(this).scrollTop();

        checkScroll(scrollOffset)

    });

    function checkScroll(scrollOffset) {

        if( scrollOffset >= headerH ) {
            menu.addClass("fixed");
        } else {
            menu.removeClass("fixed");
        }
    }

    /* Smooth scroll */
    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('scroll'), 
            blockOffset = $(blockId).offset().top - 80;

        $("#nav a").removeClass("active");
        $this.addClass("active");

        if ($("#nav_toggle").hasClass('active')) {
        
            $(window).on("scroll", function() {

            $('#nav_toggle').removeClass("active");

            $("#nav").removeClass("active");

            });
        }
        
        
        $("html, body").animate({
            scrollTop: blockOffset
        }, 500);
    });

    /* Menu nav Toggle */
    $("#nav_toggle").on("click", function(event) {
        event.preventDefault();
        
        $(this).toggleClass("active");
        $("#nav").toggleClass("active");
    });

    $("[data-slider]").slick( {
        infinite: true,
        fade: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

});