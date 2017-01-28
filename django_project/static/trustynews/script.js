$(document).ready(function(){
    $("button[name='go']").attr('disabled', false);
});

function setupML(json){
    $cols = $(".ml_cont .stats .col ul");
    $emotion = $($cols[0]).find("li");
    $lang = $($cols[1]).find("li");
    $social = $($cols[2]).find("li");

    for (var i = 0; i < $emotion.length; i++) {
        $($emotion[i]).find("div").css("width",json.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100 + "%");
        $($emotion[i]).find(".percent").css("width",json.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100 + "%");
    }
    for (var i = 0; i < $lang.length; i++) {
        $($lang[i]).find("div").css("width",json.Language[$($lang[i]).find("span")[0].innerHTML]*100 + "%");
        $($lang[i]).find(".percent").css("width",json.Language[$($lang[i]).find("span")[0].innerHTML]*100 + "%");
    }
    for (var i = 0; i < $social.length; i++) {
        $($social[i]).find("div").css("width",json.Social[$($social[i]).find("span")[0].innerHTML]*100 + "%");
        $($social[i]).find(".percent").css("width",json.Social[$($social[i]).find("span")[0].innerHTML]*100 + "%");
    }

    total = $(".ml_cont .overalltotal");
    total.find("div").css("width",json.Total*100 + "%");
    total.find(".percent").html(Math.round(json.Total*100) + "%");

    //KEY WORDS
    keywords = $(".ml_cont .keywords ul");
    keywords.html("");
    str = "";
    for (var i = 0; i < json.Keywords.length; i++) {
        str += "<li>"+json.Keywords[i]+"</li>";
    }
    keywords.html(str);
}


function changeTab(tab){
    $(".tabs_cont li").removeClass("selected");
    $($(".tabs_cont li")[tab]).addClass("selected");
    $(".content_cont .cont").addClass("hide");
    $($(".content_cont .cont")[tab]).removeClass("hide");
}



function isURL(str) {
    var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
   return regexp.test(str);
}
