$(document).ready(function () {

  //main-nav btn
  $('#menu-btn').click(function () {
    $('.main-nav__list').slideToggle(300);
    if ($(this).hasClass('not-active')) {
      $(this).addClass('is-active').removeClass('not-active');
    } else {
      setTimeout(() => $(this).addClass('not-active').removeClass('is-active'), 0);
    }
  });

  //multimedia tabs on home page
  $(".multimedia-tab__content").not(":first").hide();
  $(".multimedia-tab__link").click(function () {
    $(".multimedia-tab__link").removeClass("active").eq($(this).index()).addClass("active");
    $(".multimedia-tab__content").hide().eq($(this).index()).fadeIn()
  }).eq(0).addClass("active");

  //multimedia gallery
  $('[data-fancybox="images"]').fancybox({
    buttons: [
      //"zoom",
      //"share",
      "slideShow",
      //"fullScreen",
      //"download",
      //"thumbs",
      "close"
    ],
  });
})