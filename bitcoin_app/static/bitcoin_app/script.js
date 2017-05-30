    $(document).ready(function () {
    var interval = 1000;
    function refresh() {
        $.ajax({
            url: "",
            success: function(context) {
                $('#container').load(' #container', function(){$(this).children().unwrap()});
                setTimeout(function() {
                    refresh();
                     },
                interval);
            }
        });
    };
    refresh();
});