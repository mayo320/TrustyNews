searching = false;
$(document).ready(function(){
    $("button[name='go']").attr('disabled', false);

    $(".search_form input[name='searchURL']").keypress(function(event){
        if(event.keyCode == 13){
            event.preventDefault();
            if(!searching) $("button[name='go']").click();
            searching = true;
            $(this).blur();
        }
    });
});

function setupML(data){
    MLjson = data.MachineLearning;
    if(!MLjson.Emotion){
        $(".ml_cont .stats").hide();
        return;
    }
    $(".ml_cont .stats").show();
    $cols = $(".ml_cont .stats .col ul");
    $emotion = $($cols[0]).find("li");
    $lang = $($cols[1]).find("li");
    $social = $($cols[2]).find("li");

    for (var i = 0; i < $emotion.length; i++) {
        $($emotion[i]).find("div").css("width",MLjson.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100 + "%");
        $($emotion[i]).find(".percent").html(" "+ Math.round(MLjson.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100) + "%");
    }
    for (var i = 0; i < $lang.length; i++) {
        $($lang[i]).find("div").css("width",MLjson.Language[$($lang[i]).find("span")[0].innerHTML]*100 + "%");
        $($lang[i]).find(".percent").html(" "+ Math.round(MLjson.Language[$($lang[i]).find("span")[0].innerHTML]*100) + "%");
    }
    for (var i = 0; i < $social.length; i++) {
        $($social[i]).find("div").css("width",MLjson.Social[$($social[i]).find("span")[0].innerHTML]*100 + "%");
        $($social[i]).find(".percent").html(" "+ Math.round(MLjson.Social[$($social[i]).find("span")[0].innerHTML]*100) + "%");
    }

    total = $(".ml_cont .overalltotal");
    total.find("div").css("width",MLjson.Total*100 + "%");
    total.find(".percent").html(Math.round(MLjson.Total*100) + "%");

    //KEY WORDS
    keywords = $(".ml_cont .keywords ul");
    keywords.html("");
    str = "";
    for (var i = 0; i < MLjson.Keywords.length; i++) {
        str += "<li>"+MLjson.Keywords[i]+"</li>";
    }
    keywords.html(str);
}
function setupOverview(data){
    $reliable = $(".content_cont .overview_cont .reliability");
    $reliable.show();
    if(data.DomainCheck == 1) $reliable.find("span").html("RELIABLE").removeClass("red").addClass("green");
    else if(data.DomainCheck == 0) $reliable.find("span").html("NOT RELIABLE, PROCEED WITH CAUTION!").removeClass("green").addClass("red");
    else $reliable.hide();


    $tab_re = $(".overview_cont ul li");

    if(data.MachineLearning.Total) $($tab_re[0]).find(".percent").html(Math.round(data.MachineLearning.Total*100)+"%");
    else $($tab_re[0]).find(".percent").html("(no available data)");
    $($tab_re[1]).find(".percent").html(Math.round(data.SearchResults.SearchReliability*100)+"%");
    //$($tab_re[2]).find(".percent").html(Math.round(data.TotalReliability*100)+"%");


}
function setupGoogle(data){
    googleJson = data.SearchResults;
    google = $(".google_cont");
    google.find(".total_results").html(googleJson.NumResults);
    keywords = data.MachineLearning.Keywords[0] + " " + data.MachineLearning.Keywords[1] + " " + data.MachineLearning.Keywords[2];
    google.find(".searched_keywords").html(keywords);
    google.find(".percent").html(Math.round(googleJson.SearchReliability*100)+"%");

    google.find(".overalltotal div").css("width",Math.round(googleJson.SearchReliability*100)+"%");
    str = '';
    for (var i = 0; i < googleJson.URLs.length; i++) {
        reliability_class = googleJson.URLs[i].reliable ? 'valid':'invalid';
        reliability_str = googleJson.URLs[i].reliable ? 'RELIABLE':'NOT RELIABLE';
        if(googleJson.URLs[i].reliable==2){
            reliability_class = 'unknown';
            reliability_str = 'UNKNOWN RELIABILITY';
        }
        str += '<li class="'+reliability_class+'"><a href="'+googleJson.URLs[i].url+'" target="_blank"><span class="url">' + googleJson.URLs[i].url + '</span><span>' + reliability_str + '</span></a></li>';
    }
    google.find("ul").html(str);
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
