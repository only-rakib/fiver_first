
$(document).ready(function () {
    $(window).on('load scroll', function () {
        var scrolled = $(this).scrollTop();
        
        $('#hero-vid').css('transform', 'translate3d(0, ' + -(scrolled * .25) + 'px, 0)'); // parallax (25% scroll rate)
       
      
    
    });    
    
});
