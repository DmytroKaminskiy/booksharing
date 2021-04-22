$(document).ready(function () {
    $(".request-book-js").on("click", function () {
        // make request
        let bookId = $(this).data('book-id');
        let targetUrl = `/api/v1/book/create/request/${bookId}/`;
        let button = $(this);

        $.ajax({
            url: targetUrl,         /* Куда пойдет запрос */
            method: 'get',             /* Метод передачи (post или get) */
            dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
            success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
                alert('Your request was created successfully.');            /* В переменной data содержится ответ от index.php. */
                button.hide();
            }
        });
    });
});
// https://learn.javascript.ru/
// https://ru.reactjs.org/
// https://ru.reactjs.org/tutorial/tutorial.html
// react native https://reactnative.dev/

// https://ionicframework.com/

// https://angular.io/
