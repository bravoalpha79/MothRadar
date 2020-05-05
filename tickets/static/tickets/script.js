// getCookie function obtained from Django documentation
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
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
  const url = `comments/add/`;
  const text = $("#text").val();
  let csrfToken = getCookie("csrftoken");

  if (!text) {
    $("#comments").prepend("<small>You can't post an empty comment.</small>");
  } else {
    let data = {
      csrfmiddlewaretoken: csrfToken,
      text: text,
    };
    $.post(url, data).done(function () {
      $("#comments").prepend("<small>Comment added</small>");
      $("#text").val("");
    });
  }
});
