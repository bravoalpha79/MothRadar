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
 * Post a new comment - Ajax call and DOM insertion.
 * Ajax code written based on a suggestion and a sample snippet
 * provided by ckz8780.
 **/
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

        $("#noComment").hide();
        $("#commentsList").append(newCommentDiv);
        $(newCommentDiv).fadeIn("4000");
      }
    });
  }
});

// Handle click of upvoteDone (disabled) button
$("#upvoteDone").click(function () {
  $("#upvoteMessage").text("Already upvoted.");
});

// upvoteFree button click - Ajax call and DOM insertion
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

// Homepage card animation
$(".homeCard").click(function () {
  $(this).children("p").toggle("500");
});
