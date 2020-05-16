/**
 * GetCookie function obtained from Django documentation
 * From the list of document cookies, extract the one with the
 * name passed in as the argument.
 **/
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

/**
 * Post a new comment - Ajax call to backend and DOM insertion.
 * Ajax logic based on a suggestion and a sample snippet
 * provided by ckz8780.
 **/
$("#postComment").click(function () {
  const url = `comments/add/`;
  const text = $("#commentTextArea").val();
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
        $("#commentTextArea").val("");
        $("#commentMessage").text(response.success);

        let newCommentDiv = document.createElement("div");

        let newCommentBody = document.createElement("div");
        newCommentDiv.setAttribute("class", "card-body");

        let newCommentHeader = document.createElement("small");
        newCommentHeader.setAttribute("class", "card-subtitle text-muted");
        newCommentHeader.innerHTML = `Posted by ${response.author} a moment ago`;

        let newCommentText = document.createElement("p");
        newCommentText.setAttribute("class", "card-text mt-2");
        newCommentText.innerHTML = `${response.text}`;

        newCommentBody.appendChild(newCommentHeader);
        newCommentBody.appendChild(newCommentText);
        newCommentDiv.appendChild(newCommentBody);

        $("#noComment").hide();
        $("#commentsList").append(newCommentDiv);
        $(newCommentDiv).addClass("card mt-2 newComment");
        $(newCommentDiv).fadeIn("4000");
      }
    });
  }
});

/**
 * Handling of upvoteFree button click -
 * Ajax call to backend and DOM insertion.
 * Ajax logic based on a suggestion and a sample snippet
 * provided by ckz8780.
 */
$("#upvoteFree").click(function () {
  const url = "upvote/";
  let csrfToken = getCookie("csrftoken");

  let data = {
    csrfmiddlewaretoken: csrfToken,
  };

  $.post(url, data).done(function (response) {
    let count = parseInt($("#upvoteCount").text());
    if (response.error) {
      $("#upvoteMessage").text(response.error);
    } else {
      count += 1;
      $("#upvoteMessage").text(response.success);
      $("#upvoteFree")
        .removeClass("btn-primary")
        .addClass("btn-secondary")
        .attr("disabled");
      $("#upvoteCount").text(count);
    }
  });
});

// Handle click of upvoteDone (disabled) button
$("#upvoteDone").click(function () {
  $("#upvoteMessage").text("Already upvoted.");
});

// Homepage card animation - '.not(this)' obtained from Stack Overflow
$(".homeCard").click(function () {
  $(this).children("p").toggle("500");
  $(".homeCard").not(this).children("p").hide("500");
});
