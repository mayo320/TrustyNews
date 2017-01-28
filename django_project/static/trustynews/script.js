var trusynews = angular.module("trustynews",[]);
trusynews.controller("search-ctrl",function($scope){
    $scope.search= function(){
        _url = $("input[name='searchURL']").val();
        $.ajax({
           url: "{% url 'searchURL' %}",
           type: "POST",
           data: {
               'url':_url,
               csrfmiddlewaretoken: "{{ csrf_token }}"
           },
           success:function(json){
               console.log(json);
           },
           error:function(){
               alert("no");
           }
        });
    }

}
