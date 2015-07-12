function submit_image(link,button)

	$.getJSON('/_getlink',{
		a:$('input[name="url1']).val(),
		b:$('input[name="url2']).val()
	})
		,function(data){
			
			alert("Data sent");}
			});

}


function check(b)
{
	alert(b);

}
