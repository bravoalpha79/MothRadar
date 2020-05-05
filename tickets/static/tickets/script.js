function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$("#postComment").click(function () {
  let csrfToken = getCookie("csrftoken");
  //   let ticketId = parseInt($("#ticketId").val());
  let url = `comments/add/`;
  let text = $("#text").val();

  let data = {
    csrfmiddlewaretoken: csrfToken,
    // ticketId: ticketId,
    text: text,
  };

  $.post(url, data).done(function () {
    $("#comments").prepend("<p>Comment added</p>");
  });
});
