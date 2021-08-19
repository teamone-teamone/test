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

const closePopup1 = () => {
  $("#bpopup1").bPopup().close();
};

(function ($) {
  $(function () {
    $("#share_repo").bind("click", function (e) {
      e.preventDefault();
      BPOPUP = $("#bpopup2").bPopup({
        speed: 600,
        transition: "slideUp",
        transitionClose: "slideUp",
      });
    });
  });
})(jQuery);

const closePopup2 = () => {
  $("#bpopup2").bPopup().close();
};

document.querySelectorAll("form").forEach((element) => {
  element.addEventListener("focusout", (e) => {
    if (e.path[1].id == "url_input") {
      if (e.path[0].value) {
        e.path[1].submit();
      }
    } else {
      if (e.path[1].id !== "search_popup") e.path[1].submit();
    }
  });
});
