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
    $("#commentMessage").text("You can't post an empty comment.");
  } else {
    let data = {
      csrfmiddlewaretoken: csrfToken,
      text: text,
    };
    $.post(url, data).done(function (response) {
      if (response.error) {
        $("#commentMessage").text(response.error);
      } else {
        $("#text").val("");
        $("#commentMessage").text(response.success);

        let newCommentDiv = document.createElement("div");
        newCommentDiv.id = "newComment";
        newCommentDiv.setAttribute("class", "card");

        let newCommentHeader = document.createElement("small");
        newCommentHeader.id = "newCommentHeader";
        newCommentHeader.innerHTML = `Posted by ${response.author} a moment ago`;

        let newCommentText = document.createElement("p");
        newCommentText.id = "newCommentText";
        newCommentText.innerHTML = `${response.text}`;

        newCommentDiv.appendChild(newCommentHeader);
        newCommentDiv.appendChild(newCommentText);

        let comments = document.getElementById("commentsList");
        comments.insertBefore(newCommentDiv, comments.firstChild);
      }
    });
  }
});
