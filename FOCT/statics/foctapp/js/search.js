 var fsj_l=[];
 var fsj_r=[];
 var fsj_d=[];
 var data_content=[];
$(document).ready(function(){
	$("#select1 dd").click(function () {
        $(this).addClass("selected").siblings().removeClass("selected");
        var content=$(this).text();
        fsj_l=[];
        fsj_l.push(content);
        data_content=[fsj_l,fsj_d,fsj_r];
        var post_data=JSON.stringify(data_content);
        var search_data= $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/foctapp/qurry',
            data:{'fsj':post_data},
            dataType:'json'
        });
    });
    	$("#select2 dd").click(function () {
            $(this).addClass("selected").siblings().removeClass("selected");
            $(this).addClass("selected");
            var content = $(this).text();
            fsj_r=[];
            fsj_r.push(content);
            data_content=[fsj_l,fsj_d,fsj_r];
            var post_data = JSON.stringify(data_content);
        var search_data = $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/foctapp/qurry',
            data:{'fsj':post_data},
            dataType:'json'
        });
	});
    	$("#select3 dd").click(function () {
            $(this).addClass("selected").siblings().removeClass("selected");
            $(this).addClass("selected");
            var content = $(this).text();
            fsj_d=[];
            fsj_d.push(content);
            data_content=[fsj_l,fsj_d,fsj_r]
            var post_data = JSON.stringify(data_content);
        var search_data = $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/foctapp/qurry',
            data:{'fsj':post_data},
            dataType:'json'
        });
});
});

