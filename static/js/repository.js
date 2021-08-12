var BPOPUP = "";
(function ($) {
  $(function () {
    $("#search_repo").bind("click", function (e) {
      e.preventDefault();
      BPOPUP = $("#bpopup1").bPopup({
        speed: 650,
        transition: "slideDown",
        transitionClose: "slideDown",
      });
    });
  });
})(jQuery);
