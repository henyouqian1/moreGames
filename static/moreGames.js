var onDocReady = function(){
    $('.button:first-child').addClass("bigButton");
    $('table:even').addClass("even");
}

$(document).ready(onDocReady);