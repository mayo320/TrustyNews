$(document).ready(function(){
    $("button[name='go']").attr('disabled', false);
});

var myApp = angular.module("myApp",[]);
myApp.controller("google_ctrl",function($scope){

});

function setupML(MLjson){
    $cols = $(".ml_cont .stats .col ul");
    $emotion = $($cols[0]).find("li");
    $lang = $($cols[1]).find("li");
    $social = $($cols[2]).find("li");

    for (var i = 0; i < $emotion.length; i++) {
        $($emotion[i]).find("div").css("width",MLjson.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100 + "%");
        $($emotion[i]).find(".percent").css("width",Math.round(MLjson.Emotion[$($emotion[i]).find("span")[0].innerHTML]*100) + "%");
    }
    for (var i = 0; i < $lang.length; i++) {
        $($lang[i]).find("div").css("width",MLjson.Language[$($lang[i]).find("span")[0].innerHTML]*100 + "%");
        $($lang[i]).find(".percent").css("width",Math.round(MLjson.Language[$($lang[i]).find("span")[0].innerHTML]*100) + "%");
    }
    for (var i = 0; i < $social.length; i++) {
        $($social[i]).find("div").css("width",MLjson.Social[$($social[i]).find("span")[0].innerHTML]*100 + "%");
        $($social[i]).find(".percent").css("width",Math.round(MLjson.Social[$($social[i]).find("span")[0].innerHTML]*100) + "%");
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
    if(data.DomainCheck){
        $reliable = $(".content_cont .overview_cont .reliability");
        $reliable.show();
        if(data.DomainCheck == 1) $reliable.find("span").html("RELIABLE");
        else if(data.DomainCheck == 0) $reliable.find("span").html("NOT RELIABLE");
        else $reliable.hide();
    }

    $tab_re = $(".overview_cont ul li");

    $($tab_re[0]).find(".percent").html(Math.round(data.MachineLearning.Total*100)+"%");
    //$($tab_re[1]).find(".percent").html(Math.round(data.Google.Total*100)+"%");


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
