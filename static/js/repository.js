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

const closePopup = () => {
  $("#bpopup1").bPopup().close();
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
