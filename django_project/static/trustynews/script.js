

function setupML(json){
    $cols = $(".ml_cont .stats .col ul");
    $emotion = $($cols[0]).find("li");
    $lang = $($cols[1]).find("li");
    $social = $($cols[2]).find("li");

    for (var i = 0; i < $emotion.length; i++) {
        $($emotion[i]).find("div").css("width",json.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100 + "%");
    }
    for (var i = 0; i < $lang.length; i++) {
        $($lang[i]).find("div").css("width",json.Language[$($lang[i]).find("span")[0].innerHTML]*100 + "%");
    }
    for (var i = 0; i < $social.length; i++) {
        $($social[i]).find("div").css("width",json.Social[$($social[i]).find("span")[0].innerHTML]*100 + "%");
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
