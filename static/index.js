import { DebugForm } from "./debug.js";

function main() {
    var file = document.getElementById("/tmp/test.txt").files[0];

    var reader = new FileReader();
    reader.onload = function (e) {
        var textArea = document.getElementById("textarea");
        textArea.value = e.target.result;
    };
    reader.readAsText(file);


    $(document).ready(function () {
        $("#loaded_text").click(function () {
            $.ajax({
                url: "/tmp/test.txt",
                dataType: "text",
                success: function (data) {
                    $(".text").html(data);
                }
            });
        });
    });
}

main();