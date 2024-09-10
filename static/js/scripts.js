$(document).ready(function(){
    $("#getRecommendationButton").click(function(){
        $(this).prop("disabled", true).text("Получение рекомендации...");

        $("#loadingIndicator").show();

        $.ajax({
            type: "POST",
            url: "/get_recommendation",
            contentType: "application/json",
            data: JSON.stringify({
                gender: $("#gender").val(),
                age: $("#age").val(),
                activity: $("#activity").val(),
                mood: $("#mood").val(),
                budget: $("#budget").val()
            }),
            success: function(response) {
                $("#recommendationText").text(response.recommendation);

                // Показываем блок с рекомендацией, добавляя класс 'show'
                $("#recommendationOutput").hide().fadeIn(1000).addClass('show');
            },
            error: function() {
                $("#recommendationText").text("Произошла ошибка при получении рекомендации.");
            },
            complete: function() {
                $("#getRecommendationButton").prop("disabled", false).text("Получить рекомендацию 🎁");

                $("#loadingIndicator").hide();

                $("html, body").animate({
                    scrollTop: $("#recommendationOutput").offset().top
                }, 800);
            }
        });
    });
});
